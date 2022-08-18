def timeConversion(s):
  '''
  A function that takes an input string that represents a time with units 
  AM or PM and converts it to 24 hour time.
  Time complexity: O(1).
  Space complexity: O(1).
  '''
  
  if ((s[len(s)-2:]=='AM' and s[:2]!='12') 
    or (s[len(s)-2:]=='PM' and s[:2]=='12')):
      return s[:len(s)-2]
  if s[len(s)-2:]=='AM' and s[:2]=='12':
      return '00'+s[2:len(s)-2]
  if s[len(s)-2:]=='PM' and s[:2]!='12':
      num=int(s[:2])+12
      return str(num)+s[2:len(s)-2]
