def sockMerchant(n,ar):
  '''
  A function that considers an array of socks of size n, with matching socks having 
  the same number allocated to them in the array. The output is the number of matching 
  pairs that can be made up.
  Time complexity: O(len(ar)).
  Space complexity: O(len(socks))=O(len(ar)), worst case.
  '''
  
  socks={}
  for num in ar:
      if num not in socks:
          socks[num]=1
      else:
          socks[num]+=1
  count=0
  for key,value in socks.items():
      count+=value//2
  return count
