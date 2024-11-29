class DFS:
     def __init__(self) -> None:
          pass

     def dfs_rec(graph, visited, current):
          visited[current] = True

          print(current, end=" ")

          for i in graph[current]:
               if not visited[i]:
                    DFS.dfs_rec(graph, visited, i)
     
     def dfs(graph, current):
          visited = [False] * len(graph)
          DFS.dfs_rec(graph, visited, current)