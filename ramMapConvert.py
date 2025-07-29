"""
Convert the ram map into markdown
"""

from dataclasses import dataclass
import math

@dataclass
class Field:
	name : str
	bit_len : int
	bit_offset : int

	def extract_from(self, arr : bytearray) -> bytes:
		ecram_int = int.from_bytes(arr, byteorder='little')
		ecram_int >>= self.bit_offset
		ecram_int &= (1 << self.bit_len) - 1

		return ecram_int.to_bytes(math.ceil(self.bit_len / 8), byteorder='little')
	def gen_patched_bytes(self, arr : bytearray, value : bytes) -> bytes:
		ecram_int = int.from_bytes(arr, byteorder='little')

		value_int = int.from_bytes(value, byteorder='little')
		if value_int.bit_length() > self.bit_len:
			raise ValueError("Value too large for field")

		value_int <<= self.bit_offset


		val_mask = ( (1 << self.bit_len) - 1 ) << self.bit_offset

		ecram_int &= ~val_mask
		ecram_int |= value_int

		return ecram_int.to_bytes(len(arr), byteorder='little')


def load(path : str) -> list[Field]:
	f = open(path, "r")
	dsl = f.read()
	f.close()
	
	table_str = dsl.split("Field (ERAM")[1].split("{")[1].split("}")[0]
	strs = iter((e.strip() for e in table_str.split(",")))

	fields = []
	location = 0
	try:
		while True:
			first = next(strs).strip()
			if first.startswith("Offset"):
				# Function to set absolute offset
				loc = first.split("(")[1].split(")")[0].strip()
				assert loc.startswith("0x")
				loc = loc[2:]
				location = int(loc, 0x10) * 8
			else:
				# Only 4 letter names are allowed
				assert len(first) == 4 or len(first) == 0
				secound = int(next(strs))
				
				fields.append(Field(
					name=first,
					bit_len = int(secound),
					bit_offset = location
				))

				location += secound
	except StopIteration:
		pass
	return fields
def gen_md_table(table : list[Field], space_len = 16):
	out = [
		["Name", "Byte offset", "Inner bit offset", "Bit length", "Comment"],
		["-"*space_len]*5
	]
	for field in table:
		out.append([

			field.name, str(hex(field.bit_offset // 8)), field.bit_offset % 8, field.bit_len, ""
		])

	ret = ""
	for col in out:
		col = map(str, col)
		col = [i + " " * max(0, space_len - len(i)) + "|" for i in col]
		ret += "|" + "".join(col) + "\n"
	print(ret)


if __name__ == "__main__":
	gen_md_table(load("bins/dsdt.dsl"))
