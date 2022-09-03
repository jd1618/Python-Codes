def isIsomorphic(s,t):
  '''
  A function that returns whether the strings s and t are isomorphic, i.e., 
  there is a one-one mapping between the letters in s and the letters in t.
  Time complexity: O(max(len(s),len(t)).
  Space complexity: O(len(s)).
  '''
  
  hashmap={}
  if len(s)!=len(t):
      return False
  for i in range(len(s)):
      if s[i] not in hashmap and t[i] not in hashmap.values():
          hashmap[s[i]]=t[i]
      elif ((s[i] not in hashmap and t[i] in hashmap.values())
      or (s[i] in hashmap and t[i]!=hashmap[s[i]])):
          return False
  return True
