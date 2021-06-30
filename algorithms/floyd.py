
# 매개변수는 인접행렬 (w)
def floyd(w):
  # d를 인접행렬로 초기화
  d = w
  # n 인접행렬의 길이
  n = len(w)
  p = [[-1]* n for _ in range(n)]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if (d[i][j] >  d[i][k]+d[k][j]):
          d[i][j] = d[i][k] + d[k][j]
          p[i][j] = k

  return d,p

inf = 999

w = [
    [0,1,inf,1,5],
    [9,0,3,2,inf],
    [inf,inf,0,4,inf],
    [inf,inf,2,0,3],
    [3,inf,inf,inf,0]
  ]

d = floyd(w)
for i in range(len(d)):
  print(d[i])