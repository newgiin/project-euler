def main():
    spiral_size = 3
    curr = 1
    result = 1
    while spiral_size <= 1001:
        for i in xrange(4):
            curr += spiral_size - 1
            result += curr
        spiral_size += 2
    print result
    
if __name__ == '__main__':
    main()
