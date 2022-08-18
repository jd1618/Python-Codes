def pangrams(s):
  '''
  A function that takes as input a string s and returns 'pangram' if s consists of all
  letters of the alphabet, and returns 'not pangram', otherwise.
  Time complexity: O(len(s)).
  Space complexity: O(max(len(alpha),len(s)).
  '''
  
  alpha='abcdefghijklmnopqrstuvwxyz'
  table={}
  count=0
  for char in alpha:
      if char not in table:
          table[char]=1
  for char in s:
      if char.lower() in table and table[char.lower()]==1:
          count+=1
          table[char.lower()]-=1
  if count==len(alpha):
      return 'pangram'
  return 'not pangram'
