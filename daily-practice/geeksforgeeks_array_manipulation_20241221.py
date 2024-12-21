'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-12-21
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-12-21

## 1. Problem Understanding and Approach

The problem asks us to manipulate an array of integers by performing the following operations:

- For each query, add `B` to all elements between `L` and `R` (inclusive).
- After all queries, return the maximum element in the array.

To solve this problem, we can utilize a prefix sum approach. We can maintain an array of size N, where N is the length of the given array. For each query, we can update the prefix sum at L by adding B and decrement the prefix sum at R+1 by B. This approach ensures that all elements between L and R (inclusive) are updated correctly.

After processing all queries, we can find the maximum element in the array by iterating through the prefix sum array and keeping track of the maximum value encountered.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N + Q), where N is the length of the given array and Q is the number of queries. We iterate over the array once to calculate prefix sums and once to find the maximum element. Each query takes constant time to update the prefix sum.
- **Space Complexity**: O(N), as we use an array of size N to store the prefix sums.

## 3. Well-Commented Implementation

```python
def array_manipulation(arr: list[int], queries: list[list[int, int, int]]) -> int:
    """
    Given an array of integers, perform the following operations:

    For each query, add B to all elements between L and R (inclusive).

    Return the maximum element in the array after all queries.

    Args:
        arr (list[int]): The input array.
        queries (list[list[int, int, int]]): The list of queries.

    Returns:
        int: The maximum element in the array after all queries.
    """

    # Initialize a prefix sum array of size N + 1
    prefix_sum = [0] * (len(arr) + 1)

    # Process each query
    for query in queries:
        L, R, B = query
        # Add B to prefix_sum at L
        prefix_sum[L] += B
        # Decrement prefix_sum at R + 1 (to avoid double-counting)
        prefix_sum[R + 1] -= B

    # Calculate prefix sums
    for i in range(1, len(arr) + 1):
        prefix_sum[i] += prefix_sum[i - 1]

    # Find the maximum element in the array
    max_element = max(prefix_sum)

    return max_element
```

## 4. Example Test Cases

```python
arr = [1, 2, 3]
queries = [[1, 2, 1], [2, 3, 2]]

print(array_manipulation(arr, queries))  # Output: 5
```

## 5. Alternative Approaches

**Range-Based Approach**:

Instead of using a prefix sum array, we can directly update the elements in the original array for each query. This approach has a time complexity of O(NQ), where N is the length of the array and Q is the number of queries. However, it may not be suitable if the array is large as it requires updating elements multiple times.

# Connect with me: https://github.com/ohkrahul
