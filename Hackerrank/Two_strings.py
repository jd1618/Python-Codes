def twoStrings(s1,s2):
  '''
  A function that takes two strings as input and identifies if they share a common substring,
  i.e., a substring may be as small as one character.
  Time complexity: O(max(len(s1),len(s2))).
  Space complexity: O(len(s1)).
  '''
  
  letters_in_s1={}
  for letter in s1:
      if letter not in letters_in_s1:
          letters_in_s1[letter]=1
      else:
          letters_in_s1[letter]+=1
  for letter in s2:
      if letter in letters_in_s1:
          return 'YES'
  return 'NO'
