#!/usr/bin/python
import sys

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
        row.append([t - 2**19])
        curr_sz += 1
    return m

def make_ex_triangle():
    return [[[15]], [[-14],[-7]], [[20],[-13],[-5]],[[-3],[8],[23],[-26]],[[1],[-4],[-5],[-18],[5]],\
        [[-16],[31],[2],[9],[28],[3]]]
    
def main():
    m = make_triangle(500500)
    #m = make_ex_triangle()
    t = []
    for row in m:
        t.append([0]*len(row))
    for col in xrange(len(m[len(m)-2])):
        m[len(m)-2][col].append(m[len(m)-2][col][0] + \
            m[len(m)-1][col][0] + m[len(m)-1][col+1][0])
        t[len(m)-2][col] = min(m[len(m)-2][col][1:])
    for row in reversed(xrange(len(m)-2)):
        for col in xrange(0, len(m[row])):
            m[row][col].append(m[row][col][0] + \
                m[row+1][col][0] + m[row+1][col+1][0])
            for level in xrange(1, len(m[row+1][col])):
                m[row][col].append(m[row][col][0] + \
                    m[row+1][col][level] + m[row+1][col+1][level] - \
                    m[row+2][col+1][level-1])  
            t[row][col] = min(m[row][col][1:])

    result = sys.maxint
    for row in xrange(len(t)-1):
        for col in xrange(len(t[row])):
            if t[row][col] < result:
                result = t[row][col]
    print result
    
if __name__ == '__main__':
    main()
