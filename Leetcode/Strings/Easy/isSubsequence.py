def isSubsequence(s,t):
  '''
  A function that returns whether the string s is a subsequence 
  of the string t.
  Time complexity: O(len(t)).
  Space complexity: O(1).
  '''
  
  if len(s)>len(t):
      return False
  i,j=0,0
  while i<len(s) and j<len(t):
      if s[i]==t[j]:
          i+=1
          j+=1
      elif s[i]!=t[j]:
          j+=1
  return i==len(s)
