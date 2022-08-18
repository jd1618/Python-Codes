def breakingRecords(scores):
  '''
  A function that takes as input an array of scores a player gets in a game and 
  counts how many times they achieve a new highest score and how many times they
  achieve a new lowest score. 
  Time complexity: O(len(scores)).
  Space complexity: O(1).
  '''
  
  min_score,max_score=scores[0],scores[0]
  min_count,max_count=0,0
  for i in range(1,len(scores)):
      if min_score>scores[i]:
          min_score=scores[i]
          min_count+=1
      elif max_score<scores[i]:
          max_score=scores[i]
          max_count+=1
  return [max_count,min_count]
