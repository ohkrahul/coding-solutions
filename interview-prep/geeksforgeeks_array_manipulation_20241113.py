'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-11-13
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-11-13

## Problem Understanding and Approach

The problem requires us to perform operations on an array. The operations are of two types:

1. `a[l] += k`: Increment each element in the range `[l, r]` by `k`.
2. `print max(a)`: Print the maximum value in the array.

To approach this problem, we will use a technique called "prefix sum". We will create a new array `ps` of the same length as the original array `a`. The value of `ps[i]` will represent the sum of elements in `a` from index `0` to `i`.

Now, to perform the first operation, we will update the values in the `ps` array as follows:

- `ps[l - 1] += k`: Increase the prefix sum at the beginning of the range `[l, r]`.
- `ps[r] -= k`: Decrease the prefix sum at the end of the range `[l, r]`.

This will effectively add `k` to all elements in the range `[l, r]` without modifying the original array `a`.

To perform the second operation, we can simply iterate through the `ps` array to find the maximum value.

## Time and Space Complexity Analysis

- **Time Complexity:** O(n + q), where n is the length of the array and q is the number of operations.
- **Space Complexity:** O(n), since we need to create a prefix sum array of the same length as the original array.

## Well-Commented Implementation

```python
def arrayManipulation(a, n, queries):
    """
    Perform operations on an array and print the maximum value.

    Args:
        a (list): The original array.
        n (int): The length of the array.
        queries (list): The list of operations.

    Returns:
        int: The maximum value in the array.
    """

    # Create a prefix sum array
    ps = [0] * n

    # Perform the operations
    for l, r, k in queries:
        ps[l - 1] += k
        if r < n:
            ps[r] -= k

    # Calculate the prefix sums
    for i in range(1, n):
        ps[i] += ps[i - 1]

    # Find the maximum value in the prefix sum array
    max_value = max(ps)

    return max_value
```

## Example Test Cases

### Input

```python
a = [1, 2, 3, 4, 5]
n = len(a)
queries = [(1, 3, 2), (2, 4, 3), (3, 5, 4)]
```

### Output

```
9
```

## Alternative Approaches

- **Using a segment tree:** A segment tree can be used to efficiently perform range updates and queries on an array. This approach would have a time complexity of O(log n) per operation.
- **Using a lazy propagation technique:** This technique can be used to optimize the prefix sum approach by delaying the update of the prefix sum array until absolutely necessary. This approach would have a time complexity of O(log n) per operation.

# Connect with me: https://github.com/ohkrahul
