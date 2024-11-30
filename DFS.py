from collections import defaultdict
from PrintMaze import PrintMaze
import random

EMPTY = " "
WALL = chr(9608) # Character 9608 is '█'
NORTH, SOUTH, EAST, WEST = "n", "s", "e", "w"
WIDTH = 39
HEIGHT = 19

class DFS:
     def __init__(self) -> None:
          pass

     def visit(maze, row, col):
          maze[(row, col)] = EMPTY
          PrintMaze.printMaze(maze, row, col)


     # def dfs_rec(graph, visited, current):
     #      visited[current] = True

     #      print(current, end=" ")

     #      neighbors = graph[current][:]
     #      random.shuffle(neighbors)

     #      for i in neighbors:
     #           if not visited[i]:
     #                DFS.dfs_rec(graph, visited, i)

     #      # for i in graph[current]:
     #      #      if not visited[i]:
     #      #           DFS.dfs_rec(graph, visited, i)
     
     # def dfs(graph, current):
     #      visited = defaultdict(bool) # fill dictionary with False (False is def value for bool in Python)
     #      DFS.dfs_rec(graph, visited, current)

     def dfs_rec(graph, visited, maze, current):
          visited[current] = True
          maze[current] = EMPTY  # Mark current cell as path
          PrintMaze.printMaze(maze, HEIGHT, WIDTH)  # Display progress
          
          neighbors = graph[current][:]
          random.shuffle(neighbors)
          
          for neighbor in neighbors:
               if not visited[neighbor]:
                    DFS.dfs_rec(graph, visited, maze, neighbor)

     def dfs(graph, current):
          visited = defaultdict(bool)
          maze = defaultdict(lambda: WALL)  # Initialize maze with walls
          DFS.dfs_rec(graph, visited, maze, current)
          return maze    