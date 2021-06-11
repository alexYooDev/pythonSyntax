
def solution(arr):

  newList = {}
  answer = []
  i = 0

  for i in arr:
    if arr.count(i) > 1:
      newList[i] = arr.count(i)
      answer = list(newList.values())
      
  if arr.count(i) <= 1 or len(arr) == 0:
    answer.append(-1)

  return answer

print(solution([3,2,4,4,2,5,2,5,5]))