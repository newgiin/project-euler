import math
import time
from decimal import *
import sys


# ####################################
# Misc. functions
# ####################################

# ------------------------
# Number crunching
# ------------------------
def sieve(n):
    primes = [2]
    nums = [True]*n
    i = 3
    while (i < n):
        primes.append(i)
        sieve = i*i
        step = 2*i
        while (sieve < n):
            nums[sieve] = False
            sieve += step 
        # find next unmarked num
        found = False
        i += 2
        while (i < n):
           if (nums[i]):
                found = True
                break 
           i += 2
        if (not found):
            break
    
    return primes

def is_prime(x):
    if (x == 2):
        return True
    if (x < 2 or x % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(x)+1), 2):
        if (x % i == 0):
            return False
    return True
    
def get_factors(x):
    result = [1]
    if (x == 1):
        return result

    root = math.sqrt(x)
    for i in range(2, int(root)+1):
        if (x % i == 0):
            result.append(i)
            result.append(x/i)
    result.sort()

    if (root % 1 == 0):
        result.remove(int(root)) # remove duplicate root 

    return result  

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result   
  
def get_primeFactors(x):
    prime_factors = filter(is_prime, get_factors(x))
    return prime_factors              
# ------------------------
# String crunching
# ------------------------
def is_perm(x, y):
    y = str(y)
    for c in (str(x)):
        c_index = y.find(str(c))
        if (c_index == -1):
            return False
        y = y[0:c_index] + y[c_index + 1:] 
    if (len(y) == 0):
        return True
    return False
    
def get_perms(word):
    result = []
    for i in range(0, len(word)):
        remainder = word[0:i] + word[i+1:]
        for perm in get_perms(remainder):
            result.append(word[i] + perm)
    if (len(word) == 1):
        result.append(word[0])
    return result    

def is_perm(a, b):
    a = str(a)
    b = str(b)
    if (len(a) != len(b)):
        return False
    for c in a:
        ind = -1
        try:
            ind = b.index(c) 
        except ValueError:
            return False
        b = b[0:ind] + b[ind+1:len(b)] 
    return True    
    

def is_palindrome(s):
    s= str(s)
    for i in range(0, len(s)/2):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True 
         
# ------------------------

# ####################################
# Solutions
# ####################################

# ----------------
# 2011 code
# ----------------
def e_16():
    print sum([int(c) for c in str(2**1000)])

def e_13():
    f = open("e_13.in", "r")
    line = f.readline()
    # 2d array holding last 10 digits per line
    # must do it this way since Python has no easy way to make 2d arrays
    arr = [[],[],[],[],[],[],[],[],[],[]]
    while(line):
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
    for place in range(10):
        sum = carry
        for digit in arr[place]:
            sum += digit
        ones = sum%10
        result = str(ones) + result
        carry = int((sum - ones)/10)
    print result

def e_14():
    occurence = 0
    maxlength = 0
    memoi = [0]*1000000
    for curr in xrange(1000000):
        length = 1
        n = curr
        if(memoi[n] != 0):
            length = memoi[n]
        else:
            while(n > 1):
                if(n < 1000000 and memoi[n] != 0):
                    length += memoi[n]
                    break
                if(n%2 == 0):
                    n =int(n/2)
                else:
                    n = 3*n + 1
                length += 1
        memoi[curr] = length
        if(length > maxlength):
            maxlength = length
            occurence = curr
    print(str(occurence) + " | " + str(maxlength))    

def e_17():
    print sum([int(x) for x in str(math.factorial(100))])

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

    for row in range(1, len(arr)):
        arr[row][0] += arr[row-1][0]
        for i in range(1, len(arr[row])-1):
            if(arr[row-1][i-1] > arr[row-1][i]):
                arr[row][i] += arr[row-1][i-1]
            else:
                arr[row][i] += arr[row-1][i]
        arr[row][len(arr[row])-1] += arr[row-1][len(arr[row-1])-1]
    print max(arr[len(arr)-1])      
    
