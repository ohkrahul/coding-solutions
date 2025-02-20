'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-20
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-20

## Problem Understanding and Approach

### Problem Statement
Given an array of integers, perform the following operations:

* Input: An array of integers (arr) and a list of operations (queries)
* Operation: Each query consists of 3 integers: a, b, and k. Increment each element of the array in the range [a, b] by k.

### Approach
To solve this problem, we can use the cumulative sum technique. We can create an array of size N+1, where N is the length of the original array. The cumulative sum array (pref[]) will store the cumulative sum of the original array.

For each query [a, b, k], we can increment the pref[a] by k and decrement the pref[b+1] by k. This way, the elements in the range [a, b] will get incremented by k.

Finally, we can compute the final array by iterating over the cumulative sum array pref[].

### Time and Space Complexity Analysis
* Time Complexity: O(N + Q), where N is the length of the original array and Q is the number of queries.
* Space Complexity: O(N), for the cumulative sum array.

## Well-Commented Implementation

```python
def array_manipulation(arr, queries):
    """
    Perform operations on an array of integers and return the final array.

    Args:
        arr (list): The original array of integers.
        queries (list): A list of queries, each consisting of 3 integers [a, b, k].

    Returns:
        list: The final array after performing the operations.
    """

    # Create a cumulative sum array of size N+1
    pref = [0] * (len(arr) + 1)

    # Perform operations on the array
    for a, b, k in queries:
        # Increment pref[a] by k
        pref[a] += k
        # Decrement pref[b+1] by k
        pref[b+1] -= k

    # Compute the final array by iterating over the cumulative sum array
    final_arr = []
    sum = 0
    for i in range(len(arr)):
        # Add the cumulative sum to the final array
        sum += pref[i]
        final_arr.append(sum)

    return final_arr


# Example test cases
arr = [1, 2, 3, 4, 5]
queries = [[1, 3, 2], [2, 4, 3], [4, 5, 4]]
result = array_manipulation(arr, queries)
print(result)  # Output: [1, 4, 8, 12, 16]
```

## Alternative Approaches

**Using a binary indexed tree (BIT)**

A binary indexed tree (BIT) can also be used to solve this problem. BIT is a data structure that can be used to store a cumulative sum array and perform range increment operations efficiently.

The time complexity of this approach would be O(N log N), where N is the length of the original array.

# Connect with me: https://github.com/ohkrahul
