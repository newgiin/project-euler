import math

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
        i += 2
        while (i < n):
           if (nums[i]):
                break 
           i += 2
    
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
  
def get_prime_factors(x):
    return filter(is_prime, get_factors(x))              
# ------------------------
# String crunching
# ------------------------
def is_perm(x, y):
    if (len(x) != len(y)):
        return False
    for c in x:
        c_index = y.find(c)
        if (c_index == -1):
            return False
        y = y[0:c_index] + y[c_index + 1:] 
    if (len(y) == 0):
        return True
    return False
    
""" Returns an array of unique permutations of the input string. """
def get_perms(word):
    result = []
    seen = []
    for i in range(0, len(word)):
        if (word[i] not in seen): # do not include redundants
            seen.append(word[i])
            remainder = word[0:i] + word[i+1:]
            for perm in get_perms(remainder):
                result.append(word[i] + perm)
    if (len(word) == 1):
        result.append(word[0])
    return result   

def is_palindrome(s):
    s= str(s)
    for i in range(0, len(s)/2):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True 

""" Returns a list of all possible 'n'-character combinations of the symbols in 'alphabet'. """    
def get_combos(alphabet, n):
    result = []
    if (n == 1):
        return list(alphabet)
    for i in range(0, len(alphabet)-n+1):
        remainder = alphabet[i+1:len(alphabet)]
        for c in get_combos(remainder, n-1):
            result.append(alphabet[i] + c)    
    return result    