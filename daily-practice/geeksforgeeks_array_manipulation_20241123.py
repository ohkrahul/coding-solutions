'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-11-23
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-11-23

## Problem Understanding and Approach

The "Array Manipulation" problem from GeeksForGeeks is a typical prefix sum problem. The task is to find the maximum element value in an array after performing a series of updates.
The given array contains `N` elements, and each element has an initial value of `0`. There are `Q` queries, where each query consists of three integers: `a`, `b`, and `k`. The query means that you need to increase the value of all elements in the range `[a, b]` (inclusive) by `k`.

To solve this problem, we can use a prefix sum array. We will initialize the prefix sum array with `N` elements, where each element is initially `0`. Then, for each query, we will update the prefix sum array by adding `k` to the element at index `a-1` and subtracting `k` from the element at index `b`. Finally, we will find the maximum value in the prefix sum array, which will be the maximum element value in the original array after performing all the updates.

## Time and Space Complexity Analysis

* **Time complexity:** O(`N` + `Q`), where `N` is the size of the array and `Q` is the number of queries.
* **Space complexity:** O(`N`), since the prefix sum array has `N` elements.

## Well-Commented Implementation

```python
def array_manipulation(n: int, queries: list[tuple[int, int, int]]) -> int:
    """
    Finds the maximum element value in an array after performing a series of updates.

    Args:
        n: The size of the array
        queries: List of queries, where each query consists of three integers: a, b, and k.
    Returns:
        The maximum element value in the array after performing all the updates.
    """
    # Initialize the prefix sum array with N elements, where each element is initially 0.
    prefix_sum = [0] * n

    # Update the prefix sum array for each query.
    for a, b, k in queries:
        prefix_sum[a - 1] += k
        if b < n:
            prefix_sum[b] -= k

    # Find the maximum value in the prefix sum array.
    max_value = 0
    running_sum = 0
    for x in prefix_sum:
        running_sum += x
        max_value = max(max_value, running_sum)

    return max_value
```

## Example Test Cases

```python
# Example test case 1
n = 5
queries = [(1, 2, 100), (2, 5, 100), (3, 4, 100)]
result = array_manipulation(n, queries)
print(result)  # Output: 200

# Example test case 2
n = 10
queries = [(1, 5, 3), (4, 8, 7), (6, 9, 1)]
result = array_manipulation(n, queries)
print(result)  # Output: 10
```

## Alternative Approaches

Another approach to solve this problem is to use a segment tree. A segment tree is a tree data structure that can be used to perform range queries and updates efficiently. Using a segment tree, we can perform all the updates in O(`Q`log`N`) time and find the maximum value in O(log`N`) time. The total time complexity of this approach will be O(`Q`log`N`) which is better than the brute-force approach.

# Connect with me: https://github.com/ohkrahul
