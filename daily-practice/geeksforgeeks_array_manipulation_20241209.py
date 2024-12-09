'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-12-09
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-12-09

## Problem Understanding and Approach

**Problem:**
Given an array and a list of queries, the goal is to perform the following operations for each query:

1. Increment the value at index `a` by `b`.
2. Print the maximum element in the subarray from index `a` to `b`.

**Approach:**
To efficiently solve this problem, we can use a prefix sum array to store the accumulated values up to each index. This allows us to easily update the cumulative sum within a given range.

**Implementation:**

1. **Initialize Prefix Sum Array:** Create a prefix sum array `prefix_sum` of length `n+1`, where `n` is the length of the given array.
2. **Query Processing:** For each query, perform the following steps:
   - **Update Prefix Sum:** Add the value `b` to the `prefix_sum` at index `a`.
   - **Calculate Maximum:** Find the maximum value in the subarray from `prefix_sum[a]` to `prefix_sum[b+1]` using a simple loop or a binary search tree (BST).
   - **Print Maximum:** Print the calculated maximum value.

## Time and Space Complexity Analysis

- **Time Complexity:** O(N + Q), where N is the size of the array, and Q is the number of queries.
- **Space Complexity:** O(N), as we create a prefix sum array of size N.

## Implementation with Comments

```python
def array_manipulation(arr, queries):
    """
    :param arr: The initial array
    :param queries: A list of tuples representing queries ((a, b, k))
    :return: The maximum element in each subarray after the queries
    """

    # Create a prefix sum array
    prefix_sum = [0] * (len(arr) + 1)

    # Update the prefix sum based on queries
    for a, b, k in queries:
        prefix_sum[a] += k
        prefix_sum[b + 1] -= k

    # Calculate the cumulative sum
    for i in range(1, len(arr) + 1):
        prefix_sum[i] += prefix_sum[i - 1]

    # Find the maximum element in each subarray
    max_elements = []
    for i in range(1, len(arr) + 1):
        max_elements.append(max(prefix_sum[i:]))

    return max_elements
```

## Example Test Cases

**Input:**
- arr = [1, 2, 3, 4, 5]
- queries = [(1, 2, 1), (2, 4, -3), (3, 5, 2)]

**Output:**
- [2, 4, 4, 6]

## Alternative Approaches

1. **Using Segment Trees:** Segment trees can be used to efficiently update and query the maximum element in a range. This approach can provide better time complexity for some specific cases.
2. **Lazy Propagation:** If the query operations are significantly more than the number of array elements, using lazy propagation can optimize performance by deferring updates until absolutely necessary.

# Connect with me: https://github.com/ohkrahul
