import sys
from pprint import pprint

#memory_position = sys.argv[1]


def move_right(mem, x, y, actual_nb, times, final_pos):
	for i in xrange(times):
		actual_nb += 1
	#	print x+i+1
		if actual_nb <= final_pos:
			mem[y][x + i + 1] = actual_nb

	return x + times, y, actual_nb


def move_up(mem, x, y, actual_nb, times, final_pos):
	for i in xrange(times):
		actual_nb += 1
		if actual_nb <= final_pos:
			mem[y + i + 1][x] = actual_nb

	return x, y + times, actual_nb


def move_left(mem, x, y, actual_nb, times, final_pos):
	for i in xrange(times):
		actual_nb += 1
		if actual_nb <= final_pos:
			mem[y][x - i - 1] = actual_nb

	return x - times, y, actual_nb


def move_down(mem, x, y, actual_nb, times, final_pos):
	for i in xrange(times):
		actual_nb += 1
		if actual_nb <= final_pos:
			mem[y - i - 1][x] = actual_nb

	return x, y - times, actual_nb


def create_spiral_memory(final_pos):
	size = int(sys.argv[2])
	max = int(sys.argv[3])
	memory = [[max for x in xrange(size)]
           for y in xrange(size)]  # creating 11x11 matrix

	# RU
	x_init = 5
	y_init = 5
	start_num = 1
	memory[x_init][y_init] = start_num
	add = 1

	while start_num <= final_pos:  # change the condition for stopping when final_pos achieved
		# RU --> LD --> RU
		x_init, y_init, start_num = move_right(
			memory, x_init, y_init, start_num, add, final_pos)
		x_init, y_init, start_num = move_down(
			memory, x_init, y_init, start_num, add, final_pos)
		x_init, y_init, start_num = move_left(
			memory, x_init, y_init, start_num, add + 1, final_pos)
		x_init, y_init, start_num = move_up(
			memory, x_init, y_init, start_num, add + 1, final_pos)

		add += 2

	return memory

"""
def find_number(matrix, nb):
	for i, row in enumerate(matrix):
		for j, col in enumerate(row):
			if col == nb:
				return i, j
"""

def find_min(memory, number):
	#y, x = find_number(memory, number)
	for i, row in enumerate(memory):
			for j, col in enumerate(row):
				if col == number:
					y = i
					x = j

	print memory[x + 1][y], memory[x - 1][y], memory[x][y + 1], memory[x][y - 1]
	min_nb = min(memory[x + 1][y], memory[x - 1][y],
	             memory[x][y + 1], memory[x][y - 1])

	#print "min neighbor = {}".format(min_nb)
	return min_nb


def calculate_manhattan_distance(nb, memory):
	# find minimum neighbor
	dist = 0
	neighbor = -1
	print memory
	print ""
	while neighbor != 1:
		# print memory, nb
		neighbor = find_min(memory, nb)
		dist += 1
		nb = neighbor
		# print nb

	return dist

final_num = int(sys.argv[1])
memory = create_spiral_memory(final_num)
#print memory
#pprint(memory)
print calculate_manhattan_distance(final_num, memory)
#find_min(memory, 9)
