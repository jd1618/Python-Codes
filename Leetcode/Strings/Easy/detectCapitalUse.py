def detectCapitalUse(s):
  '''
  A function that returns whether a string s obeys the correct use of 
  capital letters or not, i.e., fully upper case or fully lower case, 
  or only the first letter is upper case.
  Time complexity: O(len(word)).
  Space complexity: O(1).
  '''
  
  if word==word.upper() or word==word.lower():
      return True
  if word[0]==word[0].upper() and word[1:]==word[1:].lower():
      return True
  return False
