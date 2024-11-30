from collections import defaultdict


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
          visited = defaultdict(bool) # fill dictionary with False (False is def value for bool in Python)
          DFS.dfs_rec(graph, visited, current)