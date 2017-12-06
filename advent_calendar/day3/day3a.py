import sys

memory_position = sys.argv[1]

def create_spiral_memory(final_pos):
	memory = [[0 for x in xrange(11)] for y in xrange(11)]	# creating 11x11 matrix

	# RU
	x_init = 5
	y_init = 5
	memory[x_init][y_init] = 1
	memory[x_init+1][y_init] = 2

	while True:	# change the condition for stopping when final_pos achieved
		# RU --> LD --> RU
		memory[][]
		

		

