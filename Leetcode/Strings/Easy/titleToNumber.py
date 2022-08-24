def titleToNumber(columnTitle):
  '''
  A function that takes an excel column title in string format as input and 
  returns the number it corresponds to, i.e., the column position in the 
  spreadsheet.
  Time complexity: O(len(columnTitle)).
  Space complexity: O(1).
  '''
  
  alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  hashmap={}
  for i in range(len(alpha)):
      hashmap[alpha[i]]=i+1
  result=0
  for i in range(len(columnTitle)):
      result+=26**(len(columnTitle)-i-1)*hashmap[columnTitle[i]]
  return result
