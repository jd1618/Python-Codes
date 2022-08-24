def lengthOfLastWord(s):
  '''
  Returns the length of the last word in the string s, disregarding blankspace, and 
  returns -1, otherwise.
  Time complexity: O(len(s)).
  Space complexity: O(1).
  '''
  
  count,i=0,0
  while i<len(s):
      if s[len(s)-i-1]==' ' and count!=0:
          break
      elif s[len(s)-i-1]!=' ':
          count+=1
      i+=1
  return count
