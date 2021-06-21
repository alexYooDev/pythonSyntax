# n*m 크기의 미로
# 현재 위치 (1,1)
# 출구 위치 (n,m) , 한번에 한 칸씩 이동
# 괴물 있는 곳 : 0 , 없는 곳 : 1
# 탈출하기 위해 움직여야 하는 최소 칸 개수
from collections import deque

def bfs(x,y):
  #queue 자료구조를 구현
  queue = deque()
  #현재 위치를 저장
  queue.append((x,y))

  #queue가 빌때가지
  while queue:
    #queue에 저장된 원소를 꺼냄
    x,y = queue.popleft()

    #다음 이동할 4가지 방향으로의 위치
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

    # 다음 이동 경로가 미로를 벗어날 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      
      #괴물이 있는 경로 무시
      if prison[nx][ny] == 0:
        continue
      
      #다음 이동경로가 방문하지 않은 길이라면 최단 거리를 기록
      if prison[nx][ny] == 1:
        prison[nx][ny] = prison[x][y]+1
        queue.append((nx,ny))

  #오른쪽 아래 까지의 최단 거리를 반환한다.
  return prison[n-1][m-1]



n,m = map(int, input().split())

prison = []
for i in range(n):
  prison.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))





