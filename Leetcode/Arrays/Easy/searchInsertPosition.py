def searchInsert(nums,target):
  '''
  Given a sorted array nums, return the index position of target in nums, 
  or return where target would be.
  Time complexity: O(len(nums)*log(len(nums))).
  Space complexity: O(1).
  '''
  
  low,high=0,len(nums)-1
  if target<nums[low]:
      return low
  if target>nums[high]:
      return high+1
  while low<=high:
      mid=(low+high)//2
      num=nums[mid]
      if num==target:
          return mid
      if num<target:
          low=mid+1
          if nums[low]>target:
              return low
      elif num>target:
          high=mid-1
          if nums[high]<target:
              return high+1
