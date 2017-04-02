#!/bin/python

import sys

def check_wakeup(seem):
    final_list = ['0','1','2','3','4','5','6','7','8','9']
    #print sorted(seem)	  
    if sorted(seem) == final_list:
	#fall asleep
	return True
    else:
        return False

def split_digits(seem, number):
    str_nb = str(number)

    for digit in str_nb:
        if not digit in seem:
	    seem.append(digit)

def last_number(number):
    seem = []
    i = 0
    while not check_wakeup(seem):
	test_number = (i+1)*number
	split_digits(seem, test_number)
	i = i + 1
    return test_number

def main():

    with open(sys.argv[1], "r") as file_input, open(sys.argv[2], "w") as file_output:
        nb = file_input.readline()
   
        t = int(nb)
        last_nb = 0

        for index in xrange(t):
            nb = int(file_input.readline())
     	     
	    if (nb) != 0:
	        last_nb = last_number(nb)
            	print "Case #{}: {}".format(index+1, last_nb)
		file_output.write("Case #{}: {}\n".format(index+1, last_nb))
	    else:
            	print "Case #{}: INSOMNIA".format(index+1)
		file_output.write("Case #{}: INSOMNIA\n".format(index+1))
	
main()




