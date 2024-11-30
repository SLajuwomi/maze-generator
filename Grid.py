from Graph import Graph

# Constants
EMPTY = " "
WALL = chr(9608) # Character 9608 is '█'
NORTH, SOUTH, EAST, WEST = "n", "s", "e", "w"

class Grid:
     def __init__(self) -> None:
          pass

     def create_grid_graph(graph, rows, cols):
          # for row in range(rows):
          #      for col in range(cols):
          #           graph[(row, col)] = WALL

          for row in range(rows):
               for col in range(cols):
                    cell = (row, col)

                    if row > 0:
                         Graph.add_edge(graph, cell, (row-1, col))
                    if row < rows -1:
                         Graph.add_edge(graph, cell, (row+1, col))
                    if col > 0:
                         Graph.add_edge(graph, cell, (row, col-1))
                    if col < cols -1:
                         Graph.add_edge(graph, cell, (row, col+1))
          
          return graph