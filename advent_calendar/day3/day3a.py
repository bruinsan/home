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
	memory = [[0 for x in xrange(10)] for y in xrange(10)]  # creating 11x11 matrix

	# RU
	x_init = 5
	y_init = 5
	start_num = 1
	memory[x_init][y_init] = start_num
	add = 1

	while start_num <= final_pos:  # change the condition for stopping when final_pos achieved
		# RU --> LD --> RU
		#		print "x_init = {} \t y_init = {} \t start_num = {}".format(x_init, y_init, start_num)
		print "updating..."
		x_init, y_init, start_num = move_right(memory, x_init, y_init, start_num, add, final_pos)
		x_init, y_init, start_num = move_down(memory, x_init, y_init, start_num, add, final_pos)
		x_init, y_init, start_num = move_left(memory, x_init, y_init, start_num, add + 1, final_pos)
		x_init, y_init, start_num = move_up(memory, x_init, y_init, start_num, add + 1, final_pos)

		add += 2

		#print start_num
		#print final_pos
	#	print ""
#	print memory
	return memory


def find_min(memory, number):

	return 0
	pass

def calculate_manhattan_distance(nb, memory):
	# find minimum neighbor
	dist = 0
	neighbor = -1
	while neighbor != 1:
		neighbor = find_min(memory, nb)
		dist += 1
		nb = neighbor

pprint(create_spiral_memory(1))
memory = create_spiral_memory(2)
pprint(create_spiral_memory(3))
#create_spiral_memory(4)
#create_spiral_memory(1024)


