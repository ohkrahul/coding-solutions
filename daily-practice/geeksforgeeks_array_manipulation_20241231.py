'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-12-31
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-12-31

## Problem Understanding and Approach

The problem involves performing operations on an integer array. The operations require updating the elements within a specified range by adding a given value. We are required to find the maximum element in the modified array after all the operations are performed.

To solve this problem, we can use a cumulative sum approach. We can initialize an array of size equal to the length of the given array, where each element initially represents the count of elements in the specified range. Then, for each operation, we increment the start index and decrement the end index by 1 in the cumulative sum array. 

After processing all the operations, we perform a cumulative sum on the cumulative sum array to get the actual modified array. Finally, we find the maximum element in the modified array.

## Time and Space Complexity Analysis

* **Time Complexity**: O(N + M) where N is the size of the given array and M is the number of operations.
* **Space Complexity**: O(N) for storing the cumulative sum array.

## Well-commented Implementation

```python
def arrayManipulation(n: int, queries: list[list[int]]) -> int:
    """
    :param n: Size of the array
    :param queries: List of operations [start, end, value]
    :return: Maximum element in the modified array
    """

    # Initialize a cumulative sum array to count elements in specified ranges
    cumulative_sum = [0] * (n + 1)

    # For each operation, update the cumulative sum array
    for query in queries:
        start, end, value = query
        cumulative_sum[start - 1] += value
        cumulative_sum[end] -= value

    # Perform cumulative sum on cumulative sum array to get the modified array
    for i in range(1, n + 1):
        cumulative_sum[i] += cumulative_sum[i - 1]

    # Find the maximum element in the modified array
    return max(cumulative_sum)
```

## Example Test Cases

**Input**:
* n = 5
* queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

**Output**:
* 200

**Explanation**:
* After applying the operations:
    * [100, 200, 200, 200, 100]
* Maximum element = 200

## Alternative Approaches

1. **Segment Tree**: We can build a segment tree on the given array and update the range values efficiently. The time complexity would be O(M log N).

2. **Lazy Propagation**: We can use lazy propagation to optimize the segment tree approach, reducing the time complexity to O(M + N).

# Connect with me: https://github.com/ohkrahul
