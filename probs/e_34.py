def main():
    for i in xrange(3, 99999):
        total = sum(e_util.factorial(int(c)) for c in str(i))
        if total == i:
            print i

# Returns list of abundant numbers up to n 
if __name__ == '__main__':
    main()
