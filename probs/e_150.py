#!/usr/bin/python
import sys
from copy import deepcopy
# TODO
def make_triangle(n):
    t = 0
    m = []
    curr_sz = 0
    max_sz = 1
    row = []
    for i in xrange(1, n + 1):
        if curr_sz == max_sz:
            curr_sz = 0
            max_sz += 1
            m.append(row)
            row = []
        t = (615949*t + 797807) % 2**20
        row.append(t - 2**19)
        curr_sz += 1
    return m

def make_ex_triangle():
    return [[15], [-14,-7], [20,-13,-5],[-3,8,23,-26],[1,-4,-5,-18,5],\
        [-16,31,2,9,28,3]]
    
def main():
    #m = make_triangle(500500)
    m = make_ex_triangle()
    t = deepcopy(m)
    for col in xrange(0, len(m[len(m)-2])):
        t[len(m)-2][col] += m[len(m)-1][col] + m[len(m)-1][col+1]
    for row in reversed(xrange(len(m)-2)):
        for col in xrange(0, len(m[row])):
            t[row][col] = \
                min(t[row][col] + m[row+1][col] + m[row+1][col+1],
                    # WRONG
                    t[row][col] + t[row+1][col] + t[row+1][col+1] - m[row+2][col+1])

    result = sys.maxint
    for row in xrange(len(t)-1):
        for col in xrange(len(t[row])):
            if t[row][col] < result:
                result = t[row][col]
    print 'result: ' + str(result)
    for row in t:
        print row
    #print min(map(min, t))
    
if __name__ == '__main__':
    main()
