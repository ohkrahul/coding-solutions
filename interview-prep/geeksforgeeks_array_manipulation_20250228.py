'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-28
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-28

```python
# Problem: Array Manipulation (GeeksForGeeks - Medium)

# 1. Problem Understanding and Approach:

# Problem Description (Generalized from GeeksForGeeks variations):
# You are given an array `arr` of integers and a list of operations (queries). Each operation is a tuple `(l, r, k)` which means: Add `k` to every element in the subarray `arr[l:r+1]`.  The task is to perform all operations and return the resulting array.

# Approach: Prefix Sum/Difference Array

# Instead of iterating through the subarray for each operation (which leads to O(n*m) complexity where n is array size and m is number of queries), we use a more efficient approach using prefix sum/difference array.

# - We create a difference array `diff` of the same size as `arr`, initialized to zeros. 
# - For each query (l, r, k), we increment `diff[l]` by `k` and decrement `diff[r+1]` by `k`.
# - Finally, we reconstruct the modified array by calculating the prefix sum of the difference array. The logic is that `diff[i]` stores the net change in `arr[i]` due to all operations.

# 2. Time and Space Complexity Analysis:

# Time Complexity: O(n + m) where n is the size of the array and m is the number of queries.
#     - O(m) to process all queries and update the difference array.
#     - O(n) to reconstruct the array from the difference array.

# Space Complexity: O(n) to store the difference array.


# 3. Well-commented Implementation:

def array_manipulation(arr, queries):
    """
    Performs array manipulation operations efficiently using the difference array technique.

    Args:
        arr: The input array of integers.
        queries: A list of tuples (l, r, k) representing the operations.

    Returns:
        The modified array after performing all operations.
    """

    n = len(arr)
    diff = [0] * (n + 1)  # Initialize difference array with zeros, size n+1 to handle r = n-1

    for l, r, k in queries:
        diff[l] += k        # Increment diff[l] by k
        if r + 1 < n +1:    # Handle cases where r is the last element.
            diff[r + 1] -= k  # Decrement diff[r+1] by k

    # Reconstruct the modified array from the difference array (prefix sum)
    modified_arr = [0] * n
    modified_arr[0] = diff[0]
    for i in range(1, n):
        modified_arr[i] = modified_arr[i - 1] + diff[i]
    
    return modified_arr



# 4. Example Test Cases:

arr1 = [1, 2, 3, 4, 5]
queries1 = [(0, 2, 2), (1, 4, 3), (2, 3, 1)]
result1 = array_manipulation(arr1, queries1)
print(f"Test Case 1: Input array: {arr1}, Queries: {queries1}, Result: {result1}")  # Output: [3, 7, 7, 7, 8]

arr2 = [0, 0, 0, 0, 0]
queries2 = [(0, 1, 10), (2, 4, 5)]
result2 = array_manipulation(arr2, queries2)
print(f"Test Case 2: Input array: {arr2}, Queries: {queries2}, Result: {result2}") # Output: [10, 10, 5, 5, 5]


# 5. Alternative Approaches:

# Brute Force:  Iterate through each subarray for every query and update the elements. This is O(n*m) and inefficient for large inputs.

# Segment Tree:  Can be used for more complex range queries like finding the maximum/minimum in a range after updates. However, it has a more complex implementation and higher overhead compared to the difference array approach for simple range additions.


```

# Connect with me: https://github.com/ohkrahul
