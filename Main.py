from collections import defaultdict
from Graph import Graph
from DFS import DFS
from Grid import Grid

if __name__ == "__main__":
     # vertices = 5
     graph = defaultdict(list)

     # edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

     # for e in edges:
     #      Graph.add_edge(graph, e[0], e[1])

     

     grid_graph = Grid.create_grid_graph(graph, 3, 3)

     for cell, neighbors in grid_graph.items():
          print(f"{cell}: {neighbors}")

     source = (0, 0)
     print("DFS from source:", source)
     DFS.dfs(grid_graph, source)