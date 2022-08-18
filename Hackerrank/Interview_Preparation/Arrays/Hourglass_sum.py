def hourglassSum(arr):
  '''
  A function that takes as input a 2d-array in the form of a list of lists, which is square.
  Return the maximum hourglass sum in the array.
  Time complexity: O(len(arr)^2).
  Space complexity: O(1).
  '''
  
  i,j=0,1
  max_sum=-63 # Initiate to the smallest possible hourglass sum!
  hourglass_sum=0
  while j<len(arr)-1 and i<len(arr)-2:
      new_sum=arr[i][j-1]+arr[i][j]+arr[i][j+1]+arr[i+1][j]
        +arr[i+2][j-1]+arr[i+2][j]+arr[i+2][j+1]
      if hourglass_sum>max_sum:
          max_sum=hourglass_sum
      j+=1
      if j==len(arr)-1 and i<len(arr)-2:
          i+=1
          j=1
      elif i==len(arr)-2:
          break 
    return max_sum
