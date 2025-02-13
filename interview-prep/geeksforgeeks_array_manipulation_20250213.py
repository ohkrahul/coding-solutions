'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-13
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-13

## Problem Understanding and Approach

The problem statement describes an array of integers where certain operations are specified. These operations involve adding specific values to specified indices within the array. Our goal is to find the maximum sum of any element in the array after performing these operations.

To approach this problem, we can iterate over the given operations and apply each operation to the corresponding array index. While iterating, we can keep track of the maximum value encountered so far.

### Time and Space Complexity Analysis

* **Time Complexity:** O(n+m), where n is the length of the array and m is the number of operations. This is because we need to iterate over both the array and the operations to apply the necessary changes.
* **Space Complexity:** O(1), as we only need to keep track of the maximum value, which is a constant size variable.

### Well-Commented Implementation in Python

```python
def array_manipulation(arr_len, operations):
    """
    Finds the maximum sum of any element in an array after performing specific operations.

    Parameters:
    arr_len(int): Length of the array.
    operations(list): List of tuples representing the operations. Each tuple contains three integers: (a, b, k),
    where a and b are the indices of the range, inclusive, and k is the value to be added.

    Returns:
    int: Maximum sum of any element in the array.
    """
    # Create an array of zeros to represent the initial state of the array.
    arr = [0] * arr_len

    # Iterate over the operations and apply them to the array.
    for a, b, k in operations:
        # Add k to all elements in the range [a, b].
        arr[a - 1] += k
        if b < arr_len:
            arr[b] -= k

    # Find the maximum value in the array.
    max_sum = 0
    sum = 0
    for element in arr:
        sum += element
        max_sum = max(max_sum, sum)

    # Return the maximum sum.
    return max_sum
```

### Example Test Cases

**Input 1**
* arr_len = 5
* operations = [(1, 2, 100), (2, 5, 100), (3, 4, 100)]

**Output 1**
200 (The maximum sum is achieved at index 3 with a value of 200.)

**Input 2**
* arr_len = 10
* operations = [(1, 5, 3), (4, 8, 7), (6, 9, 1)]

**Output 2**
10 (The maximum sum is achieved at multiple indices, including index 5 with a value of 10.)

### Alternative Approaches

**Prefix Sum Approach:**

This approach uses a prefix sum array to efficiently calculate the sum of any range in the array. First, we create a prefix sum array, where each element represents the cumulative sum of elements up to that index. Then, for each operation, we update the prefix sum array by adding the value k at index a-1 and subtracting it at index b. Finally, we find the maximum element in the prefix sum array, which represents the maximum sum of any range in the original array.

**Segment Tree Approach:**

A segment tree can be used to efficiently update and query ranges in the array. We can construct a segment tree representing the original array. When an operation is applied, we update the corresponding range in the segment tree. Then, we can use the segment tree to find the maximum value in the array in O(log n) time.

# Connect with me: https://github.com/ohkrahul
