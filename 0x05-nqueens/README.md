## 0x05-nqueens

### Summary

The N queens puzzle involves placing N non-attacking queens on an N×N chessboard. The task is to write a program that solves this problem.

**Usage:** `nqueens N`

- If the wrong number of arguments is provided, print `Usage: nqueens N` and exit with status 1.
- N must be an integer greater than or equal to 4.
  - If N is not an integer, print `N must be a number` and exit with status 1.
  - If N is less than 4, print `N must be at least 4` and exit with status 1.

The program should print every possible solution, one per line, without a specific order. Only the `sys` module is allowed for import.

**References:**

- [Queen (chess)](<https://en.wikipedia.org/wiki/Queen_(chess)>)
- [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
