from math import ceil

tests = int(input())
N = [int(input()) for i in range(tests)]

def func(num):
    return ceil((1/12)*num*(num - 1)*(num + 1)*(3*num + 2))

for num in N:
    print(func(num))
