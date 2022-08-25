def moveZeroes(nums):
  """
  Do not return anything, modify nums in-place instead.
  """
  i=0
  for j in range(i,len(nums)):
      if nums[i]==0 and nums[j]!=0:
          tmp=nums[i]
          nums[i]=nums[j]
          nums[j]=tmp
          i+=1
      elif nums[i]!=0:
          i+=1
