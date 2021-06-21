def dfs(graph, v, visited):
  #현재 노드를 방문 처리할 문장
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
#스택자료구조와 관련있으나 재귀함수로 표현하면 직관적임

#각 노드가 연결된 다른 노드
graph = [
  [],
  [2,3,8],
  [1,7],
  [4,5],
  [3,5],
  [3,5],
  [7],
  [2,6,8],
  [1,7]
]

#각 노드가 방문된 여부
visited = [False]*9

dfs(graph, 1, visited)
