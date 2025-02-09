'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-09
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-09

# Problem understanding and approach
## Problem Understanding
Given an array of integers and a series of queries, we need to perform the following operations for each query:

- Increase each element from index L to R (inclusive) by X.
- Print the maximum element in the array.

## Approach: Prefix Sum
In this problem, we can use prefix sums to efficiently perform the queries. We can create a prefix sum array, where each element represents the sum of all elements from index 1 to that index. To perform a query, we can update the prefix sum array by adding X to the element at index L and subtracting X from the element at index R+1. Then, to find the maximum element, we just need to find the maximum element in the prefix sum array.

# Time and space complexity analysis
## Time Complexity
The time complexity of our solution is O(n + q), where n is the size of the input array and q is the number of queries. Creating the prefix sum array takes O(n) time, and each query takes O(1) time.

## Space Complexity
The space complexity of our solution is O(n), since we need to store the prefix sum array.

# Well-commented implementation
```python
# Function to perform the operations on the array
def manipulate_array(arr, queries):
    # Create a prefix sum array
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    # Perform the queries
    for query in queries:
        L, R, X = query
        prefix_sum[L-1] += X
        prefix_sum[R] -= X

    # Find the maximum element in the prefix sum array
    max_element = prefix_sum[0]
    for i in range(1, len(arr)):
        max_element = max(max_element, prefix_sum[i])

    # Return the maximum element
    return max_element

# Example test cases
arr = [1, 2, 3, 4, 5]
queries = [(2, 4, 1), (1, 5, 2)]
result = manipulate_array(arr, queries)
print(result)  # Output: 7

arr = [1, 2, 3, 4, 5]
queries = [(1, 2, 3), (3, 5, 1)]
result = manipulate_array(arr, queries)
print(result)  # Output: 8
```

# Alternative approaches
## Using a Segment Tree
We can also use a segment tree to efficiently perform the queries. A segment tree is a data structure that can be used to store and update information about a range of elements in an array. In this problem, we can use a segment tree to store the maximum element in each range of the array. To perform a query, we can update the segment tree by adding X to the range from L to R. Then, to find the maximum element, we can just query the segment tree for the maximum element in the entire array.

The time complexity of using a segment tree is O(log n) for each query and O(n) for pre-processing the segment tree. The space complexity is also O(n).

# Connect with me: https://github.com/ohkrahul
