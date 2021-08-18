
# 매개변수를 2차원 배열 w로 받음

def prim(w):
  # 2차원 배열이 길이 -1 정점의 개수 (0인덱스 제외)
  n = len(w) -1 
  F = []
  nearest = [-1] * (n+1)
  distance = [-1] * (n+1)
  # 2부터 n까지 (첫번째 정점은 이미 방문처리)
  for i in range(2, n+1):
    nearest[i] = 1
    distance[i] = w[1][i]
  
  # 이미 첫번째 정점 V1을 방문했기 때문에
  for _ in range(n-1):
    # 최소값을 무한으로 초기화
    min_value = INF
    # 2에서 n까지
    for i in range(2, n+1):
      # 마이너스 값이 아니고 이미 방문된게 아니면
      if 0 <= distance[i] and distance[i] < min_value:
        min_value = distance[i]
        vnear = i
    edge = (nearest[vnear], vnear, w[nearest[vnear]][vnear])
    F.append(edge) # 간선을 F에 추가
    # 방문 처리 되었기 때문에 -1 할당
    distance[vnear] = -1
    for i in range(2, n+1):
      if distance[i] > w[i][vnear]:
        distance[i] = w[i][vnear]
        nearest[i] = vnear
    print_nd(F, nearest,distance)
  return F

def cost(F, w):
  total = 0
  for e in F:
    total += w[e[0]][e[1]]
  return total

def print_nd(F, nearest, distance):
  print('F = ', end='')
  print(F)
  print('nearest: ', end='')
  print(nearest)
  print('distance: ', end='')
  print(distance)

INF = 999

w = [
  [-1,-1,-1,-1,-1],
  [-1,0,1,3,INF,INF],
  [-1,1,0,3,6,INF],
  [-1,3,3,0,4,2,],
  [-1,INF,6,4,0,5],
  [-1,INF,INF,2,5,0],
]

F = prim(w)
for i in range(len(F)):
  print(F[i])

print("Mininum Cost is", cost(F,w))