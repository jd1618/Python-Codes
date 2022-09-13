def isMatch(p1,p2):
  if p1=='(' and p2==')' or p1=='[' and p2==']' or p1=='{' and p2=='}':
      return True
  return False

def isValid(s):
  if len(s)%2!=0:
      return False
  stack=[]
  for bracket in s:
      if bracket in '([{':
          stack.append(bracket)
      elif bracket in ')]}' and stack==[]:
          return False
      elif bracket in ')]}' and stack!=[]:
          if isMatch(stack[-1],bracket):
              stack.pop()
          else:
              return False
  return stack==[]
