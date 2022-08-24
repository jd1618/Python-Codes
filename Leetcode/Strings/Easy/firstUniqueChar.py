def firstUniqChar(s):
  '''
  A function that takes a string s as input and returns the index
  of the first unique character, and returns -1 if not unqiue
  character exists.
  Time complexity: O(len(s)).
  Space complexity: O(len(s)).
  '''
  
  hashmap={}
  for i in range(len(s)):
      if s[i] not in hashmap:
          hashmap[s[i]]=i
      else:
          hashmap[s[i]]=-1
  for letter in s:
      if hashmap[letter]>=0:
          return hashmap[letter]
  return -1
