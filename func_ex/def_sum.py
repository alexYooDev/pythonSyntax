a = [4,7,12]
b = [True, False, True]

answer = 0
plus_minus = []
result = []
    
for i in b:
    if i != True:
      plus_minus += "-"
    else: plus_minus += " "
            
for i in range(0, len(a)):
  arr = [plus_minus[i] + str(a[i])]
  result += list(map(int, arr))
answer = sum(result)
  