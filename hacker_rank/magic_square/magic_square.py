import math
import time

def vertical_sum(matrix):
    col_sum = [0] * len(matrix)

    for line in matrix:
        col_sum[0], col_sum[1], col_sum[2] = col_sum[0]+line[0], col_sum[1]+line[1], col_sum[2]+line[2]

    return col_sum

def horizontal_sum(matrix):
    lin_sum = [0] * len(matrix)

    for index, line in enumerate(matrix):
        lin_sum[index] = sum(line)

    return lin_sum

def diagonal_sum(matrix):
    diag_sum = 0
    diag_mus = 0

    for index, line in enumerate(matrix):
        diag_sum += matrix[index][index]
        diag_mus += matrix[index][len(line)-index-1]
    return diag_sum, diag_mus

def find_ovelha_negra(col, lin, diag, gaid):
    global_min = min(min(lin), min(col))
    return lin.index(min(lin)), col.index(min(col)), global_min


def formingMagicSquare(s):
    v=vertical_sum(s); h=horizontal_sum(s); ds, sd=diagonal_sum(s)
    weight = 0

    while (v != [15, 15, 15] and h != [15, 15, 15]):
        print "v = {} and h = {}".format(v, h)
        time.sleep(3)
        x, y, small = find_ovelha_negra(v, h, ds, sd)
        s[x][y] += (15-small)
        weight += (15-small)
        v=vertical_sum(s); h=horizontal_sum(s)
    return weight


s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
s2 = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]

#print s
#print "vertical sum = {}".format(vertical_sum(s))
#print "horizontal sum = {}".format(horizontal_sum(s))
#print "diagonal sum = {}".format(diagonal_sum(s))

print formingMagicSquare(s2)
# v = h = d = 0
# while not v and h and d:
