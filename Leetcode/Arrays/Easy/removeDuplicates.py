def removeDuplicates(nums):
  '''
  Return an array that corresponds to the number of unique entries in 
  the array 'nums', by iterating in-place.
  Time complexity: O(len(nums)).
  Space complexity: O(1).
  '''
  
  i=0
  for j in range(1,len(nums)):
      if nums[i]!=nums[j]:
          i+=1
          nums[i]=nums[j]
  return i+1
