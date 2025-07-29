from ecutil import *




if __name__ == "__main__":
	mp = Map("bins/dsdt.dsl")

	f = open("bins/dsdt.dsl", "r")
	cont = f.read()
	f.close()

	for k in mp.fields.keys():
		count = len(cont.split(k)) - 1
		if count > 1:
			print(k, count)