'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-11-29
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-11-29

### Problem Understanding and Approach

The problem can be understood as follows:
- We are given an array of integers.
- We need to perform the following operations on the array:
  - For each element at index `i` in the array, increase or decrease all the elements in the range [`start_i`, `end_i`] by `k_i`.
- We need to find the maximum element in the modified array.

The approach to solve this problem is as follows:
- We will maintain an array `diff` of size `n+1`, where `n` is the size of the given array. The value at index `i` in the `diff` array represents the difference to be added to the element at index `i` in the original array.
- We will traverse the given array from left to right. For each element at index `i`, we will increase the value at index `start_i` in the `diff` array by `k_i` and decrease the value at index `end_i+1` in the `diff` array by `k_i`.
- Finally, we will traverse the `diff` array from left to right and calculate the modified array by adding the differences to the original array.

### Time and Space Complexity Analysis

- **Time complexity:** O(n), where n is the size of the given array.
- **Space complexity:** O(n), as we are using an array of size n to store the differences.

### Well-Commented Implementation

```python
def array_manipulation(arr, n):
    """
    Performs the following operations on an array:
    - For each element at index i in the array, increase or decrease all the elements in the range [start_i, end_i] by k_i.
    - Returns the maximum element in the modified array.

    Args:
    arr: The given array.
    n: The size of the array.

    Returns:
    The maximum element in the modified array.
    """

    # Create an array of size n+1 to store the differences.
    diff = [0] * (n+1)

    # Traverse the given array from left to right.
    for i in range(len(arr)):
        # Increase the value at index start_i in the diff array by k_i.
        diff[arr[i][0] - 1] += arr[i][2]

        # Decrease the value at index end_i+1 in the diff array by k_i.
        diff[arr[i][1]] -= arr[i][2]

    # Traverse the diff array from left to right and calculate the modified array by adding the differences to the original array.
    max_element = 0
    sum = 0
    for i in range(len(diff)):
        sum += diff[i]
        max_element = max(max_element, sum)

    # Return the maximum element in the modified array.
    return max_element
```

### Example Test Cases

**Input:**
```
arr = [[1, 5, 3], [2, 4, 2], [6, 8, 6]]
n = 8
```

**Output:**
```
12
```

**Explanation:**
- After performing the operations, the modified array becomes [3, 5, 9, 11, 11, 11, 6, 12].
- The maximum element in the modified array is 12.

### Alternative Approaches

One alternative approach to solve this problem is to use a segment tree. A segment tree is a binary tree data structure that can be used to efficiently store and update a range of values in an array. In this case, we can use a segment tree to store the differences for each range in the array. When we want to update a range, we can simply update the corresponding node in the segment tree. The time complexity of this approach is O(n log n), where n is the size of the given array.

# Connect with me: https://github.com/ohkrahul
