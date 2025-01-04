
input_file = "input_file.txt"

def jump_out_maze(l):
    # check while iterator is still inside vector
    iterator = 0
    counter = 0
    size = len(l)
    
    while (iterator >= 0 and iterator < size):
        #print "iterator = {} \t crazy_list = {}".format(iterator, list_input)
        elem = l[iterator]
        
        l[iterator] += 1
        iterator = iterator + elem
        counter += 1

    return counter

def read_input():
    l = list()
    with open(input_file, "r") as fl:
        for line in fl:
            l.append(int(line))
    return l

list_input = read_input()

print jump_out_maze(list_input)