def main():
    """" Same idea as e_71() """
    result = 0
    d = 12000
    left_bound = float(1) / 3
    right_bound = float(1) / 2
    for denom in xrange(4, d + 1):
        left_num = math.floor(denom * left_bound) + 1
        right_num = math.ceil(denom * right_bound) - 1
        
        for num in xrange(int(left_num), int(right_num) + 1):
            if fractions.gcd(num, denom) == 1:
                result += 1
    print result
    
if __name__ == '__main__':
    main()
