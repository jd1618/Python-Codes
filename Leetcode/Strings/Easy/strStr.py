def strStr(haystack,needle):
  '''
  A function that returns the first index of the occurence of the string needle in
  the string haystack, and returns -1, otherwise.
  Time complexity: O(len(haystack)), as at worst we iterate through each character 
  of haystack.
  Space complexity: O(1), since not external storage is used.
  '''
  
  start,end=0,len(needle)
  while end<=len(haystack):
      if haystack[start:end]==needle:
          return start
      start+=1
      end+=1
  return -1
