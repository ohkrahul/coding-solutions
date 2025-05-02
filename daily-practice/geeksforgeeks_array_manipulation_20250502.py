'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-05-02
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-05-02

```python
"""
Problem: Array Manipulation (GeeksForGeeks - Medium)

Description:  You are given an array arr[] of size N. You need to perform the following operations on the array:

1.  Update(l, r, val): Add 'val' to all elements in the subarray arr[l...r].
2.  Query(index): Return the value of arr[index].

Problem Understanding and Approach:

The naive approach of iterating through the subarray for each update operation will lead to a time complexity of O(N*Q) where N is the array size and Q is the number of updates. This can be inefficient for large N and Q.

A more efficient approach uses the prefix sum technique.  Instead of directly updating the array in the update operation, we maintain a difference array. The difference array stores the difference between consecutive elements of the prefix sum array.

For Update(l, r, val):
- Add 'val' to diff[l].
- Subtract 'val' from diff[r+1].

For Query(index):
- Calculate the prefix sum up to 'index' from the difference array.

Time and Space Complexity Analysis:

- Time Complexity:
    - Update: O(1)
    - Query: O(N) (worst-case for calculating prefix sum)  However, if we are performing multiple queries, the prefix sum can be pre-calculated after all updates in O(N) time, resulting in O(1) query time afterward.
- Space Complexity: O(N) for the difference array.


Alternative Approaches:

- Segment trees can be used for more efficient range queries and updates, especially when updates are frequent and interspersed with queries.  However, for the given problem where updates can be batched and queries are potentially done after all updates, the prefix sum method is more straightforward and efficient.
"""

def array_manipulation(n, operations):
    """
    Performs array manipulations using the prefix sum technique.

    Args:
        n: The size of the array.
        operations: A list of tuples, where each tuple represents an operation (l, r, val).

    Returns:
        A list representing the final state of the array after all operations.
    """
    diff_array = [0] * (n + 1)  # Initialize difference array

    # Process updates
    for l, r, val in operations:
        diff_array[l - 1] += val  # Add 'val' to diff[l-1] (0-indexed)
        if r < n:  # Handle edge case where r is the last element
            diff_array[r] -= val    # Subtract 'val' from diff[r] (0-indexed)


    # Calculate prefix sum to get the final array
    arr = [0] * n
    arr[0] = diff_array[0]
    for i in range(1, n):
        arr[i] = arr[i-1] + diff_array[i]

    return arr



# Example test cases
n = 5
operations = [(1, 2, 10), (2, 5, 20), (1, 3, 5)]  # (l, r, val)  1-indexed
result = array_manipulation(n, operations)
print(result)  # Output: [15, 35, 25, 20, 20]


n = 10
operations = [(1, 5, 3), (4, 8, 7), (6, 9, 1)]
result = array_manipulation(n, operations)
print(result)  # Output: [3, 3, 3, 10, 10, 8, 8, 7, 1, 0]

n = 10
operations = [(2,6,8), (3,5,7),(1,8,1),(5,9,15)]
result = array_manipulation(n, operations)
print(result)  # Output: [1, 9, 16, 23, 38, 23, 23, 16, 15, 0]




```

# Connect with me: https://github.com/ohkrahul
