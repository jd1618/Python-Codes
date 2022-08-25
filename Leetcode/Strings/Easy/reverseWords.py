def reverseWords(s):
  '''
  A function that reverse every word in separated by whitespace in 
  the string s.
  Time complexity: O(len(s)).
  Space complexity: O(len(s)).
  '''
  
  words=s.split()
  result=''
  for word in words:
      result+=word[::-1]+' '
  return result[:len(s)]
