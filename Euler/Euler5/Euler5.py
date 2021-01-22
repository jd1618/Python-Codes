# Project Euler 5 (smallest multiple):

import time

tests = int(input('Number of test cases: '))
N = [int(input('Test case ' + str(i + 1) + ': ')) \
     for i in range(tests)]

start = time.time()

tests = int(input())
N = [int(input()) for i in range(tests)]

def func(num):
    tmp = 2*num
    while True:
        l = [tmp % i for i in range(2, num + 1)]
        if sum(l) == 0:
            break
        else:
            l = []
            tmp += num
    return tmp

for num in N:
    print(func(num))

end = time.time()
print('Execution time: ' + str(end - start))
