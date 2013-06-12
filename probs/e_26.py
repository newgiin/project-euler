def find_max_recur(s):
    result = ""
    # do binary split
    right_limit = int(len(s) / 2)
    while right_limit > 0:
        for start in xrange(len(s) - right_limit * 2 + 1):
            substring = s[start : right_limit + start]
            if substring == s[right_limit + start : right_limit + start + len(substring)]:
                # if 's' contains substring sufficient number of times, 
                # with some leeway at head and tail
                if s.count(substring) > int(len(s) / len(substring)) - 5:
                    subresult = find_max_recur(substring)
                    if len(subresult) > 0:
                        return subresult
                    else:
                        return substring
        right_limit -= 1
    return result
    
def main():
    getcontext().prec = 2000
    max_d = 0
    max_str = ""
    start = time.time()
    for d in xrange(3, 1000):
        dec = str(Decimal(1) / Decimal(d)).split(".")[1]
        recurrer = find_max_recur(dec)
        if len(max_str) < len(recurrer):
            max_d = d
            max_str = recurrer
        
    print str(max_d)
    
if __name__ == '__main__':
    main()
