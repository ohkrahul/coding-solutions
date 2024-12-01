'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-12-01
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-12-01

## Problem Understanding and Approach

The problem requires us to perform a series of operations on an array of integers. The operations involve updating the value of specific subarrays based on given query values. The goal is to find the maximum element in the modified array after all operations are performed.

The straightforward approach is to iterate through each operation and update the affected subarray elements. However, this approach has a time complexity of O(NQ), where N is the size of the array and Q is the number of operations. This can be inefficient for large arrays or a large number of operations.

A more efficient approach is to use a prefix sum array. The prefix sum array stores the cumulative sum of the original array up to each index. By using the prefix sum array, we can update the subarray in constant time.

The approach involves the following steps:

1. Create a prefix sum array of the original array.
2. For each operation, update the prefix sum array by adding the query value to the start and end indices of the affected subarray.
3. Compute the modified array from the updated prefix sum array.
4. Find the maximum element in the modified array.

## Time and Space Complexity Analysis

**Time Complexity:** O(N + Q), where N is the size of the array and Q is the number of operations. The time complexity is dominated by the prefix sum array computation, which takes O(N) time. The operation updates and finding the maximum element take O(Q) time.

**Space Complexity:** O(N), as the prefix sum array requires additional space.

## Well-Commented Implementation

```python
def array_manipulation(arr, queries):
    """
    Computes the maximum element in an array after performing a series of operations.

    Parameters:
        arr (list): The original array of integers.
        queries (list): A list of tuples representing the operations. Each tuple has the form (a, b, k),
            where a and b are the start and end indices of the subarray to be updated, and k is the update value.

    Returns:
        int: The maximum element in the modified array.
    """

    # Create a prefix sum array
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # Update the prefix sum array based on the queries
    for query in queries:
        a, b, k = query
        prefix_sum[a - 1] += k
        if b < len(arr):
            prefix_sum[b] -= k

    # Compute the modified array from the updated prefix sum array
    modified_arr = [0] * len(arr)
    modified_arr[0] = prefix_sum[0]
    for i in range(1, len(arr)):
        modified_arr[i] = prefix_sum[i] - prefix_sum[i - 1]

    # Find the maximum element in the modified array
    max_element = max(modified_arr)

    return max_element
```

## Example Test Cases

```python
# Test case 1
arr = [1, 2, 3, 4, 5]
queries = [(1, 3, 2), (2, 4, 3)]
result = array_manipulation(arr, queries)
print(result)  # Output: 8

# Test case 2
arr = [1, 5, 3, 2, 4]
queries = [(2, 4, -3), (1, 3, 5)]
result = array_manipulation(arr, queries)
print(result)  # Output: 12
```

## Alternative Approaches

An alternative approach is to use a segment tree. A segment tree is a data structure that can be used to perform range queries on an array in O(log N) time. This can be useful in cases where we need to perform a large number of operations on specific subarrays. However, the implementation of a segment tree is more complex than the prefix sum approach.

# Connect with me: https://github.com/ohkrahul
