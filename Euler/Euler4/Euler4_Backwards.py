import time

tests = int(input('Number of test cases: '))
D, N = [int(input('Digits for test ' + str(i + 1) + ': ')) \
         for i in range(tests)], \
       [int(input('Bound for test ' + str(i + 1) + ': ')) \
         for i in range(tests)]

start = time.time()

# Algorithm to reverse a number:
def num_rev(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = 10*rev + rem
        num = num // 10
    return rev

# Searching for palindromes from largest first:
def max_palindrome(digits, bound):
    '''
    Evaluates the product of two palindromes 
    with d digits below some bound. For
    the largest palindrome product, set
    bound equal to (10**digits)**2
    '''
    product = 0
    n1 = 10**digits - 1                             # <--- starts searching through largest numbers
    while n1 >= 10**(digits - 1):
        n2 = 10**digits - 1
        while n2 >= n1:
            if n1*n2 <= product:
                break
            if n1*n2 == num_rev(n1*n2) \
            and n1*n2 < bound:
                product = n1*n2
            n2 -= 1
        n1 -= 1
    return product

for d in D:
    for n in N:
        print('Solution 1: ' + str(max_palindrome(d, n)))  
                     
                      
end = time.time()
print('Execution time: ' + str(end - start))
