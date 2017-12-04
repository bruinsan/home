import sys

input_file = "input_day2a_base.txt"

sum = 0

def find_evenly_divisible(line):
	ordered_line = sorted(line, reverse=True)
	print "normal_line = {} \t ordered_line = {}".format(line,ordered_line)
	for nb in ordered_line:
		print ordered_line
		del ordered_line[0]
		print "ord_line = {}".format(ordered_line)
		for rest in ordered_line:
			if (nb % rest) == 0:
				print "test = {}, rest = {}".format(nb, rest)
				return nb, rest
		
		print "nb = {} | line = {}".format(nb, ordered_line)

with open(input_file, "r") as f:
	lines = [x.split() for x in f.readlines()]
	lines = [[int(x) for x in i] for i in lines]
	for line in lines:
		find_evenly_divisible(line)
#		sum += a/b

print sum
