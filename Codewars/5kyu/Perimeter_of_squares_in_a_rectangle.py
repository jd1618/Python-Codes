def perimeter(n):
    f1, f2 = 1, 1
    sum = f1
    for _ in range(n):
        sum += f2
        tmp = f1
        f1 = f2
        f2 += tmp
    return 4*sum
