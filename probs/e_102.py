#!/usr/bin/python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    count = 0
    f = open('../in_files/triangles.txt', 'r')

    for line in f:
        a = map(int, line.split(','))
        p1 = Point(a[0], a[1])
        p2 = Point(a[2], a[3])
        p3 = Point(a[4], a[5])
        p = Point(0, 0)
   
        # Using the Barycentric coordinate system
        det_t = (p2.y - p3.y)*(p1.x - p3.x) - (p2.x - p3.x)*(p1.y - p3.y)
        alpha = float(((p2.y - p3.y)*(p.x - p3.x) + 
            (p3.x - p2.x)*(p.y - p3.y))) / det_t
        beta = float(((p3.y - p1.y)*(p.x - p3.x) + 
            (p1.x - p3.x)*(p.y - p3.y))) / det_t
        gamma = 1 - alpha - beta 
       
        if 0 < alpha < 1 and 0 < beta < 1 and 0 < gamma < 1:
            count += 1
    print count 

if __name__ == '__main__':
    main()
