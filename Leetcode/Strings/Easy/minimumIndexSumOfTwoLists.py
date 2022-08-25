def findRestaurant(list1,list2):
  '''
  Given two lists of restaurant names, return the list of common restaurants
  with the minimum index sum.
  Time complexity: O(max(len(list1),len(list2)).
  Space complexity: O(len(list1)).
  '''
  
  hashmap={}
  for i in range(len(list1)):
      hashmap[list1[i]]=i
  total=len(list1)+len(list2)
  restaurants=[]
  for i in range(len(list2)):
      if list2[i] in andy and i+andy[list2[i]]<total:
          total=i+andy[list2[i]]
  for i in range(len(list2)):
      if list2[i] in andy and i+andy[list2[i]]==total:
          restaurants.append(list2[i])
  return restaurants
