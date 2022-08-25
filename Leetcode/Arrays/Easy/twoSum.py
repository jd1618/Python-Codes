def twoSum(nums,target):
  '''
  A function that takes as input an array of integers, 'nums', and 
  returns the pair of indices of the distinct index entries that
  sum to the integer 'target'. We assume there is always a solution!
  Time complexity: O(len(nums)).
  Space complexity: O(len(nums)).
  '''
  
  index_mapping={}
  for i in range(len(nums)):
      index_mapping[nums[i]]=i
  for i in range(len(nums)):
      pair=target-nums[i]
      if pair in index_mapping and index_mapping[pair]!=i:
          return [i,index_mapping[pair]]
