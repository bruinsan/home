import sys

input_file = "input_day2b.txt"

sum = 0

def find_evenly_divisible(line):
	ordered_line = sorted(line, reverse=True)
	aux_ord_line = list(ordered_line)
	for nb in ordered_line:
		del aux_ord_line[0]
		for rest in aux_ord_line:
			if (nb % rest) == 0:
				return nb, rest
		
with open(input_file, "r") as f:
	lines = [x.split() for x in f.readlines()]
	lines = [[int(x) for x in i] for i in lines]
	for line in lines:
		a, b = find_evenly_divisible(line)
		sum += a/b

print sum
