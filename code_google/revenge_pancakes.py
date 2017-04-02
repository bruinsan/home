
#!/bin/python

import sys

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




