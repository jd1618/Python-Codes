def singleNumber(nums):
  '''
  A function that takes an array nums, consisting of only one unique integer,
  and returns the unqiue integer in order n time and constant space.
  '''
  
  if len(nums)==1:
      return nums[0]
  unique=set()
  for num in nums:
      if num not in unique:
          unique.add(num)
      elif num in unique:
          unique.remove(num)
  for num in unique:
      return num
