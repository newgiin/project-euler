def main():
    """" 
    Determine closest we can get to 3 / 7 for each denominator by solving for numerator 
    in 'num / denom = 3 / 7'.
    """    
    TARGET = float(3) / 7
    closest = float('infinity')
    closest_num = closest_denom = 0
    for denom in xrange(3, 1000001):
        num = int(denom * TARGET)
        diff = TARGET - (float(num) / denom)
        if diff < closest and diff != 0:
            closest = diff
            closest_num = num
            closest_denom = denom
    print closest_num, " / " , closest_denom

if __name__ == '__main__':
    main()
