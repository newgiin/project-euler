def get_patterns(s):
    """ 
    Given a string, return a list of patterns where each pattern replaces 
    occurences of a unique character with one or more asterisks.
    """
    result = []
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
            
    for key in char_count:
        num_wilds = char_count[key]
        if len(char_count) == 1: # don't include patterns of only wildcards, e.g. "****"
            num_wilds = char_count[key] - 1
        for i in xrange(1, num_wilds + 1): # for every possible number of wildcards
            for perm in e_util.perms(key * (char_count[key] - i) + "*" * i):
                pattern = ""
                j = 0
                for c in s:
                    if c == key:
                        pattern += perm[j]
                        j += 1
                    else:
                        pattern += c
                result.append(pattern)
    return result

def main():
    mem = {}
    num_digits = 0
    FAMILY_TARGET = 8
    for prime in e_util.primes(1000000):
        prime_str = str(prime)
        if len(prime_str) > num_digits:
            mem = {}
            num_digits = len(prime_str)
        for pattern in get_patterns(prime_str):
            if pattern in mem:
                mem[pattern] += 1
                if mem[pattern] == FAMILY_TARGET:
                    print pattern + " " + prime_str
                    return
            else:
                mem[pattern] = 1
        
if __name__ == '__main__':
    main()
