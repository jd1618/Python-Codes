def miniMaxSum(arr):
  '''
  A function that takes an array as input and prints out the minimum and maximum
  rolling sum in the array. 
  Time complexity: O(len(arr)).
  Space complexity: O(1).
  '''
  
  total=0
  for num in arr:
      total+=num
  for num in [max(arr),min(arr)]:
      print(total-num,end=' ')
