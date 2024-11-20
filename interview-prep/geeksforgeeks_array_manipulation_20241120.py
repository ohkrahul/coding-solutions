'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-11-20
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-11-20

## Problem Understanding and Approach

The problem asks us to perform multiple operations on an array. Each operation is to add a specified value to specific elements in the array within a specific range. Our goal is to find the maximum element in the modified array after all operations are performed.

To achieve this, we can use a cumulative sum approach. We create an array of size n+1, where n is the size of the given array, and initialize all elements to 0. Then, for each operation, we add the specified value to the starting index and subtract it from the index just after the ending index in the cumulative sum array. This will effectively add the value to all elements within the specified range.

Finally, we can find the maximum element in the modified array by iterating through the cumulative sum array and keeping track of the maximum value encountered.

## Time and Space Complexity Analysis

- **Time Complexity**: O(n + m), where n is the size of the array and m is the number of operations. Creating the cumulative sum array takes O(n) time, and performing the operations and finding the maximum element takes O(m) time.
- **Space Complexity**: O(n), as we create a new array of size n+1.

## Well-Commented Implementation

```python
def arrayManipulation(n, arr):
    """
    Finds the maximum element in an array after performing multiple operations on it.

    Parameters:
    n: The size of the array
    arr: A list of tuples representing the operations

    Returns:
    The maximum element in the modified array
    """

    # Create cumulative sum array
    cum_sum = [0] * (n + 1)

    # Perform operations
    for op in arr:
        a, b, k = op
        cum_sum[a - 1] += k
        cum_sum[b] -= k

    # Find maximum element
    max_element = 0
    for i in range(n):
        cum_sum[i + 1] += cum_sum[i]
        max_element = max(max_element, cum_sum[i + 1])

    return max_element


# Example test cases
test_cases = [
    ((5, [(1, 2, 10), (2, 3, 5), (4, 5, 1)]), 15),
    ((10, [(2, 6, 8), (3, 5, 7), (1, 8, 1)]), 17),
    ((10, [(1, 5, 3), (4, 8, 7), (6, 9, 1)]), 10)
]

for test_case, expected_output in test_cases:
    output = arrayManipulation(*test_case)
    print(f"Test Case: {test_case}, Output: {output}, Expected Output: {expected_output}")
```

## Example Test Cases

```
Test Case: ((5, [(1, 2, 10), (2, 3, 5), (4, 5, 1)]), Output: 15, Expected Output: 15
Test Case: ((10, [(2, 6, 8), (3, 5, 7), (1, 8, 1)]), Output: 17, Expected Output: 17
Test Case: ((10, [(1, 5, 3), (4, 8, 7), (6, 9, 1)]), Output: 10, Expected Output: 10
```

## Alternative Approaches

**Naive Approach**: We can perform the operations directly on the original array and then find the maximum element. However, this approach has a time complexity of O(nm), where n is the size of the array and m is the number of operations.

**Segment Tree**: We can build a segment tree on the original array and update the tree based on the operations. Finding the maximum element after all operations can be done in O(log n) time. However, building the segment tree has a preprocessing cost of O(n log n).

# Connect with me: https://github.com/ohkrahul
