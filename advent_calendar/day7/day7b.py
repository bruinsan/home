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
    if tree[node]['child'] is None:
        # leaf
        return tree[node]['ac_sum']
    else:
		# update node weight with the children calls
        for child in tree[node]['child']:
            tree[node]['ac_sum'] += acumulated_sum(tree,child)
        return tree[node]['ac_sum']
"""
def update_tree(tree):
    for key in tree.keys():
        if not tree[key]['child'] in tree.keys():
        # new leaf
            tree[key]['child'] = None

def print_level(tree):
    # update after each level
    #print tree[base]
    print "##########"
    while tree:
        for key in tree.keys():
            if tree[key]['child'] == None :
                print tree[key]
                #print key
                tree.pop(key)
        update_tree(tree)
        print "##########"
""" 

def print_complete_node(tree, node):
    if tree[node]['child'] == None:
        print node
        return tree[node]['child']
    else:
        for child in tree[node]['child']:
            #tree[node]['ac_sum'] += acumulated_sum(tree,child)
            print child
            print_complete_node(tree, child)
        print "########"
        return tree[node]['child']
        

if __name__ == "__main__":
    d = create_tree_list()
    
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
    #pprint(d)
    
    """
    for child in d[base]['child']:
        print child
        pprint(d[child])
    """
    
    #pprint(d)
    #print_complete_node(d, 'gqmls')
    #print_level(d)
    pprint(d['gqmls'])
    for child in d['gqmls']['child']:
        print(child)
        pprint(d[child])
        
    for child in d['jfdck']['child']:
        print(child)
        pprint(d[child])
        
    for child in d['marnqj']['child']:
        print(child)
        pprint(d[child])
    
                