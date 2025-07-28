"""
Convert the ram map into markdown
"""

from dataclasses import dataclass

@dataclass
class Field:
	name : str
	bit_len : int
	bit_offset : int

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
