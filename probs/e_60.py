#!/usr/bin/python
import e_util

def main():
    n = 5
    ps = e_util.get_primes(10000)[1:] # don't need '2'
    g = {}
    for i in xrange(len(ps)):
        p_i = ps[i]
        g[i] = []
        for j in xrange(i+1, len(ps)):
            p_j = ps[j]
            if (e_util.is_prime(int(str(p_i) + str(p_j))) and
                    e_util.is_prime(int(str(p_j) + str(p_i)))):
                g[i].append(j)
                
                
    lowest = float('inf')
    lengths = [(1, None)]*len(ps) # i -> (length, neighbor))
    for i in reversed(xrange(len(ps))):
        max_len = 0
        max_nghbr = None
        for nghbr in g[i]:
            if lengths[nghbr][0] > max_len:
                max_len = lengths[nghbr][0]
                max_nghbr = nghbr
        lengths[i] = (1 + max_len, max_nghbr)
    print 'done calculating lengths'
    targets = []
    for i in xrange(len(lengths)):
        if lengths[i][0] >= 5:
            j = lengths[i][1]
            seq = [ps[i]]
            while j:
                seq.append(ps[j])
                j = lengths[j][1]
        targets.append(seq)
    min_sum = float('inf')
    for seq in targets:
        curr_sum = sum(seq)
        if curr_sum < min_sum:
            min_sum = curr_sum
            print seq
    print curr_sum
            
    
      
if __name__ == '__main__':
    main()
