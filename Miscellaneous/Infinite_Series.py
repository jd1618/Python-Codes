# Example of function composition to generate an infinite series approximation:

def frac_sum(x):
    return 1 + 1/x

def inf_sum(num):                                   # <--- num is the number of iterations
   # sum = 1 + 1/(1 + 1/(1 + 1/(1 + ...)))
    x = frac_sum(1)
    if num == 0:
        return float(1)
    elif num == 1:
        return x
    while num > 1:
        x = frac_sum(x)
        num -= 1
    return x

inf_sum(100)                                        # <--- converges to the golden ratio 1.618... 
