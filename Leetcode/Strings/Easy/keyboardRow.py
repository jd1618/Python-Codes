def findWords(words):
  '''
  Given an array of strings in the list words, return an array consisting
  of elements of words that only use a single row on the keyboard to derive
  them.
  Time complexity: O(len(words)*N), where N is the maximum length of a string
  in the array words.
  Space complexity: O(len(words)).
  '''
  
  row1={'q','w','e','r','t','y','u','i','o','p'}
  row2={'a','s','d','f','g','h','j','k','l'}
  row3={'z','x','c','v','b','n','m'}
  row,length,result=0,0,[]
  for word in words:
      for letter in word:
          if row==0:
              if letter.lower() in row1:
                  row=1
              elif letter.lower() in row2:
                  row=2
              elif letter.lower() in row3:
                  row=3
              length+=1
          else:
              if ((letter.lower() in row1 and row==2) 
                  or (letter.lower() in row1 and row==3)):
                  row,length=0,0
                  break
              elif ((letter.lower() in row2 and row==1) 
                    or (letter.lower() in row2 and row==3)):
                  row,length=0,0
                  break
              elif ((letter.lower() in row3 and row==1) 
                    or (letter.lower() in row3 and row==2)):
                  row,length=0,0
                  break
              else:
                  length+=1
          if length==len(word):
              result.append(word)
              row,length=0,0
  return result
