import math
import random
import time
import fractions
from decimal import *
import sys
import e_util

INPUT_DIR = "in_files/"
         
def e_16():
    print sum([int(c) for c in str(2**1000)])

def e_13():
    f = open("e_13.in", "r")
    line = f.readline()
    # 2d array holding last 10 digits per line
    # must do it this way since Python has no easy way to make 2d arrays
    arr = [[], [], [], [], [], [], [], [], [], []]
    while line:
        arr[0].append(int(line[49]))
        arr[1].append(int(line[48]))
        arr[2].append(int(line[47]))
        arr[3].append(int(line[46]))
        arr[4].append(int(line[45]))
        arr[5].append(int(line[44]))
        arr[6].append(int(line[43]))
        arr[7].append(int(line[42]))
        arr[8].append(int(line[41]))
        arr[9].append(int(line[40]))
        line = f.readline()
    
    carry = 0
    result = "" 
    for place in xrange(10):
        sum = carry
        for digit in arr[place]:
            sum += digit
        ones = sum % 10
        result = str(ones) + result
        carry = int((sum - ones) / 10)
    print result

def e_14():
    occurence = 0
    maxlength = 0
    memoi = [0] * 1000000
    for curr in xrange(1000000):
        length = 1
        n = curr
        if memoi[n] != 0:
            length = memoi[n]
        else:
            while n > 1:
                if n < 1000000 and memoi[n] != 0:
                    length += memoi[n]
                    break
                if n % 2 == 0:
                    n = int(n / 2)
                else:
                    n = 3 * n + 1
                length += 1
        memoi[curr] = length
        if length > maxlength:
            maxlength = length
            occurence = curr
    print(str(occurence) + " | " + str(maxlength))    

def e_17():
    print sum([int(x) for x in str(math.e_util.factorial(100))])

def e_18():
    arr = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 04, 82, 47, 65],
    [19, 01, 23, 75, 03, 34],
    [88, 02, 77, 73, 07, 63, 67],
    [99, 65, 04, 28, 06, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]

    for row in xrange(1, len(arr)):
        arr[row][0] += arr[row - 1][0]
        for i in xrange(1, len(arr[row]) - 1):
            if arr[row - 1][i - 1] > arr[row - 1][i]:
                arr[row][i] += arr[row - 1][i - 1]
            else:
                arr[row][i] += arr[row - 1][i]
        arr[row][len(arr[row]) - 1] += arr[row - 1][len(arr[row - 1]) - 1]
    print max(arr[len(arr) - 1])      
    
def e_19():
    SUN = 1; MON = 2;TUE = 3;WED  = 4; THU = 5; FRI = 6; SAT = 7; 
    year = 1901
    month = 1
    day = TUE

    sum = 0
    while year < 2001:
        month = 1
        while month <= 12:
            if month == 9 or month == 4 or month == 6 or month == 11:
                day += 1
                if day > SAT:
                    day = SUN
            elif month == 2:
                day -= 1
                if day < SUN:
                    day = SAT
            else:
                if day == SAT:
                    day = MON
                elif day == FRI:
                    day = SUN
                else:
                    day += 2
            if day == SUN:
                sum += 1
            month += 1
        year += 1
    
    print sum
    
def sum_divisors(n):
    sum = 0
    for i in xrange(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            sum += n / i
    return sum
        
def e_21():
    n = 10000
    visited = []
    result = 0
    for i in xrange(n):
        if i not in visited:
            d = sum_divisors(i)
            if sum_divisors(d) == i and d != i:
                result += i
                visited.append(i)
                if d < n:
                    result += d
                    visited.append(d)
    print result
    
def e_25():
    first = 0
    sec = 1
    n = 1
    while len(str(sec)) < 1000:
        temp = first
        first = sec
        sec += temp
        n += 1
    print n
    
def find_max_recur(s):
    result = ""
    # do binary split
    right_limit = int(len(s) / 2)
    while right_limit > 0:
        for start in xrange(len(s) - right_limit * 2 + 1):
            substring = s[start : right_limit + start]
            if substring == s[right_limit + start : right_limit + start + len(substring)]:
                # if 's' contains substring sufficient number of times, 
                # with some leeway at head and tail
                if s.count(substring) > int(len(s) / len(substring)) - 5:
                    subresult = find_max_recur(substring)
                    if len(subresult) > 0:
                        return subresult
                    else:
                        return substring
        right_limit -= 1
    return result
    
def e_26():
    getcontext().prec = 2000
    max_d = 0
    max_str = ""
    start = time.time()
    for d in xrange(3, 1000):
        dec = str(Decimal(1) / Decimal(d)).split(".")[1]
        recurrer = find_max_recur(dec)
        if len(max_str) < len(recurrer):
            max_d = d
            max_str = recurrer
        
    print str(max_d)
    
def e_27():
    max_primes = 0
    max_a = 0
    max_b = 0
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            n = 0
            while e_util.is_prime(n**2 + a * n + b):
                n += 1
            if n > max_primes:
                max_primes = n
                max_a = a
                max_b = b
    print max_a * max_b
    
def e_28():
    spiral_size = 3
    curr = 1
    result = 1
    while spiral_size <= 1001:
        for i in xrange(4):
            curr += spiral_size - 1
            result += curr
        spiral_size += 2
    print result
    
def e_31():
    denoms = [1, 2, 5, 10, 20, 50, 100, 200]

    def combo_recurr(n, max_denom):
        if max_denom == 1:
            return 1
        remainder = n - max_denom
        if remainder == 0:
            return 1 + combo_recurr(n, denoms[denoms.index(max_denom) - 1])
        if remainder < 0:
            return combo_recurr(n, denoms[denoms.index(max_denom) - 1])
        return combo_recurr(remainder, max_denom) + combo_recurr(n, denoms[denoms.index(max_denom) - 1])
    
    def combos(n):
        return combo_recurr(n, 200)
    
    
    print combos(200)

def e_35():
    def is_circular(n):
        n = list(str(n))
        for i in xrange(len(n) - 1):
            last = n[len(n) - 1]
            for c in xrange(len(n) - 2, -1, -1):
                n[c + 1] = n[c]
            n[0] = last
            if e_util.is_prime(int("".join(n))) == False:
                return False
        return True

    primes = e_util.find_primes(1000000)

    # count number of circular primes
    count = 0
    for i in xrange(len(primes)):
        if is_circular(primes[i]):
            count += 1
    print count
    
def e_36():
    total = 0
    for n in xrange(1000000):
        if e_util.is_palindrome(n) and e_util.is_palindrome("{0:b}".format(n)):
            total += n
    print total
    
def e_37():
    primes = e_util.find_primes(900000)
    result = []
    for i in xrange(4, len(primes)):
        s = str(primes[i])
        # remove from right to left
        truncable = True
        while len(s) > 1:
            s = s[0 : len(s) - 1]
            if int(s) not in primes:
                truncable = False
                break
        if truncable:
            # from left to right
            s = str(primes[i])
            while len(s) > 1:
                s = s[1 : len(s)]
                if int(s) not in primes:
                    truncable = False
                    break
        if truncable:
            result.append(primes[i])
    print sum(result)
    
def e_40():
    d_end = 0
    d = 1
    p = 0
    result = 1
    while d <= 1000000:
        d_beg = d_end + 1
        r = 10**p
        len_r = len(str(r))
        i_beg = 10**p
        i_end = 10**(p + 1) - 1
        d_end = d_beg + len_r * 9 * r - 1
        while d >= d_beg and d <= d_end:
            d_cell = (d - d_beg) / len_r
            num = i_beg + d_cell     
            digit = str(num)[(d - d_beg) % len_r]
            result *= int(digit)
            d *= 10
        p += 1
    print result
        
def e_41():
    def is_pandigital(x):
        x = str(x)
        n = len(x)
        digits = []
        for i in xrange(1, n + 1):
            digits.append(str(i))
        for i in xrange(len(digits)):
            if digits[i] not in x:
                return False
        return True
    
    primes = e_util.find_primes(99999999)
    for i in reversed(primes):
        if is_pandigital(i):
            print i
            break
        
def e_67():
    f = open("triangle.txt", "r")
    arr = []
    for line in f:
        row = [int(num) for num in line.split()]
        arr.append(row)
    
    for row in xrange(1, len(arr)):
        arr[row][0] += arr[row - 1][0]
        for i in xrange(1, len(arr[row]) - 1):
            if arr[row - 1][i - 1] > arr[row - 1][i]:
                arr[row][i] += arr[row - 1][i - 1]
            else:
                arr[row][i] += arr[row - 1][i]
        arr[row][len(arr[row]) - 1] += arr[row - 1][len(arr[row - 1]) - 1]
    print max(arr[len(arr) - 1])
    
def e_49():
    primes = e_util.find_primes(10000)
    for i in xrange(0, len(primes) - 3):
        for j in xrange(i + 1, len(primes) - 2): 
            if e_util.is_perm(str(primes[i]), str(primes[j])):
                diff = primes[j] - primes[i]
                try:
                    partner = primes.index(primes[j] + diff)
                except ValueError:
                    partner = -1
                if partner != -1 and e_util.is_perm(str(primes[j]), str(primes[partner])):
                    print primes[i], primes[j], primes[partner]

def e_24():
    perms = e_util.get_perms("0123456789")
    print perms[999999]

def e_30():
    result = []
    for i in xrange(2, 9999999):
        word = str(i)
        acc = 0
        for c in word:
            acc += int(c)**5
        if acc == i:
            result.append(i) 
    print sum(result)

def e_29():
    all = set(i**j for i in xrange(2, 101) for j in xrange(2, 101)) 
    print len(all)

def e_34():
    for i in xrange(3, 99999):
        total = sum(e_util.factorial(int(c)) for c in str(i))
        if total == i:
            print i

# Returns list of abundant numbers up to n 
def get_abundants(n):
    result = []
    for i in xrange(2, n):
        if sum(e_util.get_factors(i)) > i:
            result.append(i)
    return result 

def abundant_summable(x, abunds=[]):
    if not abunds:
        abunds = get_abundants(x)
    else:
        # get subset of abunds we care about
        i = 0
        for abund_num in abunds:
            if abund_num >= x:
                break
            i += 1
        abunds = abunds[0 : i]

    abunds_set = set(abunds)
    for abund_num in abunds:
        if (x - abund_num) in abunds_set:
            return True
    return False     

def e_23():
    total = sum(i for i in xrange(1, 24))
    abunds = get_abundants(28124)
    for i in xrange(25, 28124):
        if not abundant_summable(i, abunds):
            total += i
    print total

def is_penta(x):
    sol = e_util.solve_quad(3, -1,  -2 * x)[1]
    if sol != None and sol > 0 and sol % 1 == 0:
        return True
    return False

def is_hexa(x):
    sol = e_util.solve_quad(2, -1,  -x)[1]
    if sol != None and sol > 0 and sol % 1 == 0:
        return True
    return False
    
def e_45():
    n = 286
    tri = n * (n + 1) / 2  
    while not (is_penta(tri) and is_hexa(tri)):
       n += 1
       tri = n * (n + 1) / 2
    print tri 

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
            for perm in e_util.get_perms(key * (char_count[key] - i) + "*" * i):
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

def e_51():
    mem = {}
    num_digits = 0
    FAMILY_TARGET = 8
    for prime in e_util.find_primes(1000000):
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
        
def e_52():
    i = 10
    while True:
        flag = True
        m = 2
        for m in xrange(2, 7):
           if not e_util.is_perm(str(i), str(i * m)):
                flag = False
                break
        if flag:
            print i
            break 
        i += 1
        
def e_39():
    max_sols = 0
    max_p = 0
    for p in xrange(12, 1001):
        sols = 0
        a = 1
        b = p
        while  a < b:
            d = p - a
            b = (d**2 - a**2) / float((2 * d)) 
            a += 1
            if b % 1 == 0: # sides are integral length
                sols += 1
        if sols > max_sols:
            max_sols = sols
            max_p = p
    print max_p

def e_33():
    for num in xrange(11, 99):
        if str(num)[1] == "0":
            continue
        for den in xrange(num + 1, 99):
            num_s = str(num)
            den_s = str(den)
            if den_s[1] == "0":
                continue
            for n_i in xrange(0, len(num_s)):
                for d_i in xrange(0, len(den_s)):
                    if num_s[n_i] == den_s[d_i]:
                        red_num = num_s[0 : n_i] + num_s[n_i + 1 : len(num_s)]
                        red_den = den_s[0 : d_i] + den_s[d_i + 1 : len(den_s)]
                        if float(int(red_num)) / int(red_den) == float(num) / den:
                            print num_s + " / " + den_s
             
def e_32():
    result = set()
    for a in xrange(123, 9876):
        a_s = str(a)
        b = 0
        prod = 1 
        while len(str(prod)) <= 4:
            b += 1
            # simple string checks
            b_s = str(b)
            has_rep = False
            for c in a_s:
                if c in b_s:
                    has_rep = True 
                    break
            if has_rep:
                continue

            prod = a * b
            if e_util.is_perm(a_s + b_s + str(prod), "123456789"): 
                result.add(prod)
    print sum(result)
 
def e_53():
    total = 0
    for n in xrange(23, 101):
        for r in xrange(2, n):
            combos = e_util.factorial(n) / (e_util.factorial(r) * e_util.factorial(n - r))
            if combos > 1000000:
                total += 1
    print total 

def e_56():
    max = 0
    for a in xrange(1, 100):
        for b in xrange(1, 100):
            prod = a**b
            digit_sum = sum([int(c) for c in str(prod)])
            if digit_sum > max:
                max = digit_sum
    print max

def e_38():
    max = 0
    for i in xrange(2, 49877):
        ct_prd = ""
        m = 1
        while len(ct_prd) < 9:
            ct_prd += str(i * m)
            m += 1
        if e_util.is_perm(ct_prd, "123456789") and int(ct_prd) > max:
            max = int(ct_prd)
    print max    

def e_55():
    result = 0
    for i in range (1, 10000):
        curr = i
        is_lychrel = True
        for iterations in xrange(0, 50):
            sum = curr + int((str(curr)[ : : -1]))
            if e_util.is_palindrome(str(sum)):
                is_lychrel = False
                break
            curr = sum
        if is_lychrel:
            result += 1 
    print result

def e_50():
    max = 0
    max_sum = 0
    primes = e_util.find_primes(5000)
    prime_set = set(e_util.find_primes(1000000))
    for i in xrange(0, len(primes)):
        sum = primes[i]
        seq_len = 1
        for j in xrange(i + 1, len(primes)):
            sum += primes[j]
            if sum > 1000000:
                sum -= primes[j]
                break
            if sum in prime_set:
                seq_len = j - i + 1
        if seq_len > max:
            max = seq_len
            max_sum = sum
    print max_sum

def is_triangle(x):
    sol = e_util.solve_quad(1, 1, -2 * x)[1]
    if sol != None and sol > 0 and sol % 1 == 0:
        return True
    return False
    
def is_triangle_word(word):
    total = 0
    for c in word:
        total += ord(c) - 64
    return is_triangle(total)

def e_42():
    result = 0
    f = open(INPUT_DIR + "words.txt", "r")
    line = f.readline()
    words = line.split(",")
    for w in words:
        w = w.replace('"', '')
        if is_triangle_word(w):
            result += 1
    print result 

def is_sumPrimeAndDouble(x, primes=e_util.find_primes(1000000)):
    p = primes[0]
    i = 0
    while p < x: 
        sum = 0
        base = 1
        while sum < x:
            sum = p + 2 * base**2
            base += 1
        if sum == x:
            return True   
        i += 1
        p = primes[i]
    return False

def e_46():
    i = 9
    primes = e_util.find_primes(10000)
    while True:
        if not e_util.is_prime(i) and not is_sumPrimeAndDouble(i, primes):
            print i
            return  
        i += 2
    
def e_47():
    i = 1000
    T = 4 # find first T consecutive integers with T distinct factors
    i_processed = False # optimization to avoid getting prime factors twice
    while True:
        if i_processed or len(e_util.get_prime_factors(i)) >= T:
            seq_len = 1
            for j in reversed(xrange(1, T)): 
                if len(e_util.get_prime_factors(i + j)) >= T:
                    seq_len += 1
                else:
                    break
            if seq_len == T:
                print [i + k for k in xrange(0, T)]
                return
            i += T - seq_len + 1 # skip ahead 
            if seq_len > 1:
                i_processed = True
            else:
                i_processed = False
        else:
            i += 1 
            i_processed = False

def e_43():
    sum = 0
    primes = e_util.find_primes(18)
    for p in e_util.get_perms("0123456789"):
        flag = True
        for i in xrange(1, 8):
            if int(p[i : i + 3]) % primes[i - 1] != 0:
                flag = False
                break    
        if flag:
            sum += int(p)
    print sum

def e_44():
    RANGE = 10000 # terms to lookahead for matching pairs
    pentas = [n * (3 * n - 1) / 2 for n in xrange(1, 10001)]
    lookup_tbl = set(pentas)
    min_diff = sys.maxint
    for i in xrange(0, len(pentas) - 1):
        for j in xrange(i + 1, min(i + RANGE + 1, len(pentas))):
            sum = pentas[j] + pentas[i]
            diff = pentas[j] - pentas[i]
            if sum in lookup_tbl and diff in lookup_tbl:
                if diff < min_diff:
                    min_diff = diff
    print min_diff 

def e_79():
    f = open("keylog.txt", "r")
    visited = {}
    for line in f:
        line = line.strip() # remove newline
        for i in xrange(0, len(line)):
            c = line[i]
            if c not in visited:
                visited[c] = []
            for k in line[i + 1 : ]:
                if k not in visited[c]:
                    visited[c].append(k)    
    code = ""
    while len(visited) > 0:
        for c in visited: 
            if len(visited[c]) == len(visited) - 1:
                code += c
                del visited[c]
                break
    print code

def e_63():
    digits = 1
    count = 1 # we know 1^x will always be 1 digit, so just count it here
    while True:
        i = 2
        pwrd = str(i**digits)
        while len(pwrd) <= digits:
            if len(str(pwrd)) == digits:
                count += 1
            i += 1
            pwrd = str(i**digits)
        if i == 10 and len(str(9**digits)) < digits:
            break
        digits += 1
    print count

def has_english(filename, threshold=9):
    file = open(filename, "r")
    vocab = set(['the', 'The', 'and', 'you', 'there', 'have', 'that', 'from'])
    found = 0
    for line in file:
        for word in line.split():
            if word in vocab:
                found += 1
    file.close()
    if found >= threshold:
        return True
    return False

def decrypt(cipher, key, outname=None):
    f = open(cipher, "r")
    outfile = None
    if not outname:
        outfile = open(f.name + ".decrypted", "w")
    else:
        outfile = open(outname, "w")
    i = 0
    for line in f:
        codes = line.split(",")
        for code in codes:
            dcrptd_byte = int(code)^ord(key[i])
            outfile.write(chr(dcrptd_byte))
            i += 1
            if i == len(key):
                i = 0
    outfile.close()
    f.close()

def e_59():
    cipher = INPUT_DIR + "cipher1.txt"
    outname = "decrypted.out"
    all_letters = ""
    done = False
    key_len = 3

    for c in xrange(97, 97 + 26):
        for _ in xrange(0, key_len): # include keys with repeating characters, e.g. 'aaa'
            all_letters += chr(c)
    for combo in e_util.get_combos(all_letters, key_len):
        for key in e_util.get_perms(combo):
            decrypt(cipher, key, outname)
            if has_english(outname):
                print key
                return
                
    print "FAILED"

class _RepeatValsResult:
    """ 
    Container for find_repeat_vals result 
    """
    def __init__(self):
        self.is_four_kind = self.is_three_kind = self.is_two_pair = self.is_pair = False
        # value of a {3,4}-of-a-kind, pair vals
        self.val = self.pair1_val = self.pair2_val = None
        self.remainder = []
   
def find_repeat_vals(hand):
    """ Determines if a hand contains pairs, or a {3,4}-of-a-kind """ 
    vals = {} # Map: val -> # of cards with value of 'val' in hand
    result = _RepeatValsResult()

    for card in hand:
        if card.val in vals:
            vals[card.val] += 1
        else:
            vals[card.val] = 1

    for val in vals:
        if vals[val] == 4:
            result.is_four_kind = True
            result.val = val
        elif vals[val] == 3:
            result.is_three_kind = True
            result.val = val
        elif vals[val] == 2:
            if result.pair1_val is None:
                result.is_pair = True
                result.pair1_val = val
            else:
                result.is_two_pair = True
                result.pair2_val = val
        else:
            result.remainder.append(val)
    return result

class _FindStr8Result:
    """ 
    Container for find_str8() result. Also stores high - card since find_str8() sorts the 
    hand allowing easy access to highcard.
    """    
    def __init__(self):
        self.high_card = None
        self.has_str8 = False
            
def find_str8(hand):
    result = _FindStr8Result()
    srted = [card.val for card in hand]
    srted.sort()
    result.high_card = srted[-1]
    for i in xrange(0, len(srted) - 1):
        if srted[i] + 1 !=  srted[i + 1]:
            return result
    result.has_str8 = True
    return result

def has_flush(hand):
    suit = hand[0].suit
    for i in xrange(1, len(hand)):
        if hand[i].suit != suit:
            return False
    return True  

class _Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        
    def __init__(self, s):
        try:
            self.val = int(s[0])
        except ValueError:
            if s[0] == "T":
                self.val = 10
            elif s[0] == "J":
                self.val = 11
            elif s[0] == "Q":
                self.val = 12
            elif s[0] == "K":
                self.val = 13
            else:
                self.val = 14
        self.suit = s[1]
        
    def __repr__(self):
        return self.suit + " - " + str(self.val)
        
class _HandRank:
    HIGH_CARD, PAIR, TWO_PAIR, THREE_KIND, STR8, FLUSH\
    , FULL_HOUSE, FOUR_KIND, STR8_FLUSH = xrange(9)

def print_rank(rank):
    ranks = ["HIGH_CARD", "PAIR", "TWO_PAIR", "THREE_KIND", "STR8", "FLUSH"\
    , "FULL_HOUSE", "FOUR_KIND", "STR8_FLUSH"]
    return ranks[rank]
       
def rank_hand(hand_info):
    rank = _HandRank.HIGH_CARD
    
    rep_result = hand_info.rep_result
    str8_result =  hand_info.str8_result
    is_flush =  hand_info.is_flush   
    
    if rep_result.is_two_pair:
        rank = _HandRank.TWO_PAIR
    elif rep_result.is_pair:
        rank = _HandRank.PAIR
        if rep_result.is_three_kind:
            rank = _HandRank.FULL_HOUSE
    elif rep_result.is_three_kind:
        rank = _HandRank.THREE_KIND
    elif rep_result.is_four_kind:
        rank = _HandRank.FOUR_KIND
    elif str8_result.has_str8:
        rank = _HandRank.STR8
        if is_flush:
            rank = _HandRank.STR8_FLUSH
    elif is_flush:
        rank = _HandRank.FLUSH
        
    return rank    

class _HandInfo:
    """
    Wrapper containing all the information you need about a poker hand.
    """
    def __init__(self, hand):
        self.rep_result = find_repeat_vals(hand)
        self.str8_result = find_str8(hand)
        self.is_flush = has_flush(hand)
        self.rank = rank_hand(self)
            
def is_winning_hand(h1_info, h2_info):
    """ Returns True iff hand 1 is the winning hand """    
    if h1_info.rank != h2_info.rank:
        return h1_info.rank > h2_info.rank
    # resolve tie
    if h1_info.rank == _HandRank.PAIR or h1_info.rank == _HandRank.TWO_PAIR:
        h1_pair_val = max(h1_info.rep_result.pair1_val, h1_info.rep_result.pair2_val)
        h2_pair_val = max(h2_info.rep_result.pair1_val, h2_info.rep_result.pair2_val)
        if h1_pair_val > h2_pair_val:
            return True
        elif h1_pair_val < h2_pair_val:
            return False
        else:
            return max(h1_info.rep_result.remainder) > max(h2_info.rep_result.remainder)
    elif (h1_info.rank == _HandRank.THREE_KIND or h1_info.rank == _HandRank.FOUR_KIND or\
            h1_info.rank == _HandRank.FULL_HOUSE):
        if h1_info.rep_result.val > h2_info.rep_result.val:
            return True
        elif h1_info.rep_result.val < h2_info.rep_result.val:
            return False
    if h1_info.str8_result.high_card == h2_info.str8_result.high_card:
        raise Exception("NO CLEAR WINNER")
        
    return h1_info.str8_result.high_card > h2_info.str8_result.high_card

def e_54():
    result = 0
    f = open(INPUT_DIR + "poker.txt", "r")
    #f = open(INPUT_DIR + "my.test", "r")
    for line in f:
        cards = line.split()
        p1_hand = []
        p2_hand = []
        # populate hands
        for i in xrange(0, 5):
            p1_hand.append(_Card(cards[i]))
        for i in xrange(5, 10):
            p2_hand.append(_Card(cards[i]))
        
        hand_info_1 = _HandInfo(p1_hand)
        hand_info_2 = _HandInfo(p2_hand)
        # determine winner
        if is_winning_hand(hand_info_1, hand_info_2):
            result += 1
    print result

def e_57():
    """ 
    'acc' represents the fraction we add to 1 to calculate sqrt(2). With each iteration, we can see that
    the acc for the next iteration is simply 1 / (2 + previous_acc).
    """
    result = 0
    acc = fractions.Fraction(1, 2)
    for i in xrange(1, 1000):
        acc = 2 + acc
        acc = fractions.Fraction(acc.denominator, acc.numerator) # 1 / acc
        sqrt_2 = 1 + acc
        if len(str(sqrt_2.numerator)) > len(str(sqrt_2.denominator)):
            result += 1
    print result
        
def e_58():
    skip = 1
    p = 0
    diags = 1
    i = 1
    # create spiral
    while True:
        for _ in xrange(4):
            i += skip + 1
            if e_util.is_prime(i):
                p += 1
        diags += 4
        if float(p) / diags < .10:
            print skip + 2
            return
        skip += 2

def is_hepta(x):
    sol = e_util.solve_quad(5, -3, -2 * x)[1]
    if sol != None and sol > 0 and sol % 1 == 0:
        return True
    return False    

def is_octa(x):
    sol = e_util.solve_quad(3, -2,  -x)[1]
    if sol != None and sol > 0 and sol % 1 == 0:
        return True
    return False

def is_square(x):
    return math.sqrt(x) % 1 == 0
    
def check_fam(x):
    """
    Returns 0 if x is a triangle number, 1 if square, ... , 5 if octagonal.
    """
    func_arr = [is_triangle, is_square, is_penta, is_hexa, is_hepta, is_octa]
    for i in xrange(len(func_arr)):
        if func_arr[i](x):
            return i
    return None

def find_cyclic_chain(fam_map, x, fams_found):
    result = []
    # base case when x does not belong to a family or if we've already seen
    # this family.
    if x not in fam_map:
        return result
    if fams_found[fam_map[x]]:
        # all hexagonal numbers are also triangular
        if fam_map[x] == 0 and not fams_found[3]:
            fams_found[3] = True 
        else:
            return result
    result.append(x)
    fams_found[fam_map[x]] = True
    longest = []
    start = (x % 100) * 100
    # return longest possible chain
    # e.g. for numbers between 1800 to 1899
    for i in xrange(start, start + 100):
        chain = find_cyclic_chain(fam_map, i, list(fams_found))
        if len(chain) > len(longest):
            longest = chain
    return result + longest

def e_61():
    fam_map = {}
    for i in xrange(1000, 10000):
        fam = check_fam(i)
        if fam is not None:
            fam_map[i] = fam
    for i in fam_map:
        chain = find_cyclic_chain(fam_map, i, [False] * 6)
        if len(chain) == 6 and chain[len(chain) - 1] % 100 \
                == i / 100:
            print chain
            print sum(chain)
            return
        
def e_62():
    P = 5
    i = 5
    cubed = i**3
    num_digits = len(str(cubed))
    cubes = []

    while True:
        # cache cubes with num_digits
        while len(str(cubed)) == num_digits:
            cubes.append(cubed)
            i += 1
            cubed = i**3
        
        for j in xrange(len(cubes) - P + 1):
            cube_perms = 1
            for k in xrange(j + 1, len(cubes)):
                if e_util.is_perm(str(cubes[j]), str(cubes[k])):
                    cube_perms += 1
            if cube_perms == P:
                print cubes[j]
                return
                
        num_digits = len(str(cubed))
        cubes = []
        
def totient(n):
    if n == 2:
        return 1
    result = 1
    is_even = False
    if n % 2 == 0:
        is_even = True
    arr = [True] * (n / 2 + 1)
    loop_start = 2
    step = 1
    if is_even:
        loop_start = 3
        step = 2
    for i in xrange(loop_start, len(arr), step):
        if arr[i]:
            if n % i == 0:
                for j in xrange(i + i, len(arr), i):
                    arr[j] = False
            else:
                result += 1
                
    return result * 2

def converge_e_helper(acc, curr_level, target):
    """
    Recursion terminates by either returning a 1 or a multiple of two depending on which level
    of convergence it's on.
    """
    if curr_level % 3 == 0:
        if curr_level == target:
            return acc
        else:
            return acc + fractions.Fraction(1, converge_e_helper(acc + 2, curr_level + 1, target))
    else:
        if curr_level == target:
            return 1
        else:
            return 1 + fractions.Fraction(1, converge_e_helper(acc, curr_level + 1, target))
    
def converge_e(level):
    if level <= 1:
        return fractions.Fraction(2, 1)
    return fractions.Fraction(2, 1) + fractions.Fraction(1, converge_e_helper(2, 2, level))
    
def e_65():
    print sum(map(int, list(str(converge_e(100).numerator))))

def e_69():
    max = 0
    max_n = 0
    for n in xrange(6, 1000001, 6):
        r = float(n) / totient(n)
        if r > max:
            max = r
            max_n = n
            print n
    print max_n 

def e_71():
    """" 
    Determine closest we can get to 3 / 7 for each denominator by solving for numerator 
    in 'num / denom = 3 / 7'.
    """    
    TARGET = float(3) / 7
    closest = float('infinity')
    closest_num = closest_denom = 0
    for denom in xrange(3, 1000001):
        num = int(denom * TARGET)
        diff = TARGET - (float(num) / denom)
        if diff < closest and diff != 0:
            closest = diff
            closest_num = num
            closest_denom = denom
    print closest_num, " / " , closest_denom

def e_73():
    """" Same idea as e_71() """
    result = 0
    d = 12000
    left_bound = float(1) / 3
    right_bound = float(1) / 2
    for denom in xrange(4, d + 1):
        left_num = math.floor(denom * left_bound) + 1
        right_num = math.ceil(denom * right_bound) - 1
        
        for num in xrange(int(left_num), int(right_num) + 1):
            if fractions.gcd(num, denom) == 1:
                result += 1
    print result
    
def e_74():
    TARGET = 60
    result = 0
    for i in xrange(69, 1000000):
        chain = set([i])
        fact_sum = sum(map(math.factorial, map(int, str(i))))
        while fact_sum not in chain:
            chain.add(fact_sum)
            if len(chain) > TARGET:
                break            
            fact_sum = sum(map(math.factorial, map(int, str(fact_sum))))
        if len(chain) == TARGET:
            result += 1
    print result

    
def num_sums(n, terms, lwr_lim):
    if terms == 1:
        return 1
    result = 0
    for i in xrange(lwr_lim, n / terms + 1):
        rmdr = n - i
        result += num_sums(rmdr, terms - 1, i)
    return result
    
def e_76():
    n = 100
    result = 0
    for num_terms in xrange(2, n + 1):
        result += num_sums(n, num_terms, 1)
    print result
              
def e_81():
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

def find_num_rectangles(width, height):
    result = 0
    for h in xrange(1, height + 1):
        for w in xrange(1, width + 1):
            result += (height - h + 1) * (width - w + 1)
    return result

def e_85():
    height = 0
    closest = float('inf')
    area = 0
    recs = 0
    TARGET = 2000000
    flag = True
    
    while flag:
        flag = False
        height += 1
        width = 1
        recs = find_num_rectangles(width, height)
        while recs < TARGET:
            flag = True
            diff = math.fabs(TARGET - recs)
            if diff < closest:
                closest = diff
                area = width * height
            width += 1
            recs = find_num_rectangles(width, height)
            
    print area
            
    
def e_92():
    total = 0
    lkup_tbl = {}
    for i in xrange(1, 10000000):
        curr = i
        while curr != 89 and curr != 1:
            sum_digits = 0
            for c in str(curr):
                sum_digits += int(c)**2
            curr = sum_digits
            if curr in lkup_tbl:
                break
        if curr == 89 or curr in lkup_tbl and lkup_tbl[curr] == True:
            lkup_tbl[i] = True
            total += 1
        else:
            lkup_tbl[i] = False
    print total

def e_99():
    curr_line = max_line = max_base = max_exp = 0
    
    f = open(INPUT_DIR + "base_exp.txt", "r")
    for line in f:
        curr_line += 1
        exp_pair = line.split(",")
        curr_base = int(exp_pair[0])
        curr_exp = int(exp_pair[1])
        
        if curr_base > max_base**(float(max_exp) / curr_exp):
            max_base = curr_base
            max_exp = curr_exp
            max_line = curr_line
    print str(max_line)
    
def is_bouncy(x):
    is_inc = is_dec = True
    x = str(x)
    for i in xrange(0, len(x) - 1):
        if x[i] < x[i + 1]:
            is_dec = False
        if x[i] > x[i + 1]:
            is_inc = False
        if not (is_inc or is_dec):
            return True
    return not (is_inc or is_dec)
        
def e_112():
    total_bouncy = 0
    i = 1
    digits2mem = 5 # Limits lookup table size. Best speedup at 5.
    max_lkup_size = 10**digits2mem
    mem = set()

    while i < max_lkup_size:
        i_str = str(i)
        # Bouncy numbers within a number means the whole number is bouncy
        if is_bouncy(i):
            total_bouncy += 1
            mem.add(str(i))
        if float(total_bouncy) / i == .99:
            print i
            return
        i += 1
    
    # Memoize numbers containing <= 'digits2mem' digits.
    while True:
        i_str = str(i)
        # Bouncy numbers within a number means the whole number is bouncy
        if i_str[len(i_str) - digits2mem : ] in mem or is_bouncy(i):
            total_bouncy += 1
        if float(total_bouncy) / i == .99:
            print i
            return
        i += 1
        
def e_113():
    # TODO
    result = 0
    i = 1
    digits2mem = 6
    max_lkup_size = 10**digits2mem
    mem = set()
    
    # Memoize numbers containing <= 'digits2mem' digits.
    while i < max_lkup_size:
        i_str = str(i)
        if i_str[len(i_str) - digits2mem : ] in mem or is_bouncy(i):
            mem.add(str(i))
        else:
            result += 1
        i += 1
    
    while i < 10**8:
        i_str = str(i)
        # Bouncy numbers within a number means the whole number is bouncy
        if i_str[len(i_str) - digits2mem : ] not in mem and not is_bouncy(i):
            result += 1   
        i += 1
        
    print result

 
def e_125():
    # TODO   
    for i in xrange(2, 10**8):
        if e_util.is_palindrome(str(i)):
            print i

def e_206():
    i = 1009000000
    i_s = str(i**2)
    template = ['2', '3', '4', '5', '6', '7', '8', '9', '0']
    while i_s[0] == '1':
        i += 1
        i_s = str(i**2)
        matched_all = True
        for j in xrange(len(template)):
            if template[j] != i_s[(j + 1) * 2]:
                matched_all = False
                break
        if matched_all:
            print i
            break

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

def e_345():
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
    
def e_205():
    wins = 0
    total = 0
    m = {}
    pete_sums = map(sum, e_util.repeat_perms([1,2,3,4], 9))
    colin_sums = map(sum, e_util.repeat_perms([1,2,3,4,5,6], 6))
    for pete in pete_sums:
        if pete in m:
            wins += m[pete]
        else:
            c = 0
            for colin in colin_sums:
               if pete > colin:
                    c += 1
            wins += c
            m[pete] = c
            
    print float(wins) / (len(pete_sums) * len(colin_sums))   

def is_prime_generating(n, primes):
    fs = e_util.get_factors(n)
    if len(fs) % 2 != 0:
        # if it has an integer root, 
        # it can't be prime-generating (since 2*root is not prime)
        return False
    for i in range(len(fs)/2):
        if (fs[i] + fs[len(fs) - 1 - i]) not in primes:
            return False
    return True

def e_357():
    sum = 1 # since 1 is prime generating
    n = 100000000
    primes = e_util.find_primes_set(n + 2)
    for i in range(2, n + 2, 2):
        if (i + 1 in primes and
                i / 2 + 2 in primes and
                is_prime_generating(i, primes)):
            sum += i
    print sum

def main():
    start = time.time()
    e_357()
    print "TIME: " + str(time.time() - start)

if __name__ == '__main__':
    main()

