import time

tests = int(input())
N = [int(input()) for i in range(tests)]

# The number of adjacent numbers we want to multiply:
K = [int(input()) for i in range(tests)]

start = time.time()

def func(num, k):
    adj_prod = []
    prod = 1
    for i in range(len(str(num)) - k + 1):
        for j in range(k):
            prod *= int(str(num)[i + j])
        adj_prod.append(prod)
        prod = 1
    return max(adj_prod)
  
for num in N:
    for k in K:
        print(func(num, k))
