# 0x07. Rotate 2D Matrix

## Table of Contents

- [Introduction](#introduction)
- [Concepts Needed](#concepts-needed)
- [Resources](#resources)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Rotate 2D Matrix](#0-rotate-2d-matrix)

## Introduction

In this project, you will implement an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. This involves understanding matrix manipulation, in-place operations, and nested loops in Python.

## Concepts Needed

- Matrix Representation in Python
- In-place Operations
- Matrix Transposition
- Reversing Rows in a Matrix
- Nested Loops

## Resources

- Python Official Documentation
  - [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
  - [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- GeeksforGeeks Articles
  - [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
  - [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
- TutorialsPoint
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.html)

 - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

## Task

### 0. Rotate 2D Matrix

Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.

- Prototype: `def rotate_2d_matrix(matrix: List[List[int]]) -> None:`
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

**Example:**

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)


```Expected output
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

