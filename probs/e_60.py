#!/usr/bin/python
import e_util
    
def find_longest_seq(n, ps, g, pres):
    longest = []
    for nghbr in g[n]:
        go = True
        for pre in pres:
            if nghbr not in g[pre]:
                go = False
                break
        if go:
            seq = find_longest_seq(nghbr, ps, g, pres + [n])
            if (len(seq) > len(longest) or
                    len(seq) == len(longest) and
                    sum(seq) < sum(longest)):
                longest = seq
            
    return [ps[n]] + longest
    
def main():
    n = 5
    ps = e_util.get_primes(10000)[1:] # don't need '2'
    g = {}
    for i in xrange(len(ps)):
        p_i = ps[i]
        g[i] = set()
        for j in xrange(i+1, len(ps)):
            p_j = ps[j]
            if (e_util.is_prime(int('%d%d'%(p_i,p_j))) and
                    e_util.is_prime(int('%d%d'%(p_j,p_i)))):
                g[i].add(j)
                
    longest = []
    min_sum = float('inf')
    for i in xrange(len(ps) - (n - 1)):
        seq = find_longest_seq(i, ps, g, [])
        if (len(seq) > len(longest) or
                len(seq) == len(longest) and
                sum(seq) < sum(longest)):
            longest = seq
            min_sum = sum(seq)   
    print min_sum
    
if __name__ == '__main__':
    main()
