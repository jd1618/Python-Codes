# Project Euler 1 (Multiples of 3 and 5):

# A simple approach to finding the sum of all multiples of 3 and 5 strictly less 
# than num, a natural number to be specified:

import time

tests = int(input('Number of test cases: '))         # <--- set number of test cases
N = [int(input('Test case ' + str(i + 1) + ': ')) \
     for i in range(tests)]                          # <--- set num for each case

start = time.time()                                  # <--- initiates timer

def func(num):
    ''' 
    Sums all multiples of 3 and 5 below num
    '''
    sum = 0
    for i in range(3, num):                          # <--- 3 is the first number to keep
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

for num in N:
    print('Solution ' + str(N.index(num) + 1) + \
          ': ' + str(func(num)))                     # <--- prints the corresponding sums
    
end = time.time()                                    # <--- time after code termination
print(end - start)                                   # <--- prints execution time
