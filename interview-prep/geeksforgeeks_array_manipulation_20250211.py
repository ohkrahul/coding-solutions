'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-11
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-11

## Problem Understanding and Approach ##

The problem requires us to perform a series of operations on an array of integers. Each operation is defined by three integers (a, b, and k) and involves adding k to all elements in the subarray [a, b]. Our goal is to determine the maximum element in the modified array after all the operations are applied.

To approach this problem, we'll use a prefix sum array to efficiently calculate the impact of each operation. The prefix sum array, prefix_sum[], tracks the cumulative sum of the original array.

## Time and Space Complexity Analysis ##

Time Complexity: O(n + m), where n is the length of the original array and m is the number of operations.

Space Complexity: O(n), as we create a prefix sum array of size n.

## Implementation ##

```python
def array_manipulation(n, queries):
    """
    Finds the maximum element in an array after applying a series of operations.

    Parameters:
        n (int): The size of the original array.
        queries (list): A list of tuples representing the operations to be performed.

    Returns:
        int: The maximum element in the modified array.
    """
    # Initialize the prefix sum array to all zeros.
    prefix_sum = [0] * (n + 1)

    # Update the prefix sum array based on the queries.
    for a, b, k in queries:
        prefix_sum[a - 1] += k
        prefix_sum[b] -= k

    # Calculate the cumulative sum of the prefix sum array.
    for i in range(1, n + 1):
        prefix_sum[i] += prefix_sum[i - 1]

    # Find the maximum element in the cumulative sum array.
    maximum_element = max(prefix_sum)

    return maximum_element
```

## Example Test Cases ##

**Input:**

```python
n = 10
queries = [(1, 5, 3), (4, 8, 7), (6, 9, 1)]
```

**Output:**

```
10
```

**Explanation:**

* After the first operation, the subarray [1, 5] is incremented by 3, resulting in [4, 7, 10, 13, 16].
* After the second operation, the subarray [4, 8] is incremented by 7, resulting in [4, 7, 10, 13, 20, 27, 34].
* After the third operation, the subarray [6, 9] is incremented by 1, resulting in [4, 7, 10, 13, 20, 27, 34, 35, 36].
* The maximum element in the modified array is 36.

## Alternative Approaches ##

An alternative approach to this problem is to use a segment tree. A segment tree can be used to efficiently update and query any range in the array in O(log n) time. However, implementing and using a segment tree for this problem may be more complex than the prefix sum approach.

# Connect with me: https://github.com/ohkrahul
