def countingSort(arr):
  '''
  A function that takes as input an array of integers and returns a frequency
  array for how many times the number 0-99 appear in arr. The index of the 
  frequency array corresponds to the number it is counting.
  Time complexity: O(
  '''
  
  result=[0 for _ in range(100)]
  for i in range(len(arr)):
      result[arr[i]]+=1
  return result
