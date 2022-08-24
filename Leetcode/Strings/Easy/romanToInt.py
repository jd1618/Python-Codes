def romanToInt(s):
  '''
  A function that takes a roman numeral string and converts it to an integer.
  Time complexity: O(len(s)).
  Space complexity: O(1), since the space allocated to the numerals hashmap
  is constant and not dependent on the length of s.
  '''
  
  numerals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  i,result=0,1,0
  while i<len(s)-1:
      if s[i]=='I' and s[i+1]=='V':
          result+=4
          i+=2
      elif s[i]=='I' and s[i+1]=='X':
          result+=9
          i+=2
      elif s[i]=='X' and s[i+1]=='L':
          result+=40
          i+=2
      elif s[i]=='X' and s[i+1]=='C':
          result+=90
          i+=2
      elif s[i]=='C' and s[i+1]=='D':
          result+=400
          i+=2
      elif s[i]=='C' and s[i+1]=='M':
          result+=900
          i+=2
      else:
          result+=numerals[s[i]]
          i+=1
  if (s[len(s)-2:]=='IV' or s[len(s)-2:]=='IX' or s[len(s)-2:]=='XL' 
      or s[len(s)-2:]=='XC' or s[len(s)-2:]=='CD' or s[len(s)-2:]=='CM'):
      return result
  return result+numerals[s[i]]
