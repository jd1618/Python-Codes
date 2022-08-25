def containsDuplicate(nums):
  '''
  A function that takes an array nums as input and returns True if
  any of the values appear at least twice, and False otherwise.
  Time complexity: O(len(nums)).
  Space complexity: O(len(nums)).
  '''
  
  hashmap = {}
  for i in range(len(nums)):
      if nums[i] not in hashmap:
          hashmap[nums[i]] = 1
      else:
          hashmap[nums[i]] += 1
      if hashmap[nums[i]] >= 2:
          return True
  return False
