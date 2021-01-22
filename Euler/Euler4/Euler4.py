# Project Euler 4 (largest palindrome product):

import time

tests = int(input('Number of test cases: '))
D, N = [int(input('Digits for test ' + str(i + 1) + ': ')) \
         for i in range(tests)], \
       [int(input('Bound for test ' + str(i + 1) + ': ')) \
         for i in range(tests)]

start = time.time()

def func(digits, bound):  
    '''
    Evaluates the product between two palindromes 
    with d digits below some specified bound. For
    the largest palindrome product between two 
    numbers with the same number of digits, set
    bound equal to (10**digits)**2
    '''
    product = []
    for i in range(10**(digits - 1) + 1, 10**digits):
        for j in range(10**(digits - 1), i): 
            if str(i*j) == str(i*j)[::-1]:                    # <--- checks for palindromes
                product.append(i*j)
    return max([i for i in product if i < bound])

for d in D:
    for n in N:
        print('Solution 1: ' + str(func(d, n)))  
                     
                      
end = time.time()
print('Execution time: ' + str(end - start))
