input_file = "input.txt"

def create_tree_dict():
    dct = dict()
    with open(input_file, "r") as fl:
        for line in fl:
            list_line = line.replace(',','').split()    # replace commas and split on spaces
            if "->" in list_line:
                dct[list_line[0]] = [list_line[1].strip('()'),list_line[3:]]
            else:
                dct[list_line[0]] = [list_line[1].strip('()'),None]
    return dct
'''         line = fl.readline().split()
    
    list_int = list()
    for nb in line:
        list_int.append(int(nb))

    return list_int

 '''

if __name__ == "__main__":
    d = create_tree_dict()
    print d