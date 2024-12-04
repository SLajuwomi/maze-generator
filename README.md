<<<<<<< HEAD
# Maze Generator

A Python-based maze generator that creates random mazes using a depth-first search algorithm.

## Description

This maze generator creates random perfect mazes (mazes with exactly one path between any two points) using the following approach:

1. Creates a grid where each cell is initially surrounded by walls
2. Uses a depth-first search algorithm to:
   - Randomly visit unvisited cells
   - Break down walls between visited cells
   - Create paths until all cells are visited
3. Automatically adds an entrance at the top-left and exit at the bottom-right

## Requirements

- Python 3.x

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run the program:
   When prompted:
   Enter the desired width of the maze
   Enter the desired height of the maze
   How It Works
   The program uses the following components:

MazeGenerator class: Main class that handles maze generation
Maze representation:
Uses ASCII characters (█) for walls
Empty spaces ( ) represent paths
The maze is twice the size of input dimensions to account for walls
Generation algorithm:
Starts from a random cell (or specified starting point)
Marks current cell as visited
Randomly chooses an unvisited neighbor
Removes the wall between current cell and chosen neighbor
Recursively repeats the process for the new cell
Backtracks when no unvisited neighbors are available
=======

# Maze Generator - ![Static Badge](https://img.shields.io/badge/python-3-black?logo=python&link=https%3A%2F%2Fwww.python.org%2Fdownloads%2F)

This program generates random mazes using a modified version of the depth-first search (DFS) algorithm. 

## TLDR

1.  Creates a grid, with each cell surrounded by walls.
2.  Uses the modified DFS algo to:
    -   Visit cells in a random order.
    -   Knock down walls between neighboring cells to carve paths.
    -   Continue until all cells have been visited.
3.  An entrance is automatically added at the top-left corner, and an exit is placed at the bottom-right.

## What You’ll Need

-   Python 3.x installed on your system.

## Running the Program

1.  Clone the repository:
    
    ```bash
    git clone <repository-url>
    
    ```
    
2.  Change into the project directory:
    
    ```bash
    cd <project-directory>
    
    ```
    
3.  Run the program:
    
    ```bash
    python maze.py
    
    ```
    
4.  Follow the prompts:
    -   Enter the width of the maze.
    -   Enter the height of the maze.

## How It Works

### Key Components

#### Maze Structure

-   Walls are represented using `█` characters.
-   Paths are empty spaces (  ).
-   To account for walls, the program doubles the size of the input dimensions when creating the maze grid.

#### Maze Generation Steps

1.  The program starts at a random cell (or a predefined starting point).
2.  It marks the current cell as visited.
3.  From the current cell, it selects a random unvisited neighbor.
4.  The wall between the current cell and the chosen neighbor is removed.
5.  The program recursively visits the neighbor.
6.  If there are no unvisited neighbors, it backtracks to the previous cell and continues the process until the entire grid is explored.

This backtracking ensures that every cell is connected, creating a perfect maze with no loops or isolated sections.

#### Note

This program cannot create grids with a width or height greater than 45. This is because the algorithm uses a recursive depth-first search (DFS) approach, which relies heavily on Python's recursion stack. By default, Python’s recursion limit is set to 1000 calls, and the depth of the recursion stack grows with the grid size. For larger grids, the number of recursive calls exceeds this limit, causing a `RecursionError`.

If you need to handle larger mazes, you can:

1.  Increase the recursion limit using:
	~~~python
	import sys
	sys.setrecursionlimit(new_limit)
	~~~

	   **Warning:** Raising the recursion limit can lead to memory issues or program crashes if the stack size becomes too large.
    
2.  Refactor the algorithm to use an iterative approach, which avoids recursion altogether by using an explicit stack data structure. This approach eliminates the dependency on Python’s recursion depth.
>>>>>>> f43055cc18f959e5aa079daf577f2761c440a10a
