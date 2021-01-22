# Codewars factorial decomposition (5kyu):

import math
import time

tests = int(input('Number of test cases: '))
N = [int(input('Input for test ' + str(i + 1) + ': ')) for i in range(tests)]

start = time.time()

def factorial_func(num):
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        return factorial
    
def prime_list(num):
    p = 3
    primes = [2]
    while primes[-1] < num:
        prime = True
        for i in range(2, int(math.sqrt(p) + 1)):
            if p % i == 0: 
                prime = False
                break 
        if prime: 
            primes.append(p)
        p += 1
    if primes[-1] > num:
        primes.pop()
    return primes

def decomp(n):
    decomposition = ''
    prime_facts = []
    factorial = factorial_func(n)
    while factorial % 2 == 0:
        prime_facts.append(2)
        factorial = factorial // 2
    primes = prime_list(n)
    for i in primes[1:]:
        while factorial % i == 0:
            prime_facts.append(i)
            factorial = factorial // i
    if factorial > 2:
        prime_facts.append(factorial)
    dist_primes = list(sorted(set(prime_facts)))
    for i in range(len(dist_primes)):
        if prime_facts.count(dist_primes[i]) > 1:
            decomposition += str(dist_primes[i]) + '^' \
            + str(prime_facts.count(dist_primes[i])) + ' * '
        else:
            decomposition += str(dist_primes[i]) + ' * '
    return decomposition[:-3]

for num in N:
    print(decomp(num))

end = time.time()
print('Time execution: ' + str(end - start))