def e_19():
    SUN = 1; MON = 2;TUE = 3;WED  =4; THU = 5; FRI = 6; SAT = 7; 
    year = 1901
    month = 1
    day = TUE

    sum = 0
    while(year < 2001):
        month = 1
        while(month <= 12):
            if(month == 9 or month == 4 or month == 6 or month == 11):
                day += 1
                if(day > SAT):
                    day = SUN
            elif(month == 2):
                day -= 1
                if(day < SUN):
                    day = SAT
            else:
                if(day == SAT):
                    day = MON
                elif(day == FRI):
                    day = SUN
                else:
                    day += 2
            if(day == SUN):
                sum += 1
            month += 1
        year += 1
    
    print sum
    
def sumDivisors(n):
    sum = 0;
    for i in range(1, int(math.sqrt(n))+1):
        if(n%i == 0):
            sum += i;
            sum += n/i;
    return sum;
        
def e_21():
    n = 10000;
    visited = [];
    result = 0;
    for i in range(n):
        if i not in visited:
            d = sumDivisors(i);
            if(sumDivisors(d) == i and d != i):
                result += i;
                visited.append(i);
                if(d < n):
                    result += d;
                    visited.append(d);
    print result;
    
def e_25():
    first = 0
    sec = 1
    n = 1
    while(len(str(sec)) < 1000):
    #while(n < 20):
        temp = first
        first = sec
        sec += temp
        n += 1
    print n
    
def findMaxRecur(s):
    result = ""
    # do that binary split magic!
    rightLimit = int(len(s)/2)
    while(rightLimit > 0):
        for start in range(len(s)-rightLimit*2+1):
            substring = s[start:rightLimit+start]
            if(substring == s[rightLimit+start:rightLimit+start+len(substring)]):
                # if 's' contains substring sufficient number of times, 
                # with some leeway at head and tail
                if(s.count(substring) > int(len(s)/len(substring))-5):
                    subresult = findMaxRecur(substring)
                    if(len(subresult) > 0):
                        return subresult
                    else:
                        return substring
        rightLimit -= 1
    return result
    
def e_26():
    getcontext().prec = 2000
    max_d = 0
    max_str = ""
    start = time.time()
    for d in range(3,1000):
        dec = str(Decimal(1)/Decimal(d)).split(".")[1]
        recurrer = findMaxRecur(dec)
        if(len(max_str) < len(recurrer)):
            max_d = d
            max_str = recurrer
        
    print str(max_d)
    
def e_27():
    max_primes = 0
    max_a = 0
    max_b = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while (is_prime(n**2 + a*n + b)):
                n += 1
            if (n > max_primes):
                max_primes = n
                max_a = a
                max_b = b
    print max_a*max_b
    
def e_28():
    spiralSize = 3
    curr = 1
    result = 1
    while(spiralSize <= 1001):
        for i in range(4):
            curr += spiralSize-1
            result += curr
        spiralSize += 2
    print result
    
def e_31():
    denoms = [1,2,5,10,20,50,100,200]

    def combo_recurr(n, maxDenom):
        if(maxDenom == 1):
            return 1
        remainder = n - maxDenom
        if(remainder == 0):
            return 1 + combo_recurr(n,denoms[denoms.index(maxDenom)-1])
        if(remainder < 0):
            return combo_recurr(n, denoms[denoms.index(maxDenom)-1])
        return combo_recurr(remainder, maxDenom)+combo_recurr(n, denoms[denoms.index(maxDenom)-1])
    
    def combos(n):
        return combo_recurr(n,200)
    
    
    print combos(200)

def e_35():
    def isCircular(n):
        n = list(str(n));
        for i in range(len(n)-1):
            last = n[len(n)-1]
            for c in range(len(n)-2, -1, -1):
                n[c+1] = n[c];
            n[0] = last;
            if(is_prime(int("".join(n))) == False):
                return False;
        return True;

    primes = sieve(1000000)

    # count number of circular primes
    count = 0;
    for i in range(len(primes)):
        if(isCircular(primes[i])):
            count += 1;
    print count;
    
