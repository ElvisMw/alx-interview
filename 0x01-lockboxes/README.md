# Lockboxes
## Project Description
This project aims to solve the Lockboxes problem, which involves determining whether all boxes can be opened given that each box may contain keys to other boxes.

## Task Description
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1, and each box may contain keys to the other boxes. Write a method that determines if all the boxes can be opened.
```
- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
     * There can be keys that do not have boxes
- The first box boxes[0] is unlocked
-   Return True if all boxes can be opened, else return False
```

### main.py
```
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```
### When you Run: `./main_0.py` <br>
```
True
True
False
```

To successfully solve this project, you will need a solid understanding of the following concepts:

<l><li>Lists and List Manipulation
<l><li>Graph Theory Basics (e.g., BFS, DFS)
<l><li>Algorithmic Complexity (Big O Notation)
<l><li>Recursion
<l><li>Queue and Stack
<l><li>Set Operations
<l><li>Additional Resources
<l><li>Python Official Documentation
<l><li>Graph Theory
<l><li>Big O Notation
<l><li>Recursion in Python
<l><li>Python Queue and Stack
<l><li>Python Sets