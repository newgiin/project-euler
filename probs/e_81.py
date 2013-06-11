def main():
    f = open(INPUT_DIR + "matrix.txt", "r")
    arr = [map(int, line.split(",")) for line in f]
    
    num_rows = len(arr)
    num_cols = len(arr[0])
    # update edges
    for col in xrange(1, num_cols):
        arr[0][col] += arr[0][col - 1]
    for row in xrange(1, num_rows):
        arr[row][0] += arr[row - 1][0]
        
    curr = 1
    while curr < num_rows:
        for col in xrange(curr, num_cols):
            if arr[curr][col - 1] < arr[curr - 1][col]:
                arr[curr][col] += arr[curr][col - 1]
            else:
                arr[curr][col] += arr[curr - 1][col]
        for row in xrange(curr + 1, num_rows):
            if arr[row][curr - 1] < arr[row - 1][curr]:
                arr[row][curr] += arr[row][curr - 1]
            else:
                arr[row][curr] += arr[row - 1][curr]
        curr += 1
    print arr[num_rows - 1][num_cols - 1]

if __name__ == '__main__':
    main()
