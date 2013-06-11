def main():
    total = 0
    for n in xrange(1000000):
        if e_util.is_palindrome(n) and e_util.is_palindrome("{0:b}".format(n)):
            total += n
    print total
    
if __name__ == '__main__':
    main()
