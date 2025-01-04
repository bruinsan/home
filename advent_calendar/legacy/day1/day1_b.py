import sys

input = sys.argv[1]

sum = 0
length = len(input)


for index,number in enumerate(input):
    if input[index] == input[(index + length/2)%len(input)]:
       sum += int(input[index])

print sum
