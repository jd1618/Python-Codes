def gradingStudents(grades):
  '''
  A function that takes as input a list of grades, and returns a list of grades that 
  are rounded if the difference with the next multiple of 5 is less than 3, and is 
  not rounded at all if the grade is less than 38.
  Time complexity: O(len(grades)).
  Space complexity: O(1).
  '''
  
  for i in range(len(grades)):
      diff=5-grades[i]%5
      if grades[i]>=38 and diff<3:
          grades[i]+=diff
  return grades
