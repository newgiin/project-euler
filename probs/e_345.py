#!/usr/bin/python
class Coord:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __repr__(self):
        return 'Coord(%d, %d)' % (self.row, self.col)

class MatrixState:
    def __init__(self, m):
        self.m = [list(row) for row in m]
        self.c_rows = set()
        self.c_cols = set()
        self.star_zs = [[False]*len(m) for row in m]
        self.prime_zs = [[False]*len(m) for row in m]

    def row_star(self, row):
        for col in xrange(len(self.m)):
            if self.star_zs[row][col]:
                return Coord(row, col)
        return None

    def col_star(self, col):
        for row in xrange(len(self.m)):
            if self.star_zs[row][col]:
                return Coord(row, col)
        return None

    def row_prime(self, row):
        for col in xrange(len(self.m)):
            if self.prime_zs[row][col]:
                return Coord(row, col)
        return None

    def col_prime(self, col):
        for row in xrange(len(self.m)):
            if self.prime_zs[row][col]:
                return Coord(row, col)
        return None

    def star(self, row, col):
        self.star_zs[row][col] = True

    def unstar(self, row, col):
        self.star_zs[row][col] = False

    def prime(self, row, col):
        self.prime_zs[row][col] = True

    def is_star(self, row, col):
        return self.star_zs[row][col]

    def is_prime(self, row, col):
        return self.prime_zs[row][col]

    def clear_primes(self):
        self.prime_zs = [[False]*len(self.m) for row in self.m]

    def cover_col(self, col):
        self.c_cols.add(col)

    def cover_row(self, row):
        self.c_rows.add(row)

    def uncover_col(self, col):
        if col in self.c_cols:
            self.c_cols.remove(col)

    def uncover_row(self, row):
        if row in c_rows:
            self.c_rows.remove(row)
    
    def clear_lines(self):
        self.c_rows = set()
        self.c_cols = set()

    def is_row_covered(self, row):
        return row in self.c_rows

    def is_col_covered(self, col):
        return col in self.c_cols

    def is_covered(self, row, col):
        return self.is_row_covered(row) or self.is_col_covered(col)

    def __repr__(self):
        s = '/,'
        s += ','.join(['x' if self.is_col_covered(col) else '/' 
                            for col in xrange(len(self.m))]) + '\n'
        for row in xrange(len(self.m)):
            s += 'x,' if self.is_row_covered(row) else '/,'
            costs = []
            for col in xrange(len(self.m)):
                exp = ''
                if self.is_star(row, col):
                    exp += '*'
                if self.is_prime(row, col):
                    exp += "'"
                costs.append(str(self.m[row][col]) + exp)
            s += ','.join(costs) + '\n'
        return s

def row_reduce(m):
    for row in m:
        c = min(row)
        for col in xrange(len(m)):
            row[col] -= c
            
def step_2(ms):
    starred_cols = set()
    for row in xrange(len(ms.m)):
        for col in xrange(len(ms.m)):
            if ms.m[row][col] == 0 and col not in starred_cols:
                ms.star(row, col)
                starred_cols.add(col)
                break
    step_3(ms)

def step_3(ms):
    c_count = 0
    for col in xrange(len(ms.m)):
        if ms.col_star(col) is not None:
            ms.cover_col(col)
            c_count += 1
    if c_count == len(ms.m):
        return
    step_4(ms)

def step_4(ms):
    restart = True
    while restart:
        restart = False
        min_uncovered = float('inf')
        for row in xrange(len(ms.m)):
            for col in xrange(len(ms.m)):
                if not ms.is_covered(row, col):
                    if ms.m[row][col] == 0:
                        ms.prime(row, col)
                        star = ms.row_star(row)
                        if star is None:
                            step_5(ms, Coord(row, col))
                            return
                        else:
                            ms.cover_row(row)
                            ms.uncover_col(star.col)
                            restart = True
                            break
                    elif ms.m[row][col] < min_uncovered:
                         min_uncovered = ms.m[row][col]
            if restart:
                break
    step_6(ms, min_uncovered)

def step_5(ms, z_prime):
    z_star = ms.col_star(z_prime.col)
    ms.star(z_prime.row, z_prime.col)

    while z_star is not None:
        ms.unstar(z_star.row, z_star.col)
        z_prime = ms.row_prime(z_star.row)
        z_star = ms.col_star(z_prime.col)

        ms.star(z_prime.row, z_prime.col)

    ms.star(z_prime.row, z_prime.col)
    ms.clear_primes()
    ms.clear_lines()

    step_3(ms)

def step_6(ms, min_uncovered):
    for row in xrange(len(ms.m)):
        if ms.is_row_covered(row):
            for col in xrange(len(ms.m)):
                ms.m[row][col] += min_uncovered
    for col in xrange(len(ms.m)):
        if not ms.is_col_covered(col):
            for row in xrange(len(ms.m)):
                ms.m[row][col] -= min_uncovered
    step_4(ms)

def get_solution(ms):
    result = []
    for row in xrange(len(ms.m)):
        star = ms.row_star(row)
        if star is None:
            raise Exception('Matrix is not done, missing star at row ' +
                str(row))
        result.append(star)
    return result

# Implementation of the 'Hungarian' algorithm, described here: 
# http://csclab.murraystate.edu/bob.pilgrim/445/munkres.html
def hungarian(og_m, find_max=False):
    ms = None
    if find_max:
        ms = MatrixState([[-1 * col for col in row] for row in og_m])
    else:
        ms = MatrixState(og_m)
    row_reduce(ms.m)
    step_2(ms)
    return get_solution(ms)

def main():
    m = [
        [7,53,183,439,863,497,383,563,79,973,287,63,343,169,583],
        [627,343,773,959,943,767,473,103,699,303,957,703,583,639,913],
        [447,283,463,29,23,487,463,993,119,883,327,493,423,159,743],
        [217,623,3,399,853,407,103,983,89,463,290,516,212,462,350],
        [960,376,682,962,300,780,486,502,912,800,250,346,172,812,350],
        [870,456,192,162,593,473,915,45,989,873,823,965,425,329,803],
        [973,965,905,919,133,673,665,235,509,613,673,815,165,992,326],
        [322,148,972,962,286,255,941,541,265,323,925,281,601,95,973],
        [445,721,11,525,473,65,511,164,138,672,18,428,154,448,848],
        [414,456,310,312,798,104,566,520,302,248,694,976,430,392,198],
        [184,829,373,181,631,101,969,613,840,740,778,458,284,760,390],
        [821,461,843,513,17,901,711,993,293,157,274,94,192,156,574],
        [34,124,4,878,450,476,712,914,838,669,875,299,823,329,699],
        [815,559,813,459,522,788,168,586,966,232,308,833,251,631,107],
        [813,883,451,509,615,77,281,613,459,205,380,274,302,35,805]
    ]

    cost = 0
    for coord in hungarian(m, find_max=True):
        cost += m[coord.row][coord.col]
    print cost

if __name__ == '__main__':
    main()
