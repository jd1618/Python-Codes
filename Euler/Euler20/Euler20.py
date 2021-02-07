def func(num):
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    sum = 0
    for elem in str(factorial):
        sum += int(elem)
    return sum

T = int(input())
for _ in range(T):
    N = int(input())
    print(func(N))
