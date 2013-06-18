import math

# ------------------------
# Number crunching
# ------------------------
def get_primes(n):
    """
    Returns a list of prime numbers up to 'n'. Implemented
    using the Sieve of Eratosthenes.
    """
    primes = [2]
    nums = [True] * n
    i = 3
    while i < n:
        primes.append(i)
        sieve = i * i
        step = 2 * i
        while sieve < n:
            nums[sieve] = False
            sieve += step 
        # find next unmarked num
        i += 2
        while i < n:
           if nums[i]:
                break 
           i += 2
    
    return primes

def primes_set(n):
    """
    Returns a set of prime numbers up to 'n'.
    """
    primes = set([2])
    nums = [True] * n
    i = 3
    while i < n:
        primes.add(i)
        sieve = i * i
        step = 2 * i
        while sieve < n:
            nums[sieve] = False
            sieve += step 
        # find next unmarked num
        i += 2
        while i < n:
           if nums[i]:
                break 
           i += 2

    return primes
    
def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x) + 1), 2):
        if x % i == 0:
            return False
    return True
    
def factor(x):
    result = [1]
    big_half = []
    if x == 1:
        return result

    root = math.sqrt(x)
    for i in range(2, int(root) + 1):
        if x % i == 0:
            result.append(i)
            big_half.insert(0, x / i)
    if root % 1 == 0:
        big_half.pop(0) # remove duplicate root 
    result += big_half
    result.append(x)
    
    return result
    
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result   
  
def prime_factors(x):
    return filter(is_prime, factor(x))

def solve_quad(a, b, c):
    """ 
    Solves quadratic equation and returns left and right 
    zero-crossing in a list, at index 0 and 1 respectively.
    """
    sol = [None] * 2
    if a == 0:
        if b != 0:
            sol[0] = -c / b
    else:
        try:
            root = math.sqrt(b**2 - 4 * a * c)
            sol[0] = (-1 * b - root) / float(2 * a)
            sol[1] = (-1 * b + root) / float(2 * a)
        except ValueError:
            pass
    return sol
    
# ------------------------
# String crunching
# ------------------------
def is_perm(word1, word2):
    if len(word1) != len(word2):
        return False
    counts = {}
    for c in word1:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1

    for c in word2:
        if c not in counts:
            return False
        counts[c] -= 1
        if counts[c] < 0:
            return False
        elif counts[c] == 0:
            del counts[c]
    if len(counts) != 0:
        return False
    return True
    
def get_perms(word):
    """ Returns an array of unique permutations of the input string. """
    result = []
    seen = []
    for i in range(0, len(word)):
        if word[i] not in seen: # do not include redundants
            seen.append(word[i])
            remainder = word[0 : i] + word[i + 1 : ]
            for perm in perms(remainder):
                result.append(word[i] + perm)
    if len(word) == 1:
        result.append(word[0])
    return result   

def is_palindrome(s):
    s= str(s)
    for i in range(0, len(s) / 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True 

def get_combos(items, n):
    """ 
    Returns a list of all possible 'n'-character combinations 
    of the symbols in 'items'. 
    """    
    result = []
    if n == 1:
        return [[x] for x in items]
    for i in range(0, len(items) - n + 1):
        remainder = items[i + 1 : len(items)]
        for c in combos(remainder, n - 1):
            result.append([items[i]] + c)    
    return result
  
def repeat_perms(items, n):
    """ 
    Returns a list of all n-length permutations of
    items in 'items', allowing repetition
    """
    if n <= 0:
        return []
    if n == 1:
        return [[item] for item in items]
    result = []
    for item in items:
        for s in repeat_perms(items, n - 1):
            result.append([item] + s)
    return result 

def repeat_combos(items, n):
    if n <= 0 or len(items) == 0:
        return []
    if n == 1:
        return [[item] for item in items]
    result = []
    subset = items[1:]
    result.append([items[0]]*n)
    for i in range(n):
        prefix = [items[0]]*i
        for combo in repeat_combos(subset, n - i):
            result.append(prefix + combo)   
    return result

