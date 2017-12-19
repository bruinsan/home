import sys
from pprint import pprint
from math import sqrt, ceil

def move_right(mem, x, y, times, final_pos):
	print "[RIGHT_START] x = {} \t y = {}".format(x, y)

	for i in xrange(times):
	# 	positions = [mem[y+1][x-1], mem[y+1][x], mem[y+1][x+1], mem[y][x-1], mem[y][x], mem[y][x+1], mem[y-1][x-1], mem[y-1][x], mem[y-1][x+1]]
	# 	print positions
		print "[RIGHT] x = {} \t y = {}".format(x+i+1, y)
	# 	actual_nb = sum(positions)
	# 	if actual_nb <= final_pos:
	# 		mem[y][x] = actual_nb
	# 	# x += 1

	return x+times, y

def move_left(mem, x, y, times, final_pos):
	print "[LEFT_START] x = {} \t y = {}".format(x, y)
	for i in xrange(times):
		print "[LEFT] x = {} \t y = {}".format(x-i-1, y)
	# 	positions = [mem[y+1][x-1], mem[y+1][x], mem[y+1][x+1], mem[y][x-1], mem[y][x], mem[y][x+1], mem[y-1][x-1], mem[y-1][x], mem[y-1][x+1]]
	# 	print positions, x, y
	# 	actual_nb = sum(positions)
	# 	if actual_nb <= final_pos:
	# 		mem[y][x - i - 1] = actual_nb
	# 	x=x-i
	# # mem[y][x] = "X"
	return x - times, y


def move_up(mem, x, y, times, final_pos):
	print "[UP_START] x = {} \t y = {}".format(x, y)

	for i in xrange(times):
		print "[UP] x = {} \t y = {}".format(x, y-i-1)
	# 	positions = [mem[y+1][x-1], mem[y+1][x], mem[y+1][x+1], mem[y][x-1], mem[y][x], mem[y][x+1], mem[y-1][x-1], mem[y-1][x], mem[y-1][x+1]]
	# 	print positions
	# 	print "x = {} \t y = {}".format(x, y)

	# 	actual_nb = sum(positions)
	# 	if actual_nb <= final_pos:
	# 		mem[y][x] = actual_nb

	return x, y - times

def move_down(mem, x, y, times, final_pos):
	print "[DOWN_START] x = {} \t y = {}".format(x, y)

	for i in xrange(times):
		print "[DOWN] x = {} \t y = {}".format(x, y+i+1)
	# 	positions = [mem[y+1][x-1], mem[y+1][x], mem[y+1][x+1], mem[y][x-1], mem[y][x], mem[y][x+1], mem[y-1][x-1], mem[y-1][x], mem[y-1][x+1]]
	# 	actual_nb = sum(positions)
	# 	if actual_nb <= final_pos:
	# 		mem[y + i + 1][x] = actual_nb

	return x, y + times

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
		x_init, y_init = move_right(memory, x_init, y_init, add, final_pos)
		x_init, y_init = move_up(memory, x_init, y_init, add, final_pos)
		x_init, y_init = move_left(memory, x_init, y_init, add+1, final_pos)
		x_init, y_init = move_down(memory, x_init, y_init, add+1, final_pos)

		add += 2
		pprint(memory)
		start_num += 1
	return memory


final_num = int(sys.argv[1])
memory = create_spiral_memory(final_num)
pprint(memory)
#print calculate_manhattan_distance(final_num, memory)
