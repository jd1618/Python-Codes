def containsNearbyDuplicate(nums,k):
  '''
  A function that returns True if there are two elements in nums 
  with distinct indices and the sum of the indices is less than
  or equal to k, and returns False otherwise.
  Time complexity: O(len(nums)).
  Space complexity: O(len(nums)).
  '''
  
  hashmap={}
  for i in range(len(nums)):
      if ((nums[i] not in hashmap) 
          or (nums[i] in hashmap 
              and abs(hashmap[nums[i]]-i)>k)):
          hashmap[nums[i]]=i
      else:
          return True 
  return False
