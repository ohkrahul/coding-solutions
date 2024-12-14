'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-12-14
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-12-14

## Problem Understanding

Given an array and an array of pairs, each pair containing two integers 'a' and 'b'. Our task is to add a to every element in the range [a, b] and then return the maximum of the resultant array.

## Approach

For each pair [a, b], increase the value of a by 1 and decrease the value of b+1 by 1. In this way, when we iterate the original array, the summation effect of all the updates is captured in each element. Finally, find the maximum element in the modified array.

## Time and Space Complexity Analysis

* Time Complexity: O(N + K), where N is the size of the original array and K is the number of pairs.
* Space Complexity: O(N), as we need an array of size N to store the modified array.

## Well-Commented Implementation

```python
def arrayManipulation(n, queries):
    """
    Args:
        n (int): Size of the original array
        queries (list): List of queries, each query contains two integers [a, b]

    Returns:
        int: Maximum element in the modified array
    """

    # Create an array of size n+2 to store the modified array
    modified_array = [0] * (n + 2)

    # For each query, update the modified array
    for query in queries:
        a, b = query  # Unpack the query
        modified_array[a] += 1
        modified_array[b + 1] -= 1

    # Find the maximum element in the modified array
    max_element = 0
    current_sum = 0

    # Iterate over the modified array and calculate the cumulative sum
    for i in range(1, n + 1):
        current_sum += modified_array[i]
        max_element = max(max_element, current_sum)

    return max_element
```

## Example Test Cases

```python
test_case_1 = {
    "n": 5,
    "queries": [[1, 2], [2, 4]]
}
expected_result_1 = 2

test_case_2 = {
    "n": 5,
    "queries": [[1, 2], [2, 4], [1, 5]]
}
expected_result_2 = 3

test_case_3 = {
    "n": 5,
    "queries": [[1, 2], [2, 3], [1, 5]]
}
expected_result_3 = 3
```

## Alternative Approaches

1. **Using Segment Tree:** This approach is more efficient for a large number of queries. It allows us to perform range updates in logarithmic time.
2. **Using Prefix Sum Array:** This approach is similar to the given approach, but instead of using an array of size N+2, we use an array of size N+1. We calculate the prefix sum of the modified array and then find the maximum element from the prefix sum array.

# Connect with me: https://github.com/ohkrahul
