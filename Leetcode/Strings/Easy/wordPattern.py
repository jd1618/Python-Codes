def wordPattern(pattern,s):
  '''
  A function that takes a pattern, e.g., 'abba', and returns if the string s
  obeys this pattern, i.e., for every word in s there is a one-one mapping 
  between a letter in pattern and a word in s. 
  Time complexity: O(len(pattern)).
  Space complexity: O(len(words)).
  '''
  
  hashmap={}
  words=s.split()
  if len(pattern)!=len(words):
      return False
  for i in range(len(pattern)):
      if pattern[i] not in hashmap and words[i] not in hashmap.values():
          hashmap[pattern[i]]=words[i]
      elif pattern[i] not in hashmap and words[i] in hashmap.values():
          return False
      elif pattern[i] in hashmap and words[i]!=hashmap[pattern[i]]:
          return False
  return True
