import sys
from pprint import pprint

#memory_position = sys.argv[1]

def move_right(mem, x, y, actual_nb, times):
	for i in xrange(times):
		actual_nb += 1
		mem[x+i+1][y] = actual_nb

	return x+times, y, actual_nb

def move_up(mem, x, y, actual_nb, times):
	for i in xrange(times):
		actual_nb += 1
		mem[x][y+i+1] = actual_nb
		
	return x, y+times, actual_nb

def move_left(mem, x, y, actual_nb, times):
	for i in xrange(times):
		actual_nb += 1
		mem[x-i-1][y] = actual_nb

	return x-times, y, actual_nb

def move_down(mem, x, y, actual_nb, times):
	for i in xrange(times):
		actual_nb += 1
		mem[x][y-i-1] = actual_nb

	return x, y-times, actual_nb



def create_spiral_memory(final_pos):
	memory = [[0 for x in xrange(11)] for y in xrange(11)]	# creating 11x11 matrix

	# RU
	x_init = 5
	y_init = 5
	start_num = 1
	memory[x_init][y_init] = start_num
	add = 1
	
	while True:	# change the condition for stopping when final_pos achieved
		# RU --> LD --> RUi
		print "x_init = {} \t y_init = {} \t start_num = {}".format(x_init, y_init, start_num)
		pprint(memory)
		print ""

		x_init, y_init, start_num  = move_right(memory, x_init, y_init, start_num, add)
#		x_init, y_init, start_num  = move_up(memory, x_init, y_init, start_num, add)
#		x_init, y_init, start_num  = move_left(memory, x_init, y_init, start_num, add+1)
#		x_init, y_init, start_num  = move_down(memory, x_init, y_init, start_num, add+1)
		
		add += 2

	print memory

create_spiral_memory(1)
#create_spiral_memory(2)
#create_spiral_memory(3)
#create_spiral_memory(4)
#create_spiral_memory(5)


