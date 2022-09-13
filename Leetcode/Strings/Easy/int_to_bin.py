def convert_int_to_bin(dec_num):
  stack=[]
  while dec_num!=0:
    remainder=dec_num%2
    stack.append(str(remainder))
    dec_num//=2
  bin_str=''
  for i in range(len(stack)):
    bin_str+=stack[len(stack.items)-1-i]
  return bin_str
