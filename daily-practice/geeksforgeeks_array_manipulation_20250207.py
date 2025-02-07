'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-07
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-07

## 1. Problem understanding and approach

### Problem Understanding

Given an array of size `N`, perform the following operations `Q` times:
- Increase the value of every element of any subarray `[L, R]` by `V`.

The task is to find the maximum element in the array after performing all the operations.

### Approach

We can use a cumulative sum approach to efficiently perform this task. The key insight is that the change to elements in a subarray `[L, R]` by `V` can be represented by adding `V` to the cumulative sum at index `L-1` and subtracting `V` from the cumulative sum at index `R`.

By maintaining a cumulative sum array, we can efficiently update the array. The maximum value in the array can be found by simply finding the maximum value in the cumulative sum array.

## 2. Time and Space Complexity Analysis

### Time Complexity

The time complexity of our approach is `O(N) + O(Q)` where `N` is the size of the array and `Q` is the number of operations.

### Space Complexity

The space complexity is `O(N)`, as we need to store the cumulative sum array.

## 3. Well-commented implementation

```python
def array_manipulation(N: int, Q: int, queries: list) -> int:
    """
    Given an array of size N, perform the following operations Q times:
    - Increase the value of every element of any subarray [L, R] by V.

    Find the maximum element in the array after performing all the operations.

    Args:
        N: The size of the array
        Q: The number of operations
        queries: A list of tuples representing the operations, where each tuple (L, R, V) represents increasing the 
            value of every element of the subarray [L, R] by V.

    Returns:
        The maximum element in the array after performing all the operations.
    """

    # Create a cumulative sum array of size N+1
    cumulative_sum = [0] * (N + 1)

    # Update the cumulative sum array based on the queries
    for L, R, V in queries:
        cumulative_sum[L - 1] += V  # Add V to the left end of the subarray
        cumulative_sum[R] -= V  # Subtract V from the right end of the subarray

    # Calculate the actual array by performing cumulative sum
    array = [0] * N
    for i in range(N):
        array[i] = cumulative_sum[i]
        if i > 0:
            array[i] += array[i - 1]

    # Find the maximum element in the array
    max_element = max(array)

    return max_element
```

## 4. Example test cases

### Example 1

```
Input:
N = 5, Q = 3
queries = [(1, 2, 10), (2, 4, 5), (3, 5, 2)]

Output:
17
Explanation:
After performing the operations
[1, 2, 10] => Increase the value of all elements in the subarray [1, 2] by 10.
[2, 4, 5] => Increase the value of all elements in the subarray [2, 4] by 5.
[3, 5, 2] => Increase the value of all elements in the subarray [3, 5] by 2.

The resulting array is [12, 15, 17, 12, 7]. The maximum element is 17.
```

### Example 2

```
Input:
N = 10, Q = 4
queries = [(2, 6, 8), (3, 5, 7), (1, 8, 1), (5, 9, 2)]

Output:
10
Explanation:
After performing the operations
[2, 6, 8] => Increase the value of all elements in the subarray [2, 6] by 8.
[3, 5, 7] => Increase the value of all elements in the subarray [3, 5] by 7.
[1, 8, 1] => Increase the value of all elements in the subarray [1, 8] by 1.
[5, 9, 2] => Increase the value of all elements in the subarray [5, 9] by 2.

The resulting array is [1, 9, 10, 8, 7, 9, 3, 2, 2, 2]. The maximum element is 10.
```

## 5. Alternative approaches

### Segment Tree approach

We can also use a segment tree to efficiently perform the updates and find the maximum element. The segment tree approach has a time complexity of `O(N log N) + O(Q log N)`, which is more efficient for large arrays and a large number of updates.

However, the cumulative sum approach is simpler to implement and is sufficient for most practical scenarios.

# Connect with me: https://github.com/ohkrahul
