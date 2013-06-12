def main():
    total = 0
    lkup_tbl = {}
    for i in xrange(1, 10000000):
        curr = i
        while curr != 89 and curr != 1:
            sum_digits = 0
            for c in str(curr):
                sum_digits += int(c)**2
            curr = sum_digits
            if curr in lkup_tbl:
                break
        if curr == 89 or curr in lkup_tbl and lkup_tbl[curr] == True:
            lkup_tbl[i] = True
            total += 1
        else:
            lkup_tbl[i] = False
    print total

if __name__ == '__main__':
    main()
