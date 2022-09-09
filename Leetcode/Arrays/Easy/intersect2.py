def intersect2(nums1,nums2):
  hashmap={}
  for num in nums1:
      if num not in hashmap:
          hashmap[num]=1
      else:
          hashmap[num]+=1
  intersect=[]
  for num in nums2:
      if num in hashmap and hashmap[num]>=1:
          intersect.append(num)
          hashmap[num]-=1
  return intersect
