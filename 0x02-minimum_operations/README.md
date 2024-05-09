# 0x02. Minimum Operations

## Algorithm
- **Language:** Python
- **Weight:** 1
- **Project Duration:** May 6, 2024 6:00 AM - May 10, 2024 6:00 AM
- **Checker Release:** May 7, 2024 6:00 AM
- **Auto Review:** Launched at the deadline

## Overview
This project requires understanding key algorithmic and mathematical concepts to efficiently calculate the minimum number of operations needed to achieve a given number of characters using only “Copy All” and “Paste” operations.

### Concepts Needed:
1. **Dynamic Programming:** Helps break down the problem into simpler subproblems and build up the solution.
   - [Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/dynamic-programming/)
2. **Prime Factorization:** Crucial for reducing the problem to finding the sum of the prime factors of the target number n.
   - [Prime Factorization (Khan Academy)](https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/v/prime-factorization)
3. **Code Optimization:** Optimizing code is essential for finding the most efficient solution.
   - [How to Optimize Python Code](https://realpython.com/python-optimization/)
4. **Greedy Algorithms:** Approach the problem by choosing the best option at each step.
   - [Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)
5. **Basic Python Programming:** Proficiency in Python, including loops, conditionals, and functions.
   - [Python Functions (Python Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

By studying these concepts and utilizing the provided resources, you will be equipped to tackle the “Minimum Operations” problem effectively, applying both mathematical reasoning and programming skills to find the most efficient solution.

## Additional Resources
- Mock Technical Interview

## Requirements
### General
- **Allowed Editors:** vi, vim, emacs
- **Platform:** Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Endings:** All files should end with a new line
- **First Line:** The first line of all files should be exactly `#!/usr/bin/python3`
- **README.md:** Mandatory at the root of the project folder
- **Documentation:** Code should be documented
- **PEP 8 Style:** Code should use the PEP 8 style (version 1.7.x)
- **Executable Files:** All files must be executable

## Tasks
### 0. Minimum Operations
- **Description:** Calculate the fewest number of operations needed to achieve a given number of characters in a text file using only “Copy All” and “Paste” operations.
- **Prototype:** `def minOperations(n)`
- **Returns:** Integer
- **Example:**
    ```python
    n = 9
    # Output: 6
    ```
    Explanation:
    H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
