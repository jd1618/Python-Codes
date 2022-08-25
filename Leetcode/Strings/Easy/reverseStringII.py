def reverseStr(s,k):
  '''
  A function that takes a string s and reverse the first k elements
  of every segment of length 2k. If the remaining segment is less 
  than k in length, reverse the segment, and if the segment is greater
  than or equal to k but less than 2k in length, reverse the first k 
  elements and append the remaining elements as they are.
  Time complexity: O(len(s)**2).
  Space complexity: O(len(s)).
  '''
  
  if k>len(s):
      return s[::-1]
  if k<=len(s) and len(s)<2*k:
      head=s[:k]
      head=head[::-1]
      return head+s[k:]
  result,start='',0
  while start<=len(s)-(2*k-1) or start==0:
      dummy=s[start:start+k]
      result+=dummy[::-1]+s[start+k:start+2*k]
      start+=2*k
      if len(s[start:])<k:
          dummy=s[start:]
          return result+dummy[::-1]
      if len(s[start:])>=k and len(s[start:])<2*k:
          dummy=s[start:start+k]
          return result+dummy[::-1]+s[start+k:]
  return result
