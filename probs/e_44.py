def main():
    RANGE = 10000 # terms to lookahead for matching pairs
    pentas = [n * (3 * n - 1) / 2 for n in xrange(1, 10001)]
    lookup_tbl = set(pentas)
    min_diff = sys.maxint
    for i in xrange(0, len(pentas) - 1):
        for j in xrange(i + 1, min(i + RANGE + 1, len(pentas))):
            sum = pentas[j] + pentas[i]
            diff = pentas[j] - pentas[i]
            if sum in lookup_tbl and diff in lookup_tbl:
                if diff < min_diff:
                    min_diff = diff
    print min_diff 

if __name__ == '__main__':
    main()
