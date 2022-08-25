def addStrings(num1,num2):
  '''
  A function that takes two integer strings num1 and num2, and returns
  the corresponding string sum, without converting strings to integers
  and vice versa.
  Time complexity: O(max(len(num1),len(num2)N)), where N is the number
  of iterations it takes before n terminates to zero in the while loop.
  Space complexity: O(1), since the hashmaps have constant size.
  '''
  
  str_int={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
  int_str={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
  n1=0
  for i in range(len(num1)):
      n1+=str_int[num1[i]]*10**(len(num1)-i-1)
  n2=0
  for i in range(len(num2)):
      n2+=str_int[num2[i]]*10**(len(num2)-i-1)
  n=n1+n2
  if n==0:
      return '0'
  reverse=''
  while n>0:
      digit=n%10
      reverse+=int_str[digit]
      n=n//10
  result=''
  for i in range(len(reverse)):
      result+=reverse[len(reverse)-i-1]
  return result
