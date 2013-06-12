def get_abundants(n):
    result = []
    for i in xrange(2, n):
        if sum(e_util.get_factors(i)) > i:
            result.append(i)
    return result 

def abundant_summable(x, abunds=[]):
    if not abunds:
        abunds = get_abundants(x)
    else:
        # get subset of abunds we care about
        i = 0
        for abund_num in abunds:
            if abund_num >= x:
                break
            i += 1
        abunds = abunds[0 : i]

    abunds_set = set(abunds)
    for abund_num in abunds:
        if (x - abund_num) in abunds_set:
            return True
    return False     

def main():
    total = sum(i for i in xrange(1, 24))
    abunds = get_abundants(28124)
    for i in xrange(25, 28124):
        if not abundant_summable(i, abunds):
            total += i
    print total

if __name__ == '__main__':
    main()
