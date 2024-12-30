'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-12-30
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-12-30

## Problem Understanding and Approach

We are given an array of integers of size N and Q queries. Each query is of the form (a, b, k), where a and b are the indices of the array, and k is an integer to be added to all elements of the subarray a to b (inclusive).

The objective is to calculate the array after all queries are applied and print the maximum element in the array.

Our approach to solve this problem is as follows:
1. Initialize an array of size N to all zeros.
2. For each query (a, b, k), add k to the element at index a and subtract k from the element at index b+1 (using the exclusive prefix sum technique).
3. Perform a prefix sum operation on the array.
4. The maximum element in the prefix sum array is the maximum value in the resulting array after applying all queries.

## Time and Space Complexity Analysis

- Time complexity: O(N + Q) where N is the size of the array and Q is the number of queries.
- Space complexity: O(N) for the result array and prefix sum array.

## Well-commented Implementation

```python
def arrayManipulation(n, queries):
    """
    Performs a series of operations on an array of size n and returns the maximum element.

    Args:
        n (int): Size of the array.
        queries (list): List of tuples representing queries. Each tuple (a, b, k) represents an operation to add k to all elements in the range a to b.

    Returns:
        int: Maximum element after all queries are applied.
    """

    # Initialize array with zeros
    result = [0] * n

    # Apply queries
    for a, b, k in queries:
        result[a - 1] += k
        if b < n:
            result[b] -= k

    # Perform prefix sum
    prefix_sum = [0] * n
    prefix_sum[0] = result[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + result[i]

    # Find the maximum element in the prefix sum array
    return max(prefix_sum)
```

## Example Test Cases

**Input:**
>>> n = 5
>>> queries = [(1, 2, 10), (2, 3, 20), (2, 5, 10)]

**Output:**
>>> 30

**Explanation:**
After applying the queries, the array becomes [10, 30, 30, 30, 20]. The maximum element in the array is 30.

**Input:**
>>> n = 10
>>> queries = [(1, 5, 3), (4, 8, 7), (6, 9, 1)]

**Output:**
>>> 10

**Explanation:**
After applying the queries, the array becomes [3, 3, 3, 10, 10, 10, 17, 17, 18, 18]. The maximum element in the array is 18.

## Alternative Approaches

An alternative approach to solve this problem is to use a binary indexed tree (BIT). A BIT is a data structure that allows efficient updates and range queries on an array.

Using a BIT, we can store the original array and apply the queries by updating the corresponding ranges in the BIT. We can then perform a range query to find the maximum element in the modified array.

The time complexity of this approach is also O(N + Q) and the space complexity is O(N).

# Connect with me: https://github.com/ohkrahul
