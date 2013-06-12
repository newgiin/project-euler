def find_bad_cols(matrix):
    bad_cols = []
    for col in xrange(len(matrix)):
        col_list = []
        for row in xrange(len(matrix)):
            col_list.append(matrix[row][col])
        if col_list.count(0) == 0:
            bad_cols.append(col)
    return bad_cols
 
def print_matrix(matrix):
    for row in xrange(len(matrix)):
        for col in xrange(len(matrix[row])):
            print  str(matrix[row][col]) + ", ",
        print ""
        
def print_reduced_matrix(matrix, reduced):        
    for row in xrange(len(matrix)):
        for col in xrange(len(matrix)):
            if reduced[row][col] == 0:
                print  str(matrix[row][col]) + ", ",
            else:
                print  "-, ",
        print ""

def main():
    # TODO
    f = open(INPUT_DIR + "345.in", "r")
    orig_matrix = []
    matrix = []
    # populate matrices
    for line in f:
        row = []
        j = 0
        for n in line.split():
            row.append(int(n))
        orig_matrix.append(row)
        matrix.append(list(row))
    # subtract row max from every element in respective row
    for row in xrange(len(matrix)):
        row_max = max(matrix[row])
        for col in xrange(len(matrix)):
            matrix[row][col] = row_max - matrix[row][col]
    print "-----original matrix"
    print_matrix(orig_matrix)
    print "-------------"
    print_matrix(matrix)
    print "-------------"
    # check if every column has a 0, if not we have much more work to do
    bad_cols = find_bad_cols(matrix)
    if len(bad_cols) > 0:
        # for every column w/o a 0, subtract column max from every 
        # element in respective column
        for col in bad_cols:
            col_list = []
            for row in xrange(len(matrix)):
                col_list.append(matrix[row][col])
            col_min = min(col_list)
            for row in xrange(len(matrix)):
                matrix[row][col] = matrix[row][col] - col_min

        # Mark the minimum amount of rows and column such that all zeroes
        # are covered. Repeat until # of marked columns and rows == matrix width.
        marked_cols = []
        marked_rows = []
        while len(marked_cols) + len(marked_rows) != len(matrix):
            marked_cols = [x for x in xrange(0, len(matrix))]
            marked_rows = []
            print_matrix(matrix)
            for row in xrange(len(matrix)):
                zero_cols = []
                for col in xrange(len(matrix)):
                    if matrix[row][col] == 0:
                        zero_cols.append(col)
                if len(zero_cols) > 1:
                    cols_to_unmark = []
                    for zero_col in zero_cols:
                        can_unmark_col = True
                        co_col_zeroes = []
                        for row_j in xrange(len(matrix)):
                            if row_j != row and matrix[row_j][zero_col] == 0:
                                co_col_zeroes.append(row_j)
                        
                        for co_col_zero in co_col_zeroes:
                            if co_col_zero not in marked_rows:
                                can_unmark_col = False
                        
                        if can_unmark_col:
                            cols_to_unmark.append(zero_col)
                    if len(cols_to_unmark) > 1:
                        for col in cols_to_unmark:
                            if col in marked_cols:
                                marked_cols.remove(col)
                        marked_rows.append(row)
            print "-------------"
            print marked_rows
            print marked_cols            
            print_matrix(matrix)
            print "-------------"
            if len(marked_cols) + len(marked_rows) == len(matrix):
                break
            # step 4
            minimum = sys.maxint
            for row in xrange(len(matrix)):
                if row in marked_rows:
                    continue
                for col in xrange(len(matrix)):
                    if col not in marked_cols and matrix[row][col] < minimum:
                        minimum = matrix[row][col]
            for row in xrange(len(matrix)):
                if row in marked_rows:
                    continue
                for col in xrange(len(matrix)):
                        matrix[row][col] -= minimum
            for row in marked_rows:
                for col in marked_cols:
                    matrix[row][col] += minimum
        
        #print_matrix(matrix)
    else:
        print_matrix(matrix)
    
if __name__ == '__main__':
    main()
