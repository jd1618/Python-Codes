# Codewars Loose Change (6kyu):

import time

tests = int(input('Number of test cases: '))
N = [int(input('Test case ' + str(i + 1) + ': ')) \
               for i in range(tests)]

start = time.time()

def loose_change(num):
    if type(num) == float:
        num = int(num)
    if num <= 0:
        return {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0}
    Pennies, Nickels, Dimes, Quarters = 1, 5, 10, 25
    total = 0
    for a in range(num//25 + 1):
        for b in range((num - a*Quarters)//10 + 1):
            for c in range((num - a*Quarters - b*Dimes)//5 + 1):
                for d in range((num - a*Quarters - b*Dimes - c*Nickels)//1 + 1):
                    if a + b + c + d <= total:
                        continue
                    elif a + b + c + d > total:
                        total = a + b + c + d                    
    my_dict = {"Nickels": c, "Pennies": d, \
               "Dimes": b, "Quarters": a}
    return my_dict

for num in N:
    print(loose_change(num))
    
end = time.time()
print(end - start)
