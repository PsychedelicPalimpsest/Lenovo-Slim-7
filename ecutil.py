import sys, subprocess, os, argparse
from ramMapConvert import *


def get_ec_data():
	result = subprocess.run(['ectool', '-d'], capture_output=True, text=True)
	if 0 != result.returncode:
		print("ERROR: Please run script as root, or provide an EC dump file")
		exit(1)
	return result.stdout

def patch_ec(old : bytearray, new : bytearray, dry_run : bool = False):
	patches = [(hex(i), hex(new[i])) for i in range(len(old)) if old[i] != new[i]]
	commands = [
		["ectool", "-w", addr, "-z", val] for addr, val in patches
	]
	for command in commands:
		if dry_run:
			print(" ".join(command))
		else:
			result = subprocess.run(command)
			if 0 != result.returncode:
				print("ERROR: Unknown EC writing error")
				exit(1)
def check_or_get_ec_dump(path):
	if path:
		assert os.path.exists(path), "File not found"
		with open(path, "r") as f:
			data = f.read()
	else:
		data = get_ec_data()

	return dump_to_bytes(data)


class Map:
	fields : dict
	def __init__(self, path : str):
		table = load("bins/dsdt.dsl")
		self.fields = {f.name : f for f in table if f.name.strip()}


def dump_to_bytes(file : str) -> bytearray:
	assert file.startswith("EC RAM:")
	datalines = file.split("\n")[2:]

	bytedata_packed = (
		line.strip().split(": ")[1].split(" ")
		for line in datalines if line.strip()
	)
	hexdata = "".join(byte for line in bytedata_packed for byte in line if byte)
	return bytearray.fromhex(hexdata)


def main():
	parser = argparse.ArgumentParser(description="EcUtils: EC RAM tinkering program")

	subparsers = parser.add_subparsers(dest='command', required=True)

	file_help = "Path to EC dump file. With read type operations uses the file instead of the real ec ram"

	# list command
	list_parser = subparsers.add_parser('list', help="List all the fields and their values")
	list_parser.add_argument('-f', '--file', help=file_help)

	# numext command
	numext_parser = subparsers.add_parser('numext', help="Extract decimal value of a field")
	numext_parser.add_argument('key', help="Field name")
	numext_parser.add_argument('-f', '--file', help=file_help)
	

	# binext command
	binext_parser = subparsers.add_parser('binext', help="Extract binary value of a field")
	binext_parser.add_argument('key', help="Field name")
	binext_parser.add_argument('-f', '--file', help=file_help)

	# numset command
	numset_parser = subparsers.add_parser('numset', help="Set decimal value of a field")
	numset_parser.add_argument('key', help="Field name")
	numset_parser.add_argument('value', type=int, help="Integer value to set")
	numset_parser.add_argument('-r', '--dry-run', action='store_true', help="Print the patch commands, but do not execute them")

	

	args = parser.parse_args()
	mp = Map("bins/dsdt.dsl")

	if args.command == 'list':
		data = check_or_get_ec_dump(args.file)
		print("Valid ec ram fields:")
		for k, f in mp.fields.items():
			bts = f.extract_from(data)	
			print(f"\t{k}\t {f.bit_len} bits\t\t{bts}")

	elif args.command in ['numext', 'binext']:
		data = check_or_get_ec_dump(args.file)
		field = mp.fields.get(args.key)
		if field is None:
			print(f"Key not found: {args.key}")
			exit(1)

		value = field.extract_from(data)
		if args.command == 'binext':
			sys.stdout.buffer.write(value)
			sys.stdout.buffer.flush()
		else:
			print(int.from_bytes(value, byteorder='little'))

	elif args.command == 'numset':
		data = dump_to_bytes(get_ec_data())
		field = mp.fields.get(args.key)
		if field is None:
			print(f"Key not found: {args.key}")
			exit(1)
		patched = field.gen_patched_bytes(data, int(args.value).to_bytes(math.ceil(field.bit_len / 8), byteorder='little'))
		patch_ec(data, patched, args.dry_run)

if __name__ == "__main__":
	main()
