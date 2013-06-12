def find_num_rectangles(width, height):
    result = 0
    for h in xrange(1, height + 1):
        for w in xrange(1, width + 1):
            result += (height - h + 1) * (width - w + 1)
    return result

def main():
    height = 0
    closest = float('inf')
    area = 0
    recs = 0
    TARGET = 2000000
    flag = True
    
    while flag:
        flag = False
        height += 1
        width = 1
        recs = find_num_rectangles(width, height)
        while recs < TARGET:
            flag = True
            diff = math.fabs(TARGET - recs)
            if diff < closest:
                closest = diff
                area = width * height
            width += 1
            recs = find_num_rectangles(width, height)
            
    print area
            
    
if __name__ == '__main__':
    main()
