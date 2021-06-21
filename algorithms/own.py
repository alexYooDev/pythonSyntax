from collections import deque

def dfs(graph, v, visited):

  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:

    vs = queue.popleft()

    print(vs, end=' ')

    for i in graph[vs]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2,3,4,],
  [1,5,6],
  [1,7],
  [1,7,8],
  [2,6],
  [2,5],
  [3,4],
  [4]
]

visited = [False]*9

dfs(graph, 1, visited)
#bfs(graph, 1, visited)

