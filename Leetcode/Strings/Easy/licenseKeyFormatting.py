def licenseKeyFormatting(s,k):
  '''
  A function that takes a license key string s and reformats it
  s.t., all groups of characters in the license key are of length k, 
  except maybe the first group, and all groups are separated by 
  dashes.
  Time complexity: O(len(s)).
  Space complexity: O(len(s)).
  '''
  
  dummy=''
  for char in s:
      if char!='-':
          dummy+=char.upper()
  if k>=len(dummy):
      return dummy
  length1=len(dummy)%k 
  groups,counter='',0
  for i in range(length1,len(dummy)):
      if counter!=k:
          groups+=dummy[i]
          counter+=1
      else:
          groups+='-'+dummy[i]
          counter=1
  if length1==0:
      return groups
  else:
      return dummy[:length1]+'-'+groups
