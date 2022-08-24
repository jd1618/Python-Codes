def findTheDifference(s,t):
  '''
  A function that shuffles adds a random character to s and shuffles to generate
  the string t, and returns the newly added character.
  Time complexity: O(len(t)).
  Space complexity: O(len(s)).
  '''
  
  hashmap={}
  for letter in s:
      if letter not in hashmap:
          hashmap[letter]=1
      else:
          hashmap[letter]+=1
  for letter in t:
      if ((letter not in hashmap) or (letter in hashmap and hashmap[letter]==0)):
          return letter
      if (letter in hashmap and hashmap[letter]>0):
          hashmap[letter]-=1
