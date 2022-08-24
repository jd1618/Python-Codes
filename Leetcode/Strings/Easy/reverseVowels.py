def reverseVowels(s):
  '''
  A function that takes as input a string s and returns a string 
  corresponding to s, but with vowels reversed.
  Time complexity: O(len(s)).
  Space complexity: O(len(s)).
  '''
  
  vowels={'a','e','i','o','u'}
  letters=[]
  for char in s:
      letters.append(char)
  i,j=0,len(letters)-1
  while i<=j:
      if letters[i].lower() in vowels and letters[j].lower() in vowels:
          tmp=letters[i]
          letters[i]=letters[j]
          letters[j]=tmp
          i+=1
          j-=1
      elif letters[i].lower() in vowels and letters[j].lower() not in vowels:
          j-=1
      elif letters[i].lower() not in vowels and letters[j].lower() in vowels:
          i+=1
      else:
          i+=1
          j-=1
  result=''
  for letter in letters:
      result+=letter
  return result
