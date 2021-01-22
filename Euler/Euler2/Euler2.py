# Project Euler 2 (even Fibonacci):

import time

tests = int(input('Number of test cases: '))
N = [int(input('Test case ' + str(i + 1) + \
               ': ')) for i in range(tests)]

start = time.time()

def func(num):
    '''
    Sums even Fibonacci numbers
    '''
    sum, i = 0, 0
    fib_list = [1, 2]
    while fib_list[-1] < num:
        new_fib = fib_list[i] + fib_list[i + 1]
        fib_list.append(new_fib)
        i += 1
    if fib_list[-1] > num:
        fib_list.pop()                              # <--- removes last entry in list
    for num in fib_list:
        if num % 2 == 0:
            sum += num
    return sum
  
for num in N:
    print('Solution ' + str(N.index(num) + 1) + \
          ': ' + str(func(num)))
    
end = time.time()
print('Time execution: ' + str(end - start) + ' s')
