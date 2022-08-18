def plusMinus(arr):
  '''
  A function that takes an array as input and prints out the ratio of positive, 
  negative and zero elements, respectively.
  Time complexity: O(len(arr)).
  Space complexity: O(1).
  '''
  
  pos,neg,zer=0,0,0
  for num in arr:
      if num>0:
          pos+=1
      elif num<0:
          neg+=1
      else:
          zer+=1
  for num in [pos,neg,zer]:
      num=format(num/len(arr),'.6f')
      print(num)
