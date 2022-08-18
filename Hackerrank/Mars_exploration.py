def marsExploration(s):
  '''
  A function that takes as input a string that is compared with a string of equal
  length that is a substring of an infinite string 'SOS'. The function returns the 
  number of characters that are changed from the infinite 'SOS' string.
  Time complexity: O(len(s)).
  Space complexity: O(1).
  '''
  
  code='SOS'
  i=0
  count=0
  for char in s:
      if char!=code[i]:
          count+=1
      i+=1
      if i==len(code):
          i=0
  return count
