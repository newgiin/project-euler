def main():
    result = 0
    for i in range (1, 10000):
        curr = i
        is_lychrel = True
        for iterations in xrange(0, 50):
            sum = curr + int((str(curr)[ : : -1]))
            if e_util.is_palindrome(str(sum)):
                is_lychrel = False
                break
            curr = sum
        if is_lychrel:
            result += 1 
    print result

if __name__ == '__main__':
    main()
