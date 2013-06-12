def main():
    """ 
    'acc' represents the fraction we add to 1 to calculate sqrt(2). With each iteration, we can see that
    the acc for the next iteration is simply 1 / (2 + previous_acc).
    """
    result = 0
    acc = fractions.Fraction(1, 2)
    for i in xrange(1, 1000):
        acc = 2 + acc
        acc = fractions.Fraction(acc.denominator, acc.numerator) # 1 / acc
        sqrt_2 = 1 + acc
        if len(str(sqrt_2.numerator)) > len(str(sqrt_2.denominator)):
            result += 1
    print result
        
if __name__ == '__main__':
    main()
