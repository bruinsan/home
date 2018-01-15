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

def acumulated_sum(tree,node):
    # create field acumulated sum
    """    for key in tree:
        tree[key]['ac_sum'] = int(tree[key]['weight'])

    for key in tree:
        parent = tree[key]['parent']
        if parent != None:
            tree[parent]['ac_sum'] += int(tree[key]['ac_sum'])
        else:
            print "##################################################################"
    """

    """ node is a dictionary """
    #import IPython;IPython.embed()
    #print "node = {}".format(node)
    element = tree[node]
    if element['child'] is None:
        # leaf
        return  int(element['ac_sum'])
    else:
        ac_sum = []
        for child in element['child']:
            #print "child = {} \t elem(ac_sum) = {}".format(tree[child], element['ac_sum'])
            #import ipdb; ipdb.set_trace()
            #print "{} \t {}".format(element['ac_sum'], acumulated_sum(tree, child))
            ac_sum.append(acumulated_sum(tree, child))
            #element['ac_sum'] += acumulated_sum(tree,child)
            #print "sum = {} \t ac_sum = {}".format(_sum, element['ac_sum'])
        element['ac_sum'] = sum(ac_sum)
        return sum(ac_sum)
        #print "out"
         
    """
    for key in tree:
        tree[key]['ac_sum'] = int(tree[key]['weight'])
        if tree[key]['child'] == None:
            # loop getting parents in order
            pass    
    """
    

def get_weight_difference(tree):
    for key in tree:
        if tree[key]['parent'] is None:
            for child in tree[key]['child']:
                print "child = {} \t weight = {}".format(child,tree[child]['ac_sum'])

if __name__ == "__main__":
    d = create_tree_list()
    #import IPython;IPython.embed()
    #pprint(d)

    # initialize the parent field to all nodes
    for key in d:
        d[key]['parent'] = None

    update_parents_dict(d)


    for key in d:
        # if there is no parent so the node is a base
        if d[key]['parent'] == None:
            #print "base = {} and children = {}".format(key,d[key]['child'])
            base = key

    # initialize ac_sum
    for key in d:
        d[key]['ac_sum'] = int(d[key]['weight'])

    acumulated_sum(d,base)
    pprint(d)

    #get_weight_difference(d)
