def removeElement(nums,val):
  '''
  A function that removes elements equal to 'val' in the array nums in-place,
  and returns the resulting array.
  Time complexity: O(len(nums)).
  Space complexity: O(1).
  '''
  
  i,j=0,len(nums)-1
  while i<=j:
      if nums[i]==val:
          tmp=nums[i]
          nums[i]=nums[j]
          nums[j]=tmp
          j-=1
      elif nums[i]!=val:
          i+=1
  return len(nums)-(len(nums)-1-j)
