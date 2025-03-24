'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-03-24
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-03-24

```python
"""
Problem: Array Manipulation (GeeksForGeeks - Medium)

Description:  You are given an array arr[] of size N. You need to perform the following operations:

1. Pick any element from the array.
2. Replace it with the floor of its square root.
3. Repeat steps 1 and 2 until all elements of the array become either 0 or 1.

Return the minimum number of operations required to make all array elements either 0 or 1.


Problem Understanding and Approach:

The core idea is to repeatedly apply the square root operation until each element becomes either 0 or 1. We can optimize this by noticing that:

- Once an element becomes 0 or 1, further operations are unnecessary.
- sqrt(x) converges quickly to 1 for x > 1.
- We can use a counter for each element to track operations.

Time and Space Complexity Analysis:

- Time Complexity: O(N * log log(MAX_VALUE)), where MAX_VALUE is the maximum element in the array. The square root operation converges very quickly (double logarithmic).
- Space Complexity: O(1) - We are modifying the array in place, so constant extra space is used.

"""

import math

def min_operations(arr):
    """
    Calculates the minimum operations to reduce array elements to 0 or 1.

    Args:
        arr: The input array of integers.

    Returns:
        The minimum number of operations.
    """

    n = len(arr)
    total_operations = 0

    for i in range(n):
        operations = 0
        while arr[i] > 1:  # Only operate if the element is greater than 1
            arr[i] = int(math.sqrt(arr[i]))  # Integer division using int()
            operations += 1
        total_operations += operations

    return total_operations



# Example Test Cases
print("-----Test Cases-----")
arr1 = [2, 3, 4, 5, 16, 256]
print(f"Input: {arr1}, Output: {min_operations(arr1)}")  # Expected output: 8

arr2 = [1, 0, 2, 4, 16]
print(f"Input: {arr2}, Output: {min_operations(arr2)}") # Expected output: 4


arr3 = [1, 1, 1, 1]
print(f"Input: {arr3}, Output: {min_operations(arr3)}") # Expected output: 0



# Alternative Approaches:

# 1. Pre-calculate square roots:  For a limited range of input values, we can pre-calculate the number of square root operations needed for each number. This would involve creating a lookup table. This approach is effective if we have many repeated input values.

# 2. Logarithmic calculation: The number of square root operations to bring a number 'x' to 1 is approximately log2(log2(x)). We can use this for a quicker, albeit slightly less precise, calculation. However, handling cases where x <= 1 needs special attention.



```

# Connect with me: https://github.com/ohkrahul
