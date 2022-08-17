def jumpingOnClouds(c):
  '''
  A function that takes in a list of Os and 1s as input. We are allowed to iterate through the input list
  either 1 or 2 entries at a time, but are only allowed to stay at entries with a 1 assigned to them. 
  The outcome is the minimum number of iterations needed to traverse the input list (under the assumption
  there always exists a solution given the parameters of the problem).
  '''
  
  i,j=0,1
  count=0
  while i<len(c)-2:
      if (c[i]==0 and c[j]==1 and c[j+1]==0 or 
          c[i]==0 and c[j]==0 and c[j+1]==0):
          i+=2
      elif c[i]==0 and c[j]==0 and c[j+1]==1:
          i+=1
      j=i+1
      count+=1
  if i==len(c)-2 and c[j]==0:
      return count+1
  else:
      return count
