#!/usr/bin/python
import e_util

def totient(n):
    a = [True] * n
    factors = e_util.factor(n)
    for i in range(1, len(factors) / 2 + 1):
        f = factors[i]
        j = f
        while j < n:
            a[j] = False
            j += f 
    count = 1
    for i in range(2, len(a)):
        if a[i]:
            count += 1
    return count

# TODO
def main():
    smallest = float('inf')
    result = 0
    for n in range(400399, 10**7):
        t = totient(n)
        if e_util.is_perm(str(t), str(n)):
            r = float(n) / t 
            if r < smallest:
                smallest = r 
                result = n
                print str(n) + ' ' + str(t)
    print result
 
if __name__ == '__main__':
    main()
