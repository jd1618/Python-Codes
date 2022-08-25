def checkRecord(s):
  '''
  A function that takes a string s, consisting of the characters 'A', 'L'
  and 'P', denoting absent, late and present, on a particular day, respectively.
  If consecutively late less than 3 times or absent less than 2 times, return 
  True, and return False, otherwise.
  Time complexity: O(len(s)).
  Space complexity: O(1).
  '''
  
  absent,late=0,0
  for i in range(len(s)):
      if s[i]=='A':
          absent+=1
          late=0
          if absent==2:
              return False
      elif s[i]=='L':
          late+=1
          if late==3:
              return False
      else:
          late=0
  return True
