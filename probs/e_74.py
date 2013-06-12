def main():
    TARGET = 60
    result = 0
    for i in xrange(69, 1000000):
        chain = set([i])
        fact_sum = sum(map(math.factorial, map(int, str(i))))
        while fact_sum not in chain:
            chain.add(fact_sum)
            if len(chain) > TARGET:
                break            
            fact_sum = sum(map(math.factorial, map(int, str(fact_sum))))
        if len(chain) == TARGET:
            result += 1
    print result

    
if __name__ == '__main__':
    main()
