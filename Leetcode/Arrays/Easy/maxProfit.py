def maxProfit(prices):
  '''
  A function that takes as input an array of integers, where the elements
  corresponding to prices of a stock on a given day, and returns the 
  maximum profit you can make if you buy a stock on one day and sell it
  on a different day in the future.
  Time complexity: O(len(prices)).
  Space complexity: O(1).
  '''
  
  min_price,profit=prices[0],0
  for i in range(1,len(prices)):
    if prices[i]<min_price:
      min_price=prices[i]
    elif prices[i]-min_price>profit:
      profit=prices[i]-min_price
  return profit
