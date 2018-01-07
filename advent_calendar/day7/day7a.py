from pprint import pprint

input_file = "input.txt"

def create_tree_list():
    tree_list = dict()

    with open(input_file, "r") as fl:
        for line in fl:
            # replace commas and split on spaces
            list_line = line.replace(',', '').split()
            if "->" in list_line:
                tree_list[list_line[0]] = {'weight':list_line[1].strip('()'), 'child':list_line[3:]}
            else:
                tree_list[list_line[0]] = {'weight':list_line[1].strip('()'), 'child':None}
    return tree_list

def update_parents_dict(tree):
    """
    tree here are a dictionary
    where the keys are the names and the values
    dictionaries for weight and children

    it should return a list with a the pair
    [element,parent]
    """
    elements = dict()

    for val in tree.values():
        if val['child'] == None:
        # it is a parent
        # we need to update 
            pass

    return elements

if __name__ == "__main__":
    d = create_tree_list()
    import IPython;IPython.embed()
    pprint(d)