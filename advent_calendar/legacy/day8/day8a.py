from pprint import pprint
import sys

input_file = sys.argv[1]

class Register:

    def __init__(self):
        pass

    u

def read_instructions():
    registers = list()

    with open(input_file, "r") as fl:
        for instruction in fl:
            register = instruction.split()[0]
            if not register in registers:
                registers.append(register)


if __name__ == "__main__":
