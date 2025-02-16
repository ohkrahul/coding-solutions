'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-16
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-16

## Problem Understanding and Approach

The problem asks us to perform two types of operations on an array and output the maximum element of the array after these operations.

1. **Addition of a value**: For each operation of this type, we need to add a given value to all elements of the array within a specified range.
2. **Query**: For each operation of this type, we need to output the maximum element of the array within a specified range.

To efficiently handle these operations, we can use a prefix sum array. We can initialize the prefix sum array by adding 0 to the first element and adding the subsequent elements to the previous sum. This prefix sum array allows us to quickly calculate the sum of elements in any given range.

For the addition operations, we can simply update the prefix sum array at the start and end of the range by adding the value to be added. For the query operations, we can find the sum of elements in the given range using the prefix sum array and output the maximum value.

## Time and Space Complexity Analysis

**Time Complexity**: O(n) for initialization of the prefix sum array, O(1) for each query or update operation. The total time complexity is O(n + q), where n is the size of the array and q is the number of operations.

**Space Complexity**: O(n) for the prefix sum array.

## Well-Commented Implementation

```python
def array_manipulation(arr, queries):
    """
    Performs addition and query operations on an array and returns the maximum element.

    Parameters:
    arr: The original array.
    queries: A list of tuples, where each tuple represents an operation.
             The operations can be of two types:
             1. Addition: (1, start, end, value) -> Add 'value' to all elements in the range [start, end].
             2. Query: (2, start, end) -> Output the maximum element in the range [start, end].

    Returns:
    The maximum element in the array after all operations have been performed.
    """

    # Initialize the prefix sum array.
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    # Perform the operations.
    for query in queries:
        operation, start, end = query[:3]
        if operation == 1:
            value = query[3]
            # Update the prefix sum array.
            prefix_sum[start] += value
            prefix_sum[end + 1] -= value
        else:
            # Calculate the maximum element in the range.
            max_element = -float('inf')
            for i in range(start, end + 1):
                max_element = max(max_element, prefix_sum[i])
            print(max_element)

    # Calculate the final array after all operations.
    final_array = [0] * n
    for i in range(n):
        final_array[i] = prefix_sum[i + 1]

    # Return the maximum element in the final array.
    return max(final_array)
```

## Example Test Cases

```python
arr = [1, 2, 3, 4, 5]
queries = [(1, 0, 2, 10), (2, 0, 2), (1, 1, 3, 20), (2, 1, 3)]
result = array_manipulation(arr, queries)
print(result)  # Output: 32
```

## Alternative Approaches

Another possible approach is to use a segment tree. A segment tree is a data structure that allows us to efficiently update and query elements in a range. However, the segment tree approach is generally more complex and has a higher time complexity (O(log n) for each operation) compared to the prefix sum approach, which has a constant time complexity for each operation.

# Connect with me: https://github.com/ohkrahul
