"""
An EcRam diffing tool. Forgive my lack of comments, readability
or functionality.

It is intended to be used by a DEVELOPER!
To create your EcRam dumps use the following command:
sudo ectool -d
"""





import glob
from dataclasses import dataclass

BG_BLACK = "\033[0;90m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
FAINT = "\033[2m"


RESET = "\033[0m"

@dataclass
class Byte:
	value : str
	was_reduced : bool = False
	was_changed : bool = False
	was_l_reduced : bool = False

	def __str__(self):
		if self.was_l_reduced:
			return f"{BG_BLACK}{self.value}{RESET}"
		if self.was_reduced:
			return f"{BG_RED}{self.value}{RESET}"
		if self.was_changed:
			return f"{BG_YELLOW}{self.value}{RESET}"

		
		return self.value
	def copy_state(self, other):
		self.was_reduced = other.was_reduced
		self.was_changed = other.was_changed
		self.was_l_reduced = other.was_l_reduced


EcFile = list[Byte]


def parse(file : str) -> EcFile:
	assert file.startswith("EC RAM:")
	datalines = file.split("\n")[2:]

	bytedata_packed = (
		line.strip().split(": ")[1].split(" ")
		for line in datalines if line.strip()
	)
	bytedata = [Byte(byte) for line in bytedata_packed for byte in line if byte]

	return bytedata



def fancy_str(file : EcFile, tabs=0) -> str:

	strs = [
		str(bt)
		for bt in file
	]


	bt_lines = [
		"\t"*tabs 
		+ hex(i * 0x10) + "\t" + " ".join(strs[i*0x10 : i*0x10 + 0x10])
		for i in range(len(strs) // 0x10)
	]
	return "\n".join(bt_lines) + "\n"
	
def fancy_print(file : EcFile, tabs=0):
	print(fancy_str(file, tabs=tabs))

def reduction_diff(dst : EcFile, src : EcFile):
	assert len(src) == len(dst)

	for i in range(len(dst)):
		dst[i].was_reduced |= dst[i].value != src[i].value
		src[i].copy_state(dst[i])
def selection_diff(dst : EcFile, src : EcFile):
	assert len(src) == len(dst)

	for i in range(len(dst)):
		dst[i].was_changed |= dst[i].value != src[i].value
		src[i].copy_state(dst[i])

def multi_reduction(dst : EcFile, stages : list[str], debug : bool = False):
	for s in stages:
		src = loadf(s)
		reduction_diff(dst, src)
		if debug:
			print("With", s + ":")
			fancy_print(dst)
			fancy_print(src, tabs=1)
def multi_selection(dst : EcFile, stages : list[str], debug : bool = False):
	for s in stages:
		src = loadf(s)
		selection_diff(dst, src)
		if debug:
			print("With", s + ":")
			fancy_print(dst)
			fancy_print(src, tabs=1)

def reduction_glob(dst : EcFile, stages : str, debug : bool = False):
	multi_reduction(dst, list(sorted(glob.glob(stages))), debug = debug)



def reduce_lambda(file : EcFile, predicate):
	for b in file:
		b.was_l_reduced |= not predicate(int(b.value, 0x10))



def loadf(path : str):
	f = open(path, "r")
	data = f.read()
	f.close()
	return parse(data)

if __name__ == "__main__":
	on = loadf("ecdumps/led_on.bin")

	off = loadf("ecdumps/led_off.bin")
	reduction_diff(off, loadf("ecdumps/led_off2.bin"))
	selection_diff(off, on)


	print("off:")
	fancy_print(off, 1)
	print("on:")
	fancy_print(on, 1)

	
	
	


	



