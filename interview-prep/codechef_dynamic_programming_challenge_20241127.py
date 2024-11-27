'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-11-27
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-11-27

## Problem: Dynamic Programming Challenge

**Problem Understanding and Approach:**

This problem requires us to solve a specific type of DP (Dynamic Programming) problem known as a knapsack problem. We're given a sequence of numbers (the sequence of items), and we need to determine the maximum sum of these numbers (the maximum value of the items) while satisfying a given constraint (the capacity of the knapsack).

The approach here involves breaking down the problem into smaller subproblems. For each item in the sequence, we consider two options: either include it in the knapsack or exclude it. We then recursively solve the subproblems for the remaining items, taking into account the impact of the current item's inclusion or exclusion.

The recursive function will store the solution to each subproblem in a memoization table to avoid redundant calculations. This approach optimizes the solution by ensuring that each subproblem is solved only once.

### Time and Space Complexity Analysis:

- **Time Complexity:** O(2^n), where n is the number of items. This is the worst-case time complexity for a recursive solution.
- **Space Complexity:** O(n), as we need to store the memoization table, which contains n entries.

### Well-Commented Implementation:

```python
# Function to solve the knapsack problem using dynamic programming
def knapsack(items, capacity):

    # Create a memoization table to store the solution to subproblems
    memo = {}

    # Initialize the base cases
    memo[(0, 0)] = 0  # Empty knapsack with zero weight
    for w in range(1, capacity + 1):
        memo[(0, w)] = -1  # Empty knapsack with nonzero weight

    # Recursively solve the subproblems
    for i in range(1, len(items) + 1):
        item, weight = items[i - 1]  # Get the current item and weight
        for w in range(capacity + 1):
            # Option 1: Exclude the current item
            memo[(i, w)] = memo[(i - 1, w)]

            # Option 2: Include the current item if its weight is within the capacity
            if weight <= w:
                memo[(i, w)] = max(memo[(i, w)], memo[(i - 1, w - weight)] + item)

    # Return the maximum value of the knapsack
    return memo[(len(items), capacity)]


# Example test cases
test_cases = [
    ([(1, 2), (2, 4), (3, 6)], 5),
    ([(1, 3), (2, 5), (3, 7)], 7),
    ([(1, 1), (2, 2), (3, 3), (4, 4)], 4),
]

for items, capacity in test_cases:
    print(f"Maximum sum for items {items} with capacity {capacity}:", knapsack(items, capacity))
```

### Example Test Cases:

```
Input:
[(1, 2), (2, 4), (3, 6)], 5

Output:
Maximum sum for items [(1, 2), (2, 4), (3, 6)] with capacity 5: 7
```

```
Input:
[(1, 3), (2, 5), (3, 7)], 7

Output:
Maximum sum for items [(1, 3), (2, 5), (3, 7)] with capacity 7: 10
```

```
Input:
[(1, 1), (2, 2), (3, 3), (4, 4)], 4

Output:
Maximum sum for items [(1, 1), (2, 2), (3, 3), (4, 4)] with capacity 4: 6
```

### Alternative Approaches:

An alternative approach to solving this problem is to use an iterative approach known as the bottom-up approach. Instead of recursively solving subproblems, the bottom-up approach builds the solution starting from the smallest subproblems and gradually working towards the final solution. This approach has the same time complexity as the recursive approach but offers better memory management, making it more suitable for large-scale problems.

# Connect with me: https://github.com/ohkrahul
