# Project Euler 3 (largest prime factor):

import math
import time

tests = int(input('Number of test cases: '))        
N = [int(input('Test case ' + str(i + 1) + ': ')) \
     for i in range(tests)]                         

start = time.time()                                 

def func(num):
    prime_fact = []
    while num % 2 == 0:
        prime_fact.append(2)
        num = num/2
    for i in range(3, int(math.sqrt(num)) + 1, 2):           # <--- start at 3 since must be odd
        while num % i == 0:                                  # <--- square root for optimal search
            prime_fact.append(i)
            num = num/i
    if num > 2:
        prime_fact.append(num)
    return prime_fact[-1]                                     # <--- yields the largest prime

# Subtract by lcm sum to get rid of overlaps:
for num in N:
    print('Solution ' + str(N.index(num) + 1) + \
          ': ' + str(func(num)))  
                                                     
end = time.time()                                    
print('Time execution: ' + str(end - start) + ' s')  
