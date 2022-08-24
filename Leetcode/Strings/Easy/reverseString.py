def reverseString(s):
  """
  A function that reverses an input string s in-place.
  Time complexity: O(len(s)).
  Space complexity: O(1).
  """
  i,j=0,len(s)-1
  while i<=j:
      tmp=s[i]
      s[i]=s[j]
      s[j]=tmp
      i+=1
      j-=1
  return s
