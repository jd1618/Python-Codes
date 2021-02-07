# Project Euler 16 (power digit sum):

def func(num):
    tmp = str(2**num)
    sum = 0
    for num in tmp:
        sum += int(num)
    return sum

func(1000) # <--- solution is 1366 
