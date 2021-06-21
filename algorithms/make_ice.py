# n*m 크기의 얼음 틀이 있다. 구멍 뚤린 부분: 0, 막힌 부분 : 1
# 구멍 뚤린 부분끼리 상하좌우가 붙어있으면 연결된 것
# 얼음 틀의 모양이 주어졌을 때 생성되는 얼음의 개수 구하라
# 첫번째 입력 : 세로 길이와 가로 길이 ( 공백으로 구분)
# 두번째 줄부터 n+1번째 줄까지 얼음 틀의 형태 주어짐

def dfs(x,y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  
  if case[x][y] == 0:
    case[x][y] = 1

    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

n,m = map(int, input().split())

case = []
for i in range(n):
  case.append(list(map(int, input())))

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1

print(result)

