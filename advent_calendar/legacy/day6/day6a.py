
input_file = "input_file.txt"
output_file = "output_file.txt"

def read_input():
    with open(input_file, "r") as fl:
        line = fl.readline().split()
    
    list_int = list()
    for nb in line:
        list_int.append(int(nb))

    return list_int


def get_index_max(_list):
    list_aux = list(_list)

    list_aux.sort()

    max_elem = list_aux[-1]

    return _list.index(max_elem)

def redistribute(max_index, _list):
    block = _list[max_index]    # block to be redistributed
    _list[max_index] = 0        # change its value to zero and than redistribute
    increment = max_index
    while block > 0:
        increment = (increment + 1) % len(_list)    # wraps around to the first element and continues
        _list[increment] += 1
        block -= 1
    
    # increment counter at the end
    # return the new memory bank list
    return _list

def check_memory_bank_exists(_list):
    # check if _list doesn't exist in the file
    with open(output_file, "r") as fl:
        for line_nb, old_list in enumerate(fl):
            if old_list.split("\n")[0] == str(_list):   # convert e verything to string to compare
                return True, line_nb
        else:
            return False, line_nb

def write_list_to_file(_list):
    with open(output_file, "a") as fl:
        fl.write("{}\n".format(str(_list)))
    
def get_last_list():
    with open(output_file, "r") as fl:
        for line in fl:
            pass
    return line.split("\n")[0]

if __name__ == "__main__":
    list_input = read_input()       # get initial list
    write_list_to_file(list_input)
    
    EQUAL = False
    counter = 0
    
    while not EQUAL:
        _line = eval(get_last_list())   # convert the string to list using eval
        _line_redist = redistribute(get_index_max(_line), _line)
        ret, line_nb = check_memory_bank_exists(_line_redist)
        if not ret:
            write_list_to_file(_line_redist)
        else:
            EQUAL = True
        counter += 1
    print counter
    print counter - line_nb