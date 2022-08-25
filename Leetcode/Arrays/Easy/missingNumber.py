def missingNumber(nums):
  '''
  A function that takes an array of integers in [0,n], with a single integer missing,
  and returns the missing integer.
  Time complexity: O(len(nums)).
  Space complexity: O(len(nums)).
  '''
  
  n=len(nums)
  hashset=set()
  for num in nums:
      hashset.add(num)
  for num in range(n+1):
      if num not in hashset:
          return num 
