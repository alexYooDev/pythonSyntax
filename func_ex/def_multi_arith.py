def operator(a, b):
  add_var = a+b
  sub_var = a-b
  multi_var = a*b
  div_var = a/b
  return add_var,sub_var,multi_var,div_var

a,b,c,d = operator(7,3)
print(a,b,c,d)