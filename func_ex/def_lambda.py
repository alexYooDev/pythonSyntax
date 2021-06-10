arr = [('jason', 28),('park', 40), ('ken', 45)]

def key_val(x):
  return x[1] #정렬 기준 값 설정 => 배열 안 튜플의 1번째 값

print(sorted(arr, key=key_val)) #배열, 정렬기준(함수)
print(sorted(arr, key=lambda x: x[1]))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

# lambda expression executing addition between the elements in each array in the same position
# map function checks each elements in the list and executes certain function
result = map(lambda a,b : a+b, list1, list2)  

#contain the result in a new list
print(list(result))