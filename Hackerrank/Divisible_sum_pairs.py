def divisibleSumPairs(n,k,ar):
  '''
  A function that takes an array ar of length n as input, and returns the number of 
  integer pairs in the pair, (i,j), s.t., i<j and i+j=k.
  Time complexity: Let N=len(ar). Then O(N*log(N))+O(N^2)=O(N^2).
  Space complexity: O(1). 
  '''
  
  count=0
  ar.sort()
  for i in range(len(ar)):
      for j in range(i+1,len(ar)):
          if (ar[i]+ar[j])%k==0:
              count+=1  
  return count     
