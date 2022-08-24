def isAnagram(s,t):
  '''
  A function that considers a string s and returns whether the string
  t is an anagram of s or not.
  Time complexity: O(max(len(s),len(t)).
  Space complexity: O(len(s)).
  '''
  
  hashmap={}
  if len(s)!=len(t):
      return False
  for letter in s:
      if letter not in hashmap:
          hashmap[letter]=1
      else:
          hashmap[letter]+=1
  for letter in t:
      if ((letter in hashmap and hashmap[letter]==0) 
          or (letter not in hashmap)):
          return False
      hashmap[letter]-=1
  return True
