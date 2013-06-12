#!/usr/bin/python
import sys

def min_below(m, row, col):
    result = sys.maxint
    curr = 0
    for r in range(row, len(m)):
        curr += m[r][col]
        if curr + m[r][col-1] < result:
            result = curr + m[r][col-1]
    return result
    
def main():
    f = open('../in_files/82.in', 'r')
    m = []
    for line in f:
        m.append(map(int, line.split(',')))
    width = len(m[0])
    height = len(m)
    for col in xrange(1, width):
        m[0][col] = min_below(m, 0, col)
        for row in xrange(1, height):
            m[row][col] = \
                min([
                    m[row][col] + m[row-1][col],
                    min_below(m, row, col)
                ])
    last_col = []
    
    for row in xrange(0, height):
        last_col.append(m[row][width-1])
    print min(last_col)
    
if __name__ == '__main__':
    main()