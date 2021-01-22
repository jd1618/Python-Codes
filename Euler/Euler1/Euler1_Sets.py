import time

tests = int(input('Number of test cases: '))         
N = [int(input('Test case ' + str(i + 1) + ': ')) \
     for i in range(tests)]                          

start = time.time()                                  

def func(num):
    return sum({i for i in range(3, num, 3)}.union({i for i in range(5, num, 5)}))

for num in N:
    print('Solution ' + str(N.index(num) + 1) + \
          ': ' + str(func(num)))  
                                                     
end = time.time()                                   
print('Time execution: ' + str(end - start) + ' s')                                 
