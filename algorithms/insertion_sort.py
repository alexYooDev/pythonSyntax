arr = [7,4,5,0,6,1,3,2]

for i in range(1, len(arr)):
  for j in range(i, 0, -1):
    if arr[j] < arr[j-1]:
      arr[j], arr[j-1] = arr[j-1],arr[j]
    else:
      break
print(arr)