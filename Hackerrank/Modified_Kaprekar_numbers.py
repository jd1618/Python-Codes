def kaprekarNumbers(p,q):
  '''
  A function that generates a list of all Kaprekar numbers in the interval [p,q], if they exist.
  Kaprekar numbers of those that can be separated in half and summed together to obtain the original
  number, e.g., 9 is a Kaprekar number since 9^2=81 and 8+1=9.
  Time complexity of python code: O(q+1-p).
  Space complexity of python code: O(len(result)).
  '''
  
  result=[]
  for num in range(p,q+1):
    digits=len(str(num))
    square=str(num**2)
    
    # If a number has d digits, then the corresponding square has at most 2*d digits!
    # Proof: Let a=a0a1a2...an, where a0 is nonzero and 0<=ai<=9 for all i=0,1,2,...,n. 
    # Clearly, a=10^n*a0+10^(n-1)*a1+...+10^0*an. Thus, the square can be calculated as 
    # a^2=sum_{i=0}^n(10^(2*n-2*i)*ai^2)+2*sum_{i<j}^n(10^(2*n-i-j)*ai*aj)
    #    <=10^(2n)*(81*(1+1/100+1/10000+...+1/10^(2*n))+2*81*(1/10+1/1000+...+1/10^(2*n-1)))
    #    <=10^(2n)*(81*10/9+81/10+81/1000+...)<=10^(2*n)*100=10^(2*n+2)=10^(2*(n+1)).
    # The last line is derived using the formula for a geometric series, i.e., 
    # sum_{i=0}^n(1/10)^(2*i)=(10-(1/10)^(2*n))/9->10/9 as n tends to infinity.
    # In this case, d=n+1, so we have proven that the square has 2*d digits. 
    # Similar reasoning shows that a number with d digits has at least 2*d-1 digits.
    
    if len(square)==2*digits:
      left=square[:d]
      right=square[d:]
    elif len(square)==2*digits-1:
      left=square[:d-1]
      right=square[d-1:]
    if left=='':
      left+='0'
    if right=='':
      right+='0'
    if int(left)+int(right)==num:
      result.append(num)
  if len(result)==0:
      return 'INVALID RANGE'
  return result 
