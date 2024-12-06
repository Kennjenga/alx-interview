# 0. Island Perimeter

## Project Overview

The "Island Perimeter" project involves calculating the perimeter of a single island within a grid. The grid is represented by a 2D array of integers, where `1` represents land and `0` represents water. The goal is to determine the perimeter by analyzing the grid and applying logical conditions to count the edges that form the perimeter of the island.

## Key Concepts

### 2D Arrays (Matrices)

- **Accessing and Iterating**: You need to access and iterate over elements in a 2D array. This involves using nested loops to traverse the grid.
- **Navigating Adjacent Cells**: Understanding how to move horizontally and vertically to adjacent cells is crucial for checking the perimeter conditions.

### Conditional Logic

- **Determining Perimeter Contribution**: Apply conditions to check if a cell contributes to the perimeter. A land cell (`1`) contributes to the perimeter if it is on the grid boundary or adjacent to a water cell (`0`).

### Counting Techniques

- **Counting Edges**: Develop a method to count the edges that contribute to the island’s perimeter. This involves checking each land cell and its neighbors.

### Problem-Solving Strategies

- **Breaking Down the Problem**: Identify land cells and calculate their contribution to the perimeter by breaking the problem into smaller tasks.

### Python Programming

- **Nested Loops**: Use nested loops to iterate over the grid cells.
- **Conditional Statements**: Use conditional statements to check the status of adjacent cells.

## Example

Consider the following grid:

```
[
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```

The perimeter of the island can be calculated as follows:

- The cell at (0,1) contributes 3 edges (top, left, right).
- The cell at (1,0) contributes 2 edges (top, left).
- The cell at (1,1) contributes 0 edges (all neighbors are land).
- The cell at (1,2) contributes 1 edge (right).
- The cell at (2,1) contributes 2 edges (bottom, left).
- The cell at (3,0) contributes 2 edges (bottom, left).
- The cell at (3,1) contributes 1 edge (bottom).

Total perimeter = 3 + 2 + 0 + 1 + 2 + 2 + 1 = 11

## Resources

- **Python Official Documentation**:
  - [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
- **GeeksforGeeks Articles**:
  - [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)
- **TutorialsPoint**:
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- **YouTube Tutorials**:
  - [Python 2D arrays and lists](https://www.youtube.com/results?search_query=python+2d+arrays+and+lists)

By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. This project tests your algorithmic thinking and reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.
