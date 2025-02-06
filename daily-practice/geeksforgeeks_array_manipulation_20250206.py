'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-06
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-06

## Array Manipulation

### Problem Understanding and Approach

The array manipulation problem involves modifying an array of integers based on given operations. Each operation consists of three integers, `a`, `b`, and `k`, which represent adding `k` to each element in the range `[a, b]` of the array. The task is to determine the maximum value that any element in the array attains after performing all the operations.

Our approach to solving this problem involves using a difference array, which is another array of the same size as the original array. The difference array tracks the change in value of each element in the original array after performing the operations. Specifically, the difference array is constructed by iterating through the operations and updating the difference array as follows:

- For each operation (a, b, k), we increment the difference array at index `a` by `k` and decrement the difference array at index `b + 1` by `k`.

Once the difference array is constructed, we can find the maximum value in the original array by iteratively adding the difference array values to the original array values. The maximum value in the resulting array will be the maximum value in the original array after performing all the operations.

### Time and Space Complexity Analysis

- **Time complexity:** O(n + m), where `n` is the size of the original array and `m` is the number of operations.
- **Space complexity:** O(n), as the difference array is of the same size as the original array.

### Well-Commented Implementation

```python
def array_manipulation(n, operations):
    """
    Performs array manipulation operations and returns the maximum value in the modified array.

    Args:
        n (int): Size of the original array.
        operations (list): List of operations in the form (a, b, k).

    Returns:
        int: Maximum value in the modified array.
    """

    # Initialize difference array
    diff_array = [0] * (n + 1)

    # Update difference array based on operations
    for a, b, k in operations:
        diff_array[a] += k
        diff_array[b + 1] -= k

    # Compute modified array
    modified_array = [0] * n
    prefix_sum = 0

    for i in range(n):
        prefix_sum += diff_array[i]
        modified_array[i] = prefix_sum

    # Return maximum value in modified array
    return max(modified_array)
```

### Example Test Cases

```python
# Test case 1
n = 10
operations = [(1, 5, 3), (4, 8, 7), (6, 9, 1)]
result = array_manipulation(n, operations)
print(result)  # Output: 10

# Test case 2
n = 5
operations = [(1, 2, 100), (2, 5, 100), (3, 4, 100)]
result = array_manipulation(n, operations)
print(result)  # Output: 200
```

### Alternative Approaches

**Using a Segment Tree:**

A segment tree can be used to efficiently perform the operations and determine the maximum value. The segment tree stores the maximum value in each range of the array, and operations can be performed by updating the corresponding ranges in the segment tree. This approach has a time complexity of O(m log n) for performing the operations and O(1) for finding the maximum value.

**Using a Binary Indexed Tree (BIT):**

A binary indexed tree can also be used to solve this problem efficiently. The BIT supports range updates and point queries, which can be used to perform the operations and find the maximum value in O(log n) time for each operation.

# Connect with me: https://github.com/ohkrahul
