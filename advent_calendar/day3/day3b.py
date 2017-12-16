import sys
from pprint import pprint
from math import sqrt, ceil

def move_right(mem, x, y, times, final_pos):
	for i in xrange(times):
		positions = [mem[y+1][x-1], mem[y+1][x], mem[y+1][x+1], mem[y][x-1], mem[y][x-1], mem[y][x], mem[y-1][x-1], mem[y-1][x], mem[y-1][x+1]]
		print positions
		actual_nb = sum(positions)
	#	print x+i+1
		if actual_nb <= final_pos:
			mem[y][x + i + 1] = actual_nb

	return x + times, y, actual_nb


def move_up(mem, x, y, times, final_pos):
	for i in xrange(times):
		positions = [mem[y+1][x-1], mem[y+1][x], mem[y+1][x+1], mem[y][x-1], mem[y][x-1], mem[y][x], mem[y-1][x-1], mem[y-1][x], mem[y-1][x+1]]
		actual_nb = sum(positions)
		if actual_nb <= final_pos:
			mem[y + i + 1][x] = actual_nb

	return x, y + times, actual_nb


def move_left(mem, x, y, times, final_pos):
	for i in xrange(times):
		positions = [mem[y+1][x-1], mem[y+1][x], mem[y+1][x+1], mem[y][x-1], mem[y][x-1], mem[y][x], mem[y-1][x-1], mem[y-1][x], mem[y-1][x+1]]
		actual_nb = sum(positions)
		if actual_nb <= final_pos:
			mem[y][x - i - 1] = actual_nb

	return x - times, y, actual_nb


def move_down(mem, x, y, times, final_pos):
	for i in xrange(times):
		positions = [mem[y+1][x-1], mem[y+1][x], mem[y+1][x+1], mem[y][x-1], mem[y][x-1], mem[y][x], mem[y-1][x-1], mem[y-1][x], mem[y-1][x+1]]
		actual_nb = sum(positions)
		if actual_nb <= final_pos:
			mem[y - i - 1][x] = actual_nb

	return x, y - times, actual_nb


def create_spiral_memory(final_pos):
	size = int(sys.argv[2])
	# size = int(ceil(sqrt(final_pos))) + 2
	# max = int(sys.argv[3])
	max = final_pos + 1

	memory = [[0 for x in xrange(size)]
           for y in xrange(size)]  # creating 11x11 matrix

	# RU
	x_init = len(memory) / 2 - 1
	y_init = len(memory) / 2 - 1
	start_num = 1
	memory[x_init][y_init] = start_num
	add = 1

	while start_num <= final_pos:  # change the condition for stopping when final_pos achieved
		pprint(memory)
		# RU --> LD --> RU
		print x_init, y_init
		x_init, y_init, start_num = move_right(memory, x_init, y_init, add, final_pos)
		print x_init, y_init
		x_init, y_init, start_num = move_down(memory, x_init, y_init, add, final_pos)
		print x_init, y_init
		x_init, y_init, start_num = move_left(memory, x_init, y_init, add+1, final_pos)
		print x_init, y_init
		x_init, y_init, start_num = move_up(memory, x_init, y_init, add+1, final_pos)
		print x_init, y_init

		add += 2

#		move_right(memory, x_init, y_init, add, final_pos)
	return memory


def find_min(memory, number):
	#y, x = find_number(memory, number)
	found = False
	for i, row in enumerate(memory):
			for j, col in enumerate(row):
				if col == number:
					y = i
					x = j
					found = True
					break
			if found:
				break

	# print "x = {} \t y = {} \t nb = {}".format(x, y, memory[y][x])
	positions = [memory[y][x + 1], memory[y]
              [x - 1], memory[y + 1][x], memory[y - 1][x]]

	min_nb = min(positions)

	# print "min neighbor = {}".format(min_nb)
	return min_nb


def calculate_manhattan_distance(nb, memory):
	# find minimum neighbor
	dist = 0
	neighbor = -1
	# print memory
	print ""
	while neighbor != 1:
		# print memory, nb
		neighbor = find_min(memory, nb)
		dist += 1
		nb = neighbor
		# print "distance = {}".format(dist)

	return dist


final_num = int(sys.argv[1])
memory = create_spiral_memory(final_num)
pprint(memory)
#print calculate_manhattan_distance(final_num, memory)