def e_36():
    total = 0
    for n in range(1000000):
        if(is_palindrome(n) and is_palindrome("{0:b}".format(n))):
            total += n
    print total
    
def e_37():
    primes = sieve(900000)
    result = []
    for i in range(4,len(primes)):
        s = str(primes[i])
        # remove from right to left
        truncable = True
        while(len(s) > 1):
            s = s[0:len(s)-1]
            if(int(s) not in primes):
                truncable = False
                break
        if(truncable):
            # from left to right
            s = str(primes[i])
            while(len(s) > 1):
                s = s[1:len(s)]
                if(int(s) not in primes):
                    truncable = False
                    break
        if(truncable):
            result.append(primes[i])
    print sum(result)
    
def e_40():
    d_end = 0
    d = 1
    p = 0
    result = 1
    while (d <= 1000000):
        d_beg = d_end + 1
        r = 10**p
        len_r = len(str(r))
        i_beg = 10**p
        i_end = 10**(p+1)-1
        d_end = d_beg + len_r*9*r-1
        while (d >= d_beg and d <= d_end):
            d_cell = (d - d_beg) / len_r
            num = i_beg + d_cell     
            digit = str(num)[(d - d_beg) % len_r]
            result *= int(digit)
            d *= 10
        p += 1
    print result
        
def e_41():
    def isPanDigital(x):
        x = str(x)
        n = len(x)
        digits = []
        for i in range(1, n+1):
            digits.append(str(i))
        for i in range(len(digits)):
            if digits[i] not in x:
                return False
        return True
    
    primes = sieve(99999999)
    for i in reversed(primes):
        if(isPanDigital(i)):
            print i
            break
        
def e_67():
    tri = open("triangle.txt", "r")
    line = tri.readline()
    arr = []
    while(line):
        row = []
        for num in line.split():
            row.append(int(num))
        arr.append(row)
        line = tri.readline()
    
    for row in range(1, len(arr)):
        arr[row][0] += arr[row-1][0]
        for i in range(1, len(arr[row])-1):
            if(arr[row-1][i-1] > arr[row-1][i]):
                arr[row][i] += arr[row-1][i-1]
            else:
                arr[row][i] += arr[row-1][i]
        arr[row][len(arr[row])-1] += arr[row-1][len(arr[row-1])-1]
    print max(arr[len(arr)-1])                
# -------------
    
def e_49():
    primes = sieve(10000)
    for i in range(0, len(primes)-3):
        for j in range(i+1, len(primes)-2): 
            if (is_perm(primes[i], primes[j])):
                diff = primes[j] - primes[i]
                try:
                    partner = primes.index(primes[j] + diff)
                except ValueError:
                    partner = -1
                if (partner != -1 and is_perm(primes[j], primes[partner])):
                    print str(primes[i]) + " " + str(primes[j]) + " " + str(primes[partner])

def e_24():
    perms = get_perms("0123456789")
    print perms[999999]

def e_30():
    result = []
    for i in range(2, 9999999):
        word = str(i)
        acc = 0
        for c in word:
            acc += int(c)**5
        if (acc == i):
            result.append(i) 
    print sum(result)

def e_29():
    all = set(i**j for i in range(2, 101) for j in range(2, 101)) 
    print len(all)

def e_34():
    for i in range(3, 99999):
        total = sum(factorial(int(c)) for c in str(i))
        if (total == i):
            print i

# Returns list of abundant numbers up to n 
def get_abundants(n):
    result = []
    for i in range(2, n):
        if (sum(get_factors(i)) > i):
            result.append(i)
    return result 

def abundant_summable(x, abunds=[]):
    if (not abunds):
        abunds = get_abundants(x)
    else:
        # get subset of abunds we care about
        i = 0
        for abund_num in abunds:
            if (abund_num >= x):
                break
            i += 1
        abunds = abunds[0:i]

    abunds_set = set(abunds)
    for abund_num in abunds:
        if ((x - abund_num) in abunds_set):
            return True
    return False     

