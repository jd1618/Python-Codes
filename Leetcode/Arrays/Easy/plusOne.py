def plusOne(digits):
  '''
  A function that takes as input an array 'digits', consisting of 
  integer elements corresponding to a large integer, and adds 1 to the 
  large integer and returns the result as a array of digits.
  Time complexity: O(len(digits)).
  Space complexity: O(len(digits)).
  '''
  
  num=0
  for i in range(len(digits)):
      num+=digits[i]*10**(len(digits)-1-i)
  num+=1
  result=[]
  while num>0:
      digit=num%10
      result.append(digit)
      num=num//10
  return result[::-1]
