def countingValleys(path):
  '''
  A function that takes a list consisting of the elements 'D' and 'U' as input.
  A valley is defined as a path that goes from below sea level to above sea level.
  Assume the path begins at sea level, and that 'D' refers to moving down 1 unit 
  and 'U' refers to moving up one unit. The output is the number of valleys
  encountered traversing a particular path.
  Time complexity: O(len(path)).
  Space complexity: O(1).
  '''
  
   number_of_valleys=0
   level=0
   for entry in path:
      if level==-1 and entry=='U':
          number_of_valleys+=1
          level+=1
      elif entry=='D':
          level-=1
      elif entry=='U':
          level+=1
   return number_of_valleys
