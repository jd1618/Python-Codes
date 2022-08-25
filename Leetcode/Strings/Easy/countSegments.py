def countSegments(s):
  '''
  A function that returns the number of segments in the string s
  that are separated by whitespace.
  Time complexity: O(len(s)).
  Space complexity: O(1), though there is an easy solution using
  the split method that is O(len(s)) in space.
  '''
  
  count=0
  if s=='':
      return count
  for i in range(1,len(s)):
      if s[i]==' ' and s[i-1]!=' ':
          count+=1
  if s[len(s)-1]!=' ':
      count+=1
  return count 
