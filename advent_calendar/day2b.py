import sys

input_file = "input_day2a.txt"

sum = 0

with open(input_file, "r") as f:
	lines = [x.split() for x in f.readlines()]
	lines = [[int(x) for x in i] for i in lines]
	for line in lines:
		sum += (int(max(line)) - int(min(line)))

print sum