def e_23():
    total = sum(i for i in range(1,24))
    abunds = get_abundants(28124)
    for i in range(25, 28124):
        if (not abundant_summable(i, abunds)):
            total += i
    print total

def is_penta(x):
    c = -2*x
    if (((1 + math.sqrt(1-12*c))/6) % 1 == 0):
        return True
    return False

def is_hexa(x):
    c = x * -1
    if (((1 + math.sqrt(1-8*c))/4) % 1 == 0):
        return True
    return False
    
def e_45():
    n = 286
    tri = n*(n+1)/2  
    while (not (is_penta(tri) and is_hexa(tri))):
       n += 1
       tri = n*(n+1)/2
    print tri 

def e_52():
    i = 10
    while (True):
        flag = True
        m = 2
        for m in range(2, 7):
           if (not is_perm(i, i*m)):
                flag = False
                break
        if (flag):
            print i
            break 
        i += 1
        
def e_39():
    max_sols = 0
    max_p = 0
    for p in range(12, 1001):
        sols = 0
        a = 1
        b = p
        while ( a < b):
            d = p - a
            b = (d**2 - a**2) / float((2*d)) 
            a += 1
            if (b % 1 == 0): # sides are integral length
                sols += 1
        if (sols > max_sols):
            max_sols = sols
            max_p = p
    print max_p

def e_33():
    for num in range(11, 99):
        if (str(num)[1] == "0"):
            continue
        for den in range(num+1, 99):
            num_s = str(num)
            den_s = str(den)
            if (den_s[1] == "0"):
                continue
            for n_i in range(0, len(num_s)):
                for d_i in range(0, len(den_s)):
                    if (num_s[n_i] == den_s[d_i]):
                        red_num = num_s[0:n_i] + num_s[n_i+1:len(num_s)]
                        red_den = den_s[0:d_i] + den_s[d_i+1:len(den_s)]
                        if (float(int(red_num))/int(red_den) == float(num)/den):
                            print num_s + " / " + den_s
             
def e_32():
    result = set()
    for a in range(123, 9876):
        a_s = str(a)
        b = 0
        prod = 1 
        while (len(str(prod)) <= 4):
            b += 1
            # simple string checks
            b_s = str(b)
            has_rep = False
            for c in a_s:
                if c in b_s:
                    has_rep = True 
                    break
            if (has_rep):
                continue

            prod = a*b
            if (is_perm(a_s + b_s + str(prod), "123456789")): 
                result.add(prod)
    print sum(result)
 
def e_53():
    total = 0
    for n in range(23, 101):
        for r in range(2, n):
            combos = factorial(n) / (factorial(r)*factorial(n-r))
            if (combos > 1000000):
                total += 1
    print total 

def e_56():
    max = 0
    for a in range(1, 100):
        for b in range(1, 100):
            prod = a**b
            digit_sum = sum([int(c) for c in str(prod)])
            if (digit_sum > max):
                max = digit_sum
    print max

def e_38():
    max = 0
    for i in range(2, 49877):
        ct_prd = ""
        m = 1
        while (len(ct_prd) < 9):
            ct_prd += str(i*m)
            m += 1
        if (is_perm(ct_prd, "123456789") and int(ct_prd) > max):
            max = int(ct_prd)
    print max    

def e_55():
    result = 0
    for i in range (1, 10000):
        curr = i
        is_lychrel = True
        for iterations in range(0, 50):
            sum = curr + int((str(curr)[::-1]))
            if (is_palindrome(str(sum))):
                is_lychrel = False
                break
            curr = sum
        if (is_lychrel):
            result += 1 
    print result

def e_50():
    max = 0
    max_sum = 0
    primes = sieve(5000)
    prime_set = set(sieve(1000000))
    for i in range(0, len(primes)):
        sum = primes[i]
        seq_len = 1
        for j in range(i+1, len(primes)):
            sum += primes[j]
            if (sum > 1000000):
                sum -= primes[j]
                break
            if (sum in prime_set):
                seq_len = j-i+1
        if (seq_len > max):
            max = seq_len
            max_sum = sum
    print max_sum

