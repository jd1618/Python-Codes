def spiralOrder(matrix):
  '''
  A function that takes as input a list of lists (a matrix), and 
  returns an array consisting of the elemnts of the matrix in 
  spiral order.
  Time complexity: O(M*N), where M and N are the number of rows
  and columns of the matrix, respectively.
  Space complexity: O(M*N).
  '''
  
  rows,cols=len(matrix),len(matrix[0])         # <--- initialising lengths of dimensions
  i,j,k,counter,spiral=0,0,0,0,[]              # <--- initialising pointers and solution
  while counter<rows*cols:                     # <--- iterates through every element of the matrix
      spiral.append(matrix[i][j])              # <--- add the current element to the spiral array
      if j<cols-1-k and i==k:                  
          j+=1
      elif j==cols-1-k and i<rows-1-k:
          i+=1
      elif i==rows-1-k and j>k:
          j-=1
      elif j==k and i>k:
          i-=1
          if j==k and i==k:                    # <--- Repeat after one full loop of the outer matrix with k=k+1
              k+=1
              i,j=k,k
      counter+=1
  return spiral 
