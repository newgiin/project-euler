def main():
    max_sols = 0
    max_p = 0
    for p in xrange(12, 1001):
        sols = 0
        a = 1
        b = p
        while  a < b:
            d = p - a
            b = (d**2 - a**2) / float((2 * d)) 
            a += 1
            if b % 1 == 0: # sides are integral length
                sols += 1
        if sols > max_sols:
            max_sols = sols
            max_p = p
    print max_p

if __name__ == '__main__':
    main()
