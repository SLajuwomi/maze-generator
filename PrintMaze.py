# Constants
MARK = "@"

class PrintMaze:
     def __init__(self) -> None:
          pass

     def printMaze(graph, height, width, markX=None, markY=None):
          for col in range(height):
               for row in range(width):
                    if markX == row and markY == col:
                         print(MARK, end="")
                    else:
                         print(graph[(row, col)], end="")
          print()


