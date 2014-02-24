def main():
    f = open("../in_files/matrix.txt", "r")
    arr = [map(int, line.split(",")) for line in f]
    
    num_rows = len(arr)
    num_cols = len(arr[0])
    # update edges
    for col in xrange(1, num_cols):
        arr[0][col] += arr[0][col - 1]
    for row in xrange(1, num_rows):
        arr[row][0] += arr[row - 1][0]
        
    for row in xrange(1, num_rows):
        for col in xrange(1, num_cols):
            arr[row][col] += min(arr[row-1][col], arr[row][col-1])
    print arr[num_rows - 1][num_cols - 1]

if __name__ == '__main__':
    main()
