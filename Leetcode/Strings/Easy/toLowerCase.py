def toLowerCase(s):
  '''
  Returns the string s as a lower case string, without the use of the 
  string method lower().
  Time complexity: O(len(s)).
  Space complexity: O(len(s)), since the lower and upper string, and 
  the hashmap are have constant memory space.
  '''
  
  lower='abcdefghijklmnopqrstuvwxyz'
  upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  hashmap={}
  for i in range(len(upper)):
      hashmap[upper[i]]=lower[i]
  result=''
  for i in range(len(s)):
      if s[i] in hashmap:
          result+=hashmap[s[i]]
      else:
          result+=s[i]
  return result 
