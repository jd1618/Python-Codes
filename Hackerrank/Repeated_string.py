def repeatedString(s,n):
  '''
  A function that takes a string s and an integer n as inputs. Consider the first 
  n elements of the infinite string s+s+s+..., and identify the number of times 
  the letter 'a' occurs in this section of the inifinite string. An iterative 
  process is not desirable for n>10^6.
  Time complexity: O(len(s)).
  Space complexity: O(1).
  '''
  
  if n<len(s):
      s=s[:n]
  count=0
  for letter in s:
      if letter=='a':
          count+=1
  number_of_full_strings=n//len(s)
  length_of_partial_string=n%len(s)
  count*=number_of_full_strings
  for letter in s[:length_of_partial_string]:
      if letter=='a':
          count+=1
  return count 
