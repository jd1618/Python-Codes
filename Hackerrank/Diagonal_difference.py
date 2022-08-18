def diagonalDifference(arr):
  '''
  A function that takes a matrix as input and calculates the absolute difference between the
  sum of both diagonals.
  Time complexity: O(len(arr)).
  Space complexity: O(1).
  '''
  
  left,right=0,0
  for i in range(len(arr)):
      left+=arr[i][i]
      right+=arr[i][len(arr)-1-i]
  return abs(left-right)
