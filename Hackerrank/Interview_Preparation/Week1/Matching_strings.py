def matchingStrings(strings,queries):
  '''
  A function that takes two lists of strings as input, and checks to see how many occurences 
  of an string in queries appear in strings. The output is a list of occurences, positioned
  to correspond to how the string appears in the queries list.
  Time complexity: O(len(strings)).
  Space complexity: O(max(len(string_count),len(results)).
  '''
  
  string_count={}
  results=[]
  for string in strings:
      if string not in string_count:
          string_count[string]=1
      else:
          string_count[string]+=1
      print(string_count)
  for query in queries:
      if query not in string_count:
          results.append(0)
      else:
          results.append(string_count[query])
  return results
