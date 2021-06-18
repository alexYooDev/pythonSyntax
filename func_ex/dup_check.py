
def solution(arr):

  temp = {}
  answer = []
  i = 0
  
  for i in arr:
    if arr.count(i) > 1:
      temp[i] = arr.count(i)
      answer = list(temp.values())

  if arr.count(i) <= 1 or len(arr) == 0:
    answer.append(-1)
    if len(answer) > 1:
      answer.remove(-1)

  return answer

print(solution([3,2,4,4,2,5,2,5,5]))