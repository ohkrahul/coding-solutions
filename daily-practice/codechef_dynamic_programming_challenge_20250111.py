'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-01-11
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-01-11

## Problem Understanding and Approach

The problem is a classic Dynamic Programming problem. We can define the following states:

```
dp[i][j] = the maximum sum of the subarray from index i to index j
```

We can compute the dp table as follows:

```
dp[i][j] = max(dp[i][j-1] + a[j], a[j])
```

Where a[j] is the value at index j.

## Time and Space Complexity Analysis

The time complexity of the algorithm is O(n^2), where n is the length of the array. The space complexity is O(n^2).

## Well-Commented Implementation

```python
def max_subarray_sum(a):
    """
    Finds the maximum sum of a subarray in a given array.

    Args:
        a (list): The array to search.

    Returns:
        int: The maximum sum of a subarray in the array.
    """

    # Initialize the dp table.
    dp = [[0 for _ in range(len(a))] for _ in range(len(a))]

    # Compute the dp table.
    for i in range(len(a)):
        for j in range(len(a)):
            if i == 0:
                dp[i][j] = a[j]
            else:
                dp[i][j] = max(dp[i][j-1] + a[j], a[j])

    # Return the maximum sum of a subarray.
    return max(max(row) for row in dp)
```

## Example Test Cases

```
assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray_sum([1, 2, 3, 4, 5]) == 15
assert max_subarray_sum([1, -2, 1, 2]) == 2
```

## Alternative Approaches

There are several alternative approaches to this problem, including:

* **Kadane's algorithm**: This is a linear-time algorithm that finds the maximum sum of a subarray in O(n) time.
* **Divide-and-conquer**: This algorithm divides the array into smaller subarrays and recursively finds the maximum sum of a subarray in each subarray. The time complexity of this algorithm is O(n log n).

# Connect with me: https://github.com/ohkrahul
