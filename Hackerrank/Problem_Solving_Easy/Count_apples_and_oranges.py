def countApplesAndOranges(s,t,a,b,apples,oranges):
  '''
  A function to presents you with the width of a house [s,t], and apple and orange
  tree positions, a and b. The entries in apples and oranges refer to the distance 
  an apple and orange fall relative to their position (positive means movement to 
  the right, and negative means movement to the left). Return the number of apples
  and oranges that fall on the house.
  Time complexity: O(len(apples)).
  Space complexity: O(1).
  '''
  
  count_apples,count_oranges = 0, 0
  for i in range(len(apples)):
      apples[i]+=a
      if apples[i]>=s and apples[i]<=t:
          count_apples+=1
  for i in range(len(oranges)):
      oranges[i]+=b
      if oranges[i]>=s and oranges[i]<=t:
          count_oranges+=1
  return count_apples,count_oranges
