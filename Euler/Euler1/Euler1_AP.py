import time

tests = int(input('Number of test cases: '))        
N = [int(input('Test case ' + str(i + 1) + ': ')) \
     for i in range(tests)]                         

start = time.time()                                 

# Arithmetic progression:
def func(num, n):
    alpha = (num - 1)//n                                 # <--- // denotes floor division 
    return alpha*(alpha + 1)//2                          # <--- sum of natural numbers

def lcm(a, b):
    '''
    Calculates the lowest common multiple
    '''
    tmp = max(a, b)
    lcm = 0
    while lcm == 0:
        if tmp % a == 0 and tmp % b == 0:
            lcm += tmp
            break
        else:
            tmp += 1
    return lcm

# Subtract by lcm sum to get rid of overlaps:
for num in N:
    print('Solution ' + str(N.index(num) + 1) + \
          ': ' + str(3*func(num, 3) + 5*func(num, 5) - \
                     lcm(3, 5)*func(num, 15)))  
                                                     
end = time.time()                                    
print('Time execution: ' + str(end - start) + ' s')                                
