#!/bin/python

import sys
import math

# Don't let the machines win. You are humanity's last hope...
# width = int(raw_input())  # the number of cells on the X axis
# height = int(raw_input())  # the number of cells on the Y axis

def search_right(node_line, start_col, mat):
    for neighbor_col in range(start_col+1, len(mat[node_line])):
        # check if start_col+1 is not out of range
        # check
        if start_col+1 < len(mat[node_line]):
            if mat[node_line][neighbor_col] == '0':
                return neighbor_col,node_line
    return -1, -1    # didn't find a neighbor

def search_down(node_col, start_line, mat):
    for neighbor_line in range(start_line+1, len(mat)):   # problem here when we have only one line of matrix
        # check if we have a more than 1-dimensional matrix
        if len(mat) != 1:
            if mat[neighbor_line][node_col] == '0':
                return node_col, neighbor_line
    return -1, -1    # didn't find a neighbor

def print_grid(matrix):
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            if matrix[i][j] == '0':
                right_j, right_i = search_right(i,j,matrix)
                down_j, down_i = search_down(j,i,matrix)
                print j,i, right_j, right_i, down_j, down_i

'''
mat = [['.' for _ in xrange(width)] for _ in xrange(height)]
'''
'''
for i in xrange(height):
    line = raw_input()  # width characters, each either 0 or .
    for j in xrange(width):
        if line[j] == '0':
            mat[i][j] = line[j]
'''
print_grid([['0', '0'], ['0', '.']])
# Three coordinates: a node, its right neighbor, its bottom neighbor
