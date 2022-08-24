def isPalindrome(s):
  '''
  A function that considers a string and returns whether it is a palindrome on
  removing all non-alphanumeric characters and comverting to lowercase.
  Time complexity: O(len(s)), since in the worst case the length of s
  can be much greater than the length of alpha, whereas the length of
  alpha is fixed in the code.
  Space complexity: O(len(forwards)), since the length of hashset is fixed,
  but the length of the strings is variable.
  '''
  
  alpha='abcdefghijklmnopqrstuvwxyz0123456789'
  hashset=set()
  for letter in alpha:
      hashset.add(letter)
  forwards,backwards='',''
  for i in range(len(s)):
      if s[i].lower() in hashset:
          forwards+=s[i].lower()
      if s[len(s)-i-1].lower() in hashset:
          backwards+=s[len(s)-i-1].lower()
  return forwards==backwards
