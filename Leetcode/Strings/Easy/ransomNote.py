def canConstruct(ransomNote,magazine):
  '''
  A function that checks to see if the letters in the string magazine can 
  construct the string ransomNote.
  Time complexity: O(len(magazine)).
  Space complexity: O(len(magazine)).
  '''
  
  hashmap={}
  for letter in magazine:
      if letter not in hashmap:
          hashmap[letter]=1
      else:
          hashmap[letter]+=1
  for letter in ransomNote:
      if ((letter not in hashmap) 
      or (letter in hashmap and hashmap[letter]==0)):
          return False
      if letter in hashmap and hashmap[letter]>0:
          hashmap[letter]-=1
  return True
