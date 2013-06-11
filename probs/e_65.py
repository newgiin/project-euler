def totient(n):
    if n == 2:
        return 1
    result = 1
    is_even = False
    if n % 2 == 0:
        is_even = True
    arr = [True] * (n / 2 + 1)
    loop_start = 2
    step = 1
    if is_even:
        loop_start = 3
        step = 2
    for i in xrange(loop_start, len(arr), step):
        if arr[i]:
            if n % i == 0:
                for j in xrange(i + i, len(arr), i):
                    arr[j] = False
            else:
                result += 1
                
    return result * 2

def converge_e_helper(acc, curr_level, target):
    """
    Recursion terminates by either returning a 1 or a multiple of two depending on which level
    of convergence it's on.
    """
    if curr_level % 3 == 0:
        if curr_level == target:
            return acc
        else:
            return acc + fractions.Fraction(1, converge_e_helper(acc + 2, curr_level + 1, target))
    else:
        if curr_level == target:
            return 1
        else:
            return 1 + fractions.Fraction(1, converge_e_helper(acc, curr_level + 1, target))
    
def converge_e(level):
    if level <= 1:
        return fractions.Fraction(2, 1)
    return fractions.Fraction(2, 1) + fractions.Fraction(1, converge_e_helper(2, 2, level))
    
def main():
    print sum(map(int, list(str(converge_e(100).numerator))))

if __name__ == '__main__':
    main()
