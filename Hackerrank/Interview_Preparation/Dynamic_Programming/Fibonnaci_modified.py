def fibonacciModified(t1,t2,n,memo={}):
  '''
  A function that uses a dynamic programming approach to calculate the nth term 
  in the modified Fibonnaci sequence, t_i+2=t_i+(t_i+1)^2, where t1 and t2 are 
  inputs of the function.
  Time complexity: O(n).
  Space complexity: O(n).
  '''
  
  if n in memo:
      return memo[n]
  if n==1:
      return t1
  if n==2:
      return t2
  memo[n]=dynamic(t1,t2,n-1,memo)**2
    +dynamic(t1,t2,n-2,memo)
  return memo[n]