# Solves quadratic equation and returns left and right zero-crossing in a list, 
# at index 1 and 2 respectively.
def solv_quad(a, b, c):
    sol = [None]*2
    try:
        sol[0] = (-1*b - math.sqrt(b**2-4*a*c)) / float(2*a)
    except (ValueError, DivideByZeroError):
        pass
    try:
        sol[1] = (-1*b + math.sqrt(b**2-4*a*c)) / float(2*a)
    except (ValueError, DivideByZeroError):
        pass
    return sol

def is_triangle(word):
    total = 0
    for c in word:
        total += ord(c)-64
    sol = solv_quad(1, 1, -2*total)[1]
    if (sol != None and sol % 1 == 0):
        return True
    return False

def e_42():
    result = 0
    f = open("words.txt", "r")
    line = f.readline()
    words = line.split(",")
    for w in words:
        w = w.replace('"', '')
        if (is_triangle(w)):
            result += 1
    print result 

def is_sumPrimeAndDouble(x, primes=sieve(1000000)):
    p = primes[0]
    i = 0
    while (p < x): 
        sum = 0
        base = 1
        while (sum < x):
            sum = p + 2*base**2
            base += 1
        if (sum == x):
            return True   
        i += 1
        p = primes[i]
    return False

def e_46():
    i = 9
    primes = sieve(10000)
    while (True):
        if (not is_prime(i) and not is_sumPrimeAndDouble(i, primes)):
            print i
            return  
        i += 2
    
def e_47():
    i = 1000
    T = 4 # find first T consecutive integers with T distinct factors
    i_processed = False # optimization to avoid getting prime factors twice
    while (True):
        if (i_processed or len(get_primeFactors(i)) >= T):
            seq_len = 1
            for j in reversed(range(1,T)): 
                if (len(get_primeFactors(i+j)) >= T):
                    seq_len += 1
                else:
                    break
            if (seq_len == T):
                print [i+k for k in range(0, T)]
                return
            i += T - seq_len + 1 # skip ahead 
            if (seq_len > 1):
                i_processed = True
            else:
                i_processed = False
        else:
            i += 1 
            i_processed = False

def e_43():
    sum = 0
    primes = sieve(18)
    for p in get_perms("0123456789"):
        flag = True
        for i in range(1, 8):
            if (int(p[i:i+3]) % primes[i-1] != 0):
                flag = False
                break    
        if (flag):
            sum += int(p)
    print sum

def e_44():
    RANGE = 10000 # terms to lookahead for matching pairs
    pentas = [n*(3*n-1)/2 for n in range(1, 10001)]
    lookup_tbl = set(pentas)
    min_diff = sys.maxint
    for i in range(0, len(pentas)-1):
        for j in range(i+1, min(i+RANGE+1, len(pentas))):
            sum = pentas[j] + pentas[i]
            diff = pentas[j] - pentas[i]
            if (sum in lookup_tbl and diff in lookup_tbl):
                if (diff < min_diff):
                    min_diff = diff
    print min_diff 

def e_79():
    f = open("keylog.txt", "r")
    visited = {}
    for line in f:
        line = line.strip() # remove newline
        for i in range(0, len(line)):
            c = line[i]
            if (c not in visited):
                visited[c] = []
            for k in line[i+1:]:
                if (k not in visited[c]):
                    visited[c].append(k)    
    code = ""
    while (len(visited) > 0):
        for c in visited: 
            if (len(visited[c]) == len(visited) - 1):
                code += c
                del visited[c]
                break
    print code

def e_63():
    digits = 1
    count = 1 # we know 1^x will always be 1 digit, so just count it here
    while (True):
        i = 2
        pwrd = str(i**digits)
        while (len(pwrd) <= digits):
            if (len(str(pwrd)) == digits):
                count += 1
            i += 1
            pwrd = str(i**digits)
        if (i == 10 and len(str(9**digits)) < digits):
            break
        digits += 1
    print count

