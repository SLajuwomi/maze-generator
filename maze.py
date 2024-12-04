import random

class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Fill each space in the maze with a wall
        # Double the width and height to account for the walls between cells
        # and add 1 to each dimension to account for the outer walls
        self.maze = [[chr(9608) for x in range(width * 2 + 1)] for y in range(height * 2 + 1)]
        self.visited = [[False for x in range(width)] for y in range(height)]
    
    def generate(self, start_x=None, start_y=None):
        # start_x and start_y are optional arguments that allow you to specify the starting point of the maze
        if start_x is None: # If no starting point is specified, choose a random one
            start_x = random.randint(0, self.width - 1)
        if start_y is None:
            start_y = random.randint(0, self.height - 1)
        
        self._dfs(start_x, start_y)
        
        # Create entrance and exit
        self.maze[1][0] = ' '  # entrance
        self.maze[self.height * 2 - 1][self.width * 2] = ' '  # exit
    
    def _dfs(self, x, y):
        self.visited[y][x] = True
        self.maze[y * 2 + 1][x * 2 + 1] = ' ' # clear current cell
        
        # Possible directions to move in (up, right, down, left)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions: # Visit each direction in random order
            new_x, new_y = x + dx, y + dy # new cell coordinates
            
            # Check if new cell is within bounds and hasn't been visited
            if (0 <= new_x < self.width and 
                0 <= new_y < self.height and 
                not self.visited[new_y][new_x]):
                
                # Remove wall between cells
                wall_x = x * 2 + 1 + dx
                wall_y = y * 2 + 1 + dy
                self.maze[wall_y][wall_x] = ' '
                
                # Recursively visit the next cell
                self._dfs(new_x, new_y)
    
    def print_maze(self):
        for row in self.maze:
            print(''.join(row))

if __name__ == "__main__":
    print("Maze starts in the top left corner and ends in the bottom right corner")
    print("Insert a width and height for the maze.")
    width = int(input("Width: "))
    height = int(input("Height: "))
    maze = MazeGenerator(width, height)  
    maze.generate()
    maze.print_maze()