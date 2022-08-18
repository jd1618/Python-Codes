def checkMagazine(magazine, note):
  '''
  A function that identifies if the string note can be constructed from the 
  characters in the string magazine.
  Time complexity: O(max(len(magazine),len(note)).
  Space complexity: O(len(magazine)).
  '''
  
  letters_in_magazine={}
  count=0
  for letter in magazine:
      if letter not in letters_in_magazine:
          letters_in_magazine[letter]=1
      else:
          letters_in_magazine[letter]+=1
  for letter in note:
      if letter in letters_in_magazine and 
      letters_in_magazine[letter]>=1:
          count+=1
          letters_in_magazine[letter]-=1
  if count==len(note):
      return 'Yes'
  return 'No'