def get_combos(alphabet, k):
    result = []
    if (k == 1):
        return list(alphabet)
    for i in range(0, len(alphabet)-k+1):
        remainder = alphabet[i+1:len(alphabet)]
        for c in get_combos(remainder, k-1):
            result.append(alphabet[i] + c)    
    return result

def has_english(filename):
    file = open(filename, "r")
    vocab = set(['the', 'The','and', 'you', 'there', 'have', 'that', 'from'])
    #vocab = ['the']
    threshold = 9
    found = 0
    for line in file:
        for word in line.split():
            if (word in vocab):
                found += 1
    file.close()
    if (found >= threshold):
        return True
    return False

def decrypt(cipher, key, outname=None):
    f = open(cipher, "r")
    outfile = None
    if (not outname):
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
            if (i == len(key)):
                i = 0
    outfile.close()
    f.close()

def e_59():
    cipher = "cipher1.txt"
    outname = "decrypted.out"
    all_letters = ""
    done = False
    key_len = 3

    for c in range(97, 97+26):
        for _ in range(0, key_len):
            all_letters += chr(c)
    for combo in get_combos(all_letters, key_len):
        for key in get_perms(combo):
            decrypt(cipher, key, outname)
            if (has_english(outname)):
                print key
                done = True
                break 
        if (done):
            return
    print "FAILED"

def e_92():
    total = 0
    lkup_tbl = {}
    for i in range(1, 10000000):
        curr = i
        while (curr != 89 and curr != 1):
            sum_digits = 0
            for c in str(curr):
                sum_digits += int(c)**2
            curr = sum_digits
            if (curr in lkup_tbl):
                break
        if (curr == 89 or curr in lkup_tbl and lkup_tbl[curr] == True):
            lkup_tbl[i] = True
            total += 1
        else:
            lkup_tbl[i] = False
    print total

# Determine the decimal portion of sqrt(2) to the n'th expansion.
def sqrt2_helper(n):
    if (n == 1):
        return .5
    return float(1)/(2+sqrt2_helper(n-1)) 

def e_57():
    lkup_tbl = {}
    for i in range(1, 5):
        expan = i
        acc = .5
        while (expan > 1):
            if ((expan-1) in lkup_tbl):
                acc = lkup_tbl[expan-1]
                acc = float(1) / (2+acc)
                break
            acc = float(1) / (2+acc)
            expan -= 1
        lkup_tbl[i] = acc
        print 1 + acc 

def e_58():
    skip = 1
    p = 0
    diags = 1
    i = 1
    # create spiral
    while (True):
        for _ in range(4):
            i += skip + 1
            if (is_prime(i)):
                p += 1
        diags += 4
        if (float(p) / diags < .10):
            print skip + 2
            return
        skip += 2

def totient(n):
    #print str(n) + ": 1",
    if (n == 2):
    #    print ""
        return 1
    result = 1
    is_even = False
    if (n % 2 == 0):
        is_even = True
    arr = [True]*(n/2+1)
    loop_start = 2
    step = 1
    if (is_even):
        loop_start = 3
        step = 2
    for i in range(loop_start, len(arr), step):
        if (arr[i]):
            if (n % i == 0):
                for j in range(i+i, len(arr), i):
                    arr[j] = False
            else:
    #            print i,
                result += 1

    # loop_start = n/2 + 1
    # if (is_even and loop_start % 2 == 0):
    #     loop_start += 1 
    # for i in range(loop_start, len(arr), step):
    #     if (arr[i]):
    #         print i,
    #         result += 1
    #print ""
    return result*2

def e_69():
    max = 0
    max_n = 0
    for n in range(6, 1000001, 6):
        r = float(n) / totient(n)
        if (r > max):
            max = r
            max_n = n
            print n
    print max_n 


def main():
    start = time.time()
    e_30()
    print "TIME: " + str(time.time() - start)

if __name__ == '__main__':
    main()

