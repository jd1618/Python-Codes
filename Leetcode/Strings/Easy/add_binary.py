def addBinary(a,b):
  '''
  A function that takes two binary strings, a and b, and returns the binary sum as a string.
  '''
  
  inta,intb=0,0
  for i in range(len(a)):
      if a[i]=='1':
          inta+=2**(len(a)-i-1)
  for i in range(len(b)):
      if b[i]=='1':
          intb+=2**(len(b)-i-1)
  total=inta+intb
  if total==0:
      return '0'
  bstr=''
  while total!=0:
      digit=total%2
      bstr+=str(digit)
      total=total//2
  return bstr[::-1]
