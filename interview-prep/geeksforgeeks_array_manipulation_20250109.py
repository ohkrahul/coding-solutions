'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-01-09
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-01-09

## Problem Understanding and Approach

Given an array of integers, we need to perform a sequence of operations on it. Each operation is represented by a triplet of integers [a, b, k], where:

- a is the index of the first element of the range.
- b is the index of the last element of the range.
- k is the value we need to add to each element in the range.

Our goal is to find the maximum element in the modified array after all operations are performed.

We will use a prefix sum array to efficiently handle the operations. The prefix sum array stores the cumulative sum of elements up to each index. By manipulating the prefix sum array, we can effectively update ranges of elements without having to update each element individually.

## Time and Space Complexity Analysis

- Time Complexity: O(n), where n is the length of the array. We traverse the array once and update the prefix sum array.
- Space Complexity: O(n), as we use a prefix sum array of the same size as the original array.

## Well-Commented Implementation

```python
def max_element_after_operations(arr, operations):
    """
    Finds the maximum element in the modified array after a sequence of operations.

    Parameters:
        arr (list): The original array.
        operations (list): A list of triplets representing the operations.

    Returns:
        int: The maximum element in the modified array.
    """

    # Create a prefix sum array.
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # Perform the operations on the prefix sum array.
    for op in operations:
        a, b, k = op
        prefix_sum[a] += k
        if b + 1 < len(prefix_sum):
            prefix_sum[b + 1] -= k

    # Find the maximum element in the modified array.
    max_element = 0
    for i in range(len(arr)):
        cur_sum = prefix_sum[i]
        if i > 0:
            cur_sum += -prefix_sum[i - 1]
        max_element = max(max_element, cur_sum)

    return max_element
```

## Example Test Cases

```python
arr = [1, 2, 3, 4, 5]
operations = [[1, 2, 10], [2, 4, 5]]
result = max_element_after_operations(arr, operations)
print(result)  # Output: 15
```

## Alternative Approaches

Another approach to solve this problem is to use a segment tree. A segment tree is a data structure that allows for efficiently updating ranges of values in an array and finding the maximum value in the array. Using a segment tree, we can handle the operations in O(log n) time for each operation. However, the space complexity of this approach would be O(n).

# Connect with me: https://github.com/ohkrahul
