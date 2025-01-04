import sys

input = sys.argv[1]

sum = 0

for index,number in enumerate(input):
    if input[index] == input[(index + 1)%len(input)]:
       sum += int(input[index])

print sum
