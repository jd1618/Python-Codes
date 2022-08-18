def lonelyinteger(a):
  '''
  A function, that given a list of integers as input, identifies the unique integer 
  in the list, assuming that only one unique solution exists.
  Time complexity: O(len(a)).
  Space complexity: O(len(int_count)).
  '''
  
  int_count={}
  for num in a:
      if num not in int_count:
          int_count[num]=1
      else:
          int_count[num]+=1
  for num in a:
      if int_count[num]==1:
          return num
