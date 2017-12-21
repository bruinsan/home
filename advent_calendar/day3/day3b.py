import sys
from pprint import pprint
from math import sqrt, ceil

finished = 0

def move_right(mem, x, y, times, final_pos):
	global finished
	#print "[RIGHT_START] x = {} \t y = {}".format(x, y)

	for i in xrange(times):
	#	print "[RIGHT] x = {} \t y = {}".format(x + i + 1, y)
		r = x + i + 1
		positions = [mem[y + 1][r - 1], mem[y + 1][r], mem[y + 1][r + 1], mem[y][r - 1],
                    mem[y][r], mem[y][r + 1], mem[y - 1][r - 1], mem[y - 1][r], mem[y - 1][r + 1]]
	#	print positions
		actual_nb = sum(positions)
		if actual_nb <= final_pos:
			print actual_nb
			mem[y][r] = actual_nb
#			if actual_nb == final_pos:
#				break
	# 	# x += 1
		else:
			finished = 1
			break

	return x + times, y, actual_nb


def move_left(mem, x, y, times, final_pos):
	global finished
	# print "[LEFT_START] x = {} \t y = {}".format(x, y)
	for i in xrange(times):
		# print "[LEFT] x = {} \t y = {}".format(x-i-1, y)
		r = x - i - 1
		positions = [mem[y + 1][r - 1], mem[y + 1][r], mem[y + 1][r + 1], mem[y][r - 1],
                    mem[y][r], mem[y][r + 1], mem[y - 1][r - 1], mem[y - 1][r], mem[y - 1][r + 1]]
	 #	print positions
		actual_nb = sum(positions)
		if actual_nb <= final_pos:
			print actual_nb
			mem[y][r] = actual_nb
			#if actual_nb == final_pos:
			#	break
	# 		mem[y][x - i - 1] = actual_nb
		else:
			finished = 1
			break
	# 	x=x-i

	return x - times, y, actual_nb


def move_up(mem, x, y, times, final_pos):
	global finished
	#print "[UP_START] x = {} \t y = {}".format(x, y)

	for i in xrange(times):
	#	print "[UP] x = {} \t y = {}".format(x, y-i-1)
		s = y - i - 1
		positions = [mem[s + 1][x - 1], mem[s + 1][x], mem[s + 1][x + 1], mem[s][x - 1],
                    mem[s][x], mem[s][x + 1], mem[s - 1][x - 1], mem[s - 1][x], mem[s - 1][x + 1]]
	#	print positions
	# 	print "x = {} \t y = {}".format(x, y)

		actual_nb = sum(positions)
		if actual_nb <= final_pos:
			print actual_nb
			mem[s][x] = actual_nb
#			if actual_nb == final_pos:
#				break
		else:
			finished = 1
			break

	return x, y - times, actual_nb


def move_down(mem, x, y, times, final_pos):
	global finished
	# print "[DOWN_START] x = {} \t y = {}".format(x, y)

	for i in xrange(times):
		# print "[DOWN] x = {} \t y = {}".format(x, y+i+1)
		s = y + i + 1
		positions = [mem[s + 1][x - 1], mem[s + 1][x], mem[s + 1][x + 1], mem[s][x - 1],
                    mem[s][x], mem[s][x + 1], mem[s - 1][x - 1], mem[s - 1][x], mem[s - 1][x + 1]]
		actual_nb = sum(positions)
		if actual_nb <= final_pos:
			print actual_nb
			mem[s][x] = actual_nb
#			if actual_nb == final_pos:
#				break
	# 		mem[y + i + 1][x] = actual_nb
		else:
			finished = 1
			break

	return x, y + times, actual_nb


def create_spiral_memory(final_pos):
	global finished
	#size = int(sys.argv[2])
	size = int(ceil(sqrt(final_pos)))
	
	memory = [[0 for x in xrange(size)]
           for y in xrange(size)]  # creating 11x11 matrix

	# RU
	x_init = len(memory) / 2 - 1
	y_init = len(memory) / 2 - 1
	actual_nb = 1
	memory[x_init][y_init] = actual_nb
	add = 1

	while actual_nb <= final_pos:  # change the condition for stopping when final_pos achieved
		x_init, y_init, actual_nb = move_right(memory, x_init, y_init, add, final_pos)
		#print "x = {} \t y = {} \t actual_nb = {}".format(x_init, y_init, actual_nb)
		if finished:
			break
		x_init, y_init, actual_nb = move_up(memory, x_init, y_init, add, final_pos)
		if finished:
			break
		#print "x = {} \t y = {} \t actual_nb = {}".format(x_init, y_init, actual_nb)
		x_init, y_init, actual_nb = move_left(memory, x_init, y_init, add + 1, final_pos)
		if finished:
			break
		#print "x = {} \t y = {} \t actual_nb = {}".format(x_init, y_init, actual_nb)
		x_init, y_init, actual_nb = move_down(memory, x_init, y_init, add + 1, final_pos)
		if finished:
			break
		#print "x = {} \t y = {} \t actual_nb = {}".format(x_init, y_init, actual_nb)

		add += 2
		# pprint(memory)
	return actual_nb


final_num = int(sys.argv[1])
m = create_spiral_memory(final_num)
print m

#pprint(m)
