def sum_divisors(n):
    sum = 0
    for i in xrange(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            sum += n / i
    return sum
        
def main():
    n = 10000
    visited = []
    result = 0
    for i in xrange(n):
        if i not in visited:
            d = sum_divisors(i)
            if sum_divisors(d) == i and d != i:
                result += i
                visited.append(i)
                if d < n:
                    result += d
                    visited.append(d)
    print result
    
if __name__ == '__main__':
    main()
