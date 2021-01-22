# Project Euler 6 (sum square difference):

import time

tests = int(input('Number of test cases: '))
N = [int(input('Test case ' + str(i + 1) + ': ')) \
     for i in range(tests)]

start = time.time()

def func(num):
    sum_square, sum = 0, 0
    for i in range(1, num + 1):
        sum_square += i**2
        sum += i
    square_sum = sum**2
    return square_sum - sum_square

for num in N:
    print(func(num))
    
end = time.time()
print('Execution time: ' + str(end - start))
