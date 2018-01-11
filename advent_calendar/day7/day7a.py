from pprint import pprint
import sys

input_file = sys.argv[1]

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

    update tree adding the parents to each node
    """
    for val in tree:    # walking through the keys
        if tree[val]['child'] != None:
            for child in tree[val]['child']:
                tree[child]['parent'] = val


if __name__ == "__main__":
    d = create_tree_list()
    #import IPython;IPython.embed()
    #pprint(d)

    # initialize the parent field to all nodes
    for key in d:
        d[key]['parent'] = None

    update_parents_dict(d)

    pprint(d)

    for key in d:
        # if there is no parent so the node is a base
        if d[key]['parent'] == None:
            print key