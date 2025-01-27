'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-01-27
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-01-27

## Problem Understanding and Approach

The "Array Manipulation" problem from GeeksForGeeks involves a series of operations on an array of integers. Each operation is represented by a sequence of three integers:

```
a[i] += k
```

where `a[i]` is the value at index `i` of the array and `k` is an integer to be added to `a[i]`. The goal is to find the maximum value in the array after performing all the operations.

**Approach:**
We can use a prefix sum array to efficiently handle the operations and determine the maximum value. Here's the general approach:

1. Create a prefix sum array `prefix_sum` of size `n`, where `n` is the length of the input array. This array stores the cumulative sum of elements in the original array.
2. Iterate through the operations and update the prefix sum values accordingly. For each operation `a[i] += k`, increment the `prefix_sum[i]` by `k`.
3. Find the maximum value in the `prefix_sum` array. This maximum value represents the maximum value in the original array after performing all the operations.

## Time and Space Complexity Analysis

**Time Complexity:**

* Iterating through the operations: O(n)
* Updating prefix sum: O(n)
* Finding maximum in `prefix_sum`: O(n)

Total: O(n)

**Space Complexity:**

* Prefix sum array: O(n)

## Well-Commented Implementation in Python

```python
def array_manipulation(n: int, operations: list[list[int]]) -> int:
    """
    Finds the maximum value in an array after performing a series of operations.

    Args:
        n (int): Length of the input array.
        operations (list[list[int]]): List of tuples representing operations, i.e. [a[i], k].

    Returns:
        int: Maximum value in the array after operations.
    """

    # Create a prefix sum array
    prefix_sum = [0] * (n + 1)

    # Update prefix sum according to operations
    for operation in operations:
        start, end, k = operation
        prefix_sum[start - 1] += k
        prefix_sum[end] -= k

    # Perform prefix sum operation
    max_value = 0
    current_sum = 0
    for i in range(n):
        current_sum += prefix_sum[i]
        if current_sum > max_value:
            max_value = current_sum

    return max_value
```

## Example Test Cases

```python
# Test Case 1:
n = 5
operations = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
expected_output = 45

# Test Case 2:
n = 10
operations = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
expected_output = 31
```

## Alternative Approaches

**Using a Binary Indexed Tree (BIT):**

A BIT can also be used to efficiently update and query the prefix sum values. This approach has a time complexity of O(n log n) and space complexity of O(n).

**Using a Sparse Table:**

This data structure can be used to answer range queries for the maximum value in a given range. This approach has a time complexity of O(n log n) for preprocessing and O(log n) for each range query.

# Connect with me: https://github.com/ohkrahul
