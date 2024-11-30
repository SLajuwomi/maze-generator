from Graph import Graph

class Grid:
     def __init__(self) -> None:
          pass

     def create_grid_graph(graph, rows, cols):
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