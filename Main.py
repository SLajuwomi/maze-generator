from Graph import Graph
from DFS import DFS

if __name__ == "__main__":
     vertices = 5
     graph = [[] for _ in range(vertices)]

     edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

     for e in edges:
          Graph.add_edge(graph, e[0], e[1])

     source = 1
     print("DFS from source:", source)
     DFS.dfs(graph, source)