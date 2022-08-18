def flippingBits(n):
  '''
  A function that takes a base 10 integer n, and converts it to a 32 bit binary form. 
  If the binary form does not consist of 32 digits, prepend 0s to the binary form so 
  it has 32 digits. Then, swap 0s and 1s in the binary form and convert the result to 
  the corresponding base 2 representation.
  Time complexity: O(len(binary_string)).
  Space complexity: O(len(binary_string)).
  '''
  
  binary_string=''
  flip_string=''
  argument=n
  while n>0:
      digit=n%2
      binary_string+=str(digit)
      n=n//2
  # If input is 0, the previous while loop will be skipped, so check if the original 
  # argument was 0 before proceeding!
  if argument==0:
      binary_string='0'
  while len(binary_string)<32:
      binary_string+='0'
  binary_string=binary_string[::-1]
  for string in binary_string:
      if string=='0':
          flip_string+='1'
      else:
          flip_string+='0'
  flip_int=0
  for i in range(len(flip_string)):
      if flip_string[i]=='1':
          flip_int+=2**(len(flip_string)-1-i)
  return flip_int
