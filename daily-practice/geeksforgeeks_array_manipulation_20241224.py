'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-12-24
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-12-24

### Problem Understanding and Approach

The Array Manipulation problem involves performing a sequence of operations on an array of integers. Each operation is of the form (a, b, k), where a and b define a range of elements in the array, and k is the value to be added to all elements within that range.

The naive approach to solving this problem would be to iterate through the entire array for each operation and perform the necessary additions. However, this approach would have a time complexity of O(n * m), where n is the size of the array and m is the number of operations.

Instead, we can use a more efficient approach based on the concept of "prefix sums". We can create a new array of size n, where each element represents the sum of all elements in the original array up to that index. For example, if the original array is [1, 2, 3, 4], then the prefix sum array would be [1, 3, 6, 10].

Once we have the prefix sum array, we can perform each operation in constant time. For example, to perform the operation (1, 3, 2), we simply add 2 to the first element of the prefix sum array and subtract 2 from the fourth element. This is because adding k to all elements in the range [1, 3] is equivalent to adding k to the sum of all elements up to index 3 and subtracting k from the sum of all elements up to index 4.

### Time and Space Complexity Analysis

The time complexity of the proposed approach is O(n + m), where n is the size of the array and m is the number of operations. The space complexity is O(n), as we need to store the prefix sum array.

### Implementation

```python
def array_manipulation(n, arr):
    """
    Performs a sequence of operations on an array of integers.

    Args:
        n (int): The size of the array.
        arr (list): A list of operations, where each operation is of the form (a, b, k).

    Returns:
        int: The maximum value in the array after performing the operations.
    """

    # Create a prefix sum array.
    prefix_sum = [0] * (n + 1)

    # Perform each operation.
    for a, b, k in arr:
        prefix_sum[a - 1] += k
        prefix_sum[b] -= k

    # Calculate the maximum value in the array.
    max_value = 0
    running_sum = 0
    for i in range(n):
        running_sum += prefix_sum[i]
        max_value = max(max_value, running_sum)

    return max_value
```

### Example Test Cases

```python
# Example 1
n = 5
arr = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
result = array_manipulation(n, arr)
print(result)  # Output: 200

# Example 2
n = 10
arr = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
result = array_manipulation(n, arr)
print(result)  # Output: 10
```

### Alternative Approaches

Another approach to solving the Array Manipulation problem is using a Segment Tree. A Segment Tree is a data structure that allows us to efficiently perform range queries and updates on an array. Using a Segment Tree, we can perform each operation in O(log n) time, resulting in an overall time complexity of O(m * log n). However, the space complexity of this approach would be O(n * log n).

The choice of which approach to use depends on the specific requirements of the problem. If the number of operations is small compared to the size of the array, then the prefix sum approach is more efficient. However, if the number of operations is large, then the Segment Tree approach may be more appropriate.

# Connect with me: https://github.com/ohkrahul
