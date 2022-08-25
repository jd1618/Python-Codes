def majorityElement(nums):
  '''
  A function that returns the majority element in an array nums, 
  i.e., the element that appears more than n//2 times. We can 
  assume there is always a solution.
  Time complexity: O(len(nums)).
  Space complexity: O(len(nums)).
  '''
  
  freq={}
  for num in nums:
      if num not in freq:
          freq[num]=1
      else:
          freq[num]+=1
  for num in nums:
      if freq[num]>len(nums)//2:
          return num
