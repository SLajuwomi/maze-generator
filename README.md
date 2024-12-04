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
