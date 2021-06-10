a = 0

def func():
  global a
  a += 1

for i in range(10):
  func()

print(a)

arr = [1,2,3,4,5]
def function():
  arr.append(6)
  print(arr)

function()