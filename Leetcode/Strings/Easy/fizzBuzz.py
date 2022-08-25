def fizzBuzz(n):
  '''
  A function that iterates through numbers 1 to n and appends to an
  array different elements depends on the conditions the number 
  satisfies.
  Time complexity: O(n).
  Space complexity: O(n).
  '''
  
  answer=[]
  for i in range(1,n+1):
      if i%3==0 and i%5==0:
          answer.append("FizzBuzz")
      elif i%3==0:
          answer.append("Fizz")
      elif i%5==0:
          answer.append("Buzz")
      else:
          answer.append(str(i))
  return answer
