# Codewars Sum of positive (8kyu):

import time

tests = int(input('Number of tests: '))

# Separate inputs with a comma and a space:
N = [[input('Array for test number ' + str(i + 1) + ': ').split(', ')] \
               for i in range(tests)]

start = time.time()

def positive_sum(arr):
    '''
    Sums positive numbers in an array
    '''
    return sum([float(num) for num in arr if float(num) > 0])
  
for i in range(tests):
    for arr in N[i]:
        print('Solution 1: ' + str(positive_sum(arr)))

end = time.time()
print('Time execution: ' + str(end - start) + ' s')
