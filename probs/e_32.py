def main():
    result = set()
    for a in xrange(123, 9876):
        a_s = str(a)
        b = 0
        prod = 1 
        while len(str(prod)) <= 4:
            b += 1
            # simple string checks
            b_s = str(b)
            has_rep = False
            for c in a_s:
                if c in b_s:
                    has_rep = True 
                    break
            if has_rep:
                continue

            prod = a * b
            if e_util.is_perm(a_s + b_s + str(prod), "123456789"): 
                result.add(prod)
    print sum(result)
 
if __name__ == '__main__':
    main()
