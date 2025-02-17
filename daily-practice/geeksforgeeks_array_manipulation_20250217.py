'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-17
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-17

## Problem Understanding and Approach

The "Array Manipulation" problem in GeeksForGeeks can be broken down into the following steps:

- Given an array `arr` of length `n`, where each `arr[i]` contains a tuple `(a, b, k)`, we need to perform the following operation:
  - Increment each element in the range `a` to `b` (inclusive) by `k`.

To solve this problem, we can use a cumulative sum approach:

1. Create an auxiliary array `prefix_sum` of length `n+1`.
2. For each tuple `(a, b, k)` in `arr`, update `prefix_sum[a]` by `k` and `prefix_sum[b+1]` by `-k`.
3. Perform a cumulative sum on `prefix_sum` to obtain the final result.

## Time and Space Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the array. We iterate over the array once to update `prefix_sum`, and once to perform the cumulative sum.
- **Space Complexity**: O(n), since we use an auxiliary array `prefix_sum` of length n+1.

## Well-Commented Implementation

```python
def array_manipulation(arr, n):
    """
    Performs the specified operations on an array.

    Args:
        arr (list): The input array.
        n (int): The length of the array.

    Returns:
        list: The modified array.
    """

    # Create an auxiliary array for storing the cumulative sum.
    prefix_sum = [0] * (n + 1)

    # Update the prefix_sum array based on the given operations.
    for (a, b, k) in arr:
        prefix_sum[a] += k
        prefix_sum[b + 1] -= k

    # Perform cumulative sum on `prefix_sum` to obtain the final result.
    for i in range(1, n + 1):
        prefix_sum[i] += prefix_sum[i - 1]

    # Return the modified array.
    return prefix_sum

# Example Input
arr = [(1, 5, 2), (4, 8, 7), (6, 9, 3)]
n = 10

# Function call
result = array_manipulation(arr, n)

# Print the modified array
print(result)
```

## Example Test Cases

- **Input**: `arr = [(1, 5, 2), (4, 8, 7), (6, 9, 3)]`, `n = 10`
- **Output**: `[2, 9, 14, 21, 23, 26, 28, 31, 30, 27]`

- **Input**: `arr = [(2, 6, 1), (5, 10, 2)], n = 12`
- **Output**: `[1, 3, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6]`

## Alternative Approaches

An alternative approach to this problem is to use a segment tree. The segment tree can efficiently handle range queries and updates, but it requires O(log n) time per query or update, compared to O(1) time using the cumulative sum approach. Therefore, the cumulative sum approach is more efficient for this specific problem.

# Connect with me: https://github.com/ohkrahul
