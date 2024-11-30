from collections import defaultdict
from Graph import Graph
from DFS import DFS
from Grid import Grid
from PrintMaze import PrintMaze
import random

# Constants
WIDTH = 39
HEIGHT = 19
# Ensure grid dimensions are odd
assert WIDTH % 2 == 1 and WIDTH >= 3
assert HEIGHT % 2 == 1 and HEIGHT >= 3
# Reproduce the same maze given the same seed value
# SEED = 1
# random.seed(SEED)


if __name__ == "__main__":
     # vertices = 5
     graph = defaultdict(list)

     # edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

     # for e in edges:
     #      Graph.add_edge(graph, e[0], e[1])

     

     grid_graph = Grid.create_grid_graph(graph, WIDTH, HEIGHT)

     # for cell, neighbors in grid_graph.items():
     #      print(f"{cell}: {neighbors}")

     source = (0, 0)
     # print("DFS from source:", source)
     maze_grid = DFS.dfs(grid_graph, source)
     PrintMaze.printMaze(maze_grid, HEIGHT, WIDTH)