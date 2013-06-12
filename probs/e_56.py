def main():
    max = 0
    for a in xrange(1, 100):
        for b in xrange(1, 100):
            prod = a**b
            digit_sum = sum([int(c) for c in str(prod)])
            if digit_sum > max:
                max = digit_sum
    print max

if __name__ == '__main__':
    main()
