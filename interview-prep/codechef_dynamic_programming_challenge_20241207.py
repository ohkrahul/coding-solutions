'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-07
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-07

## Problem Understanding and Approach

The problem statement provides us with a sequence of numbers and asks us to maximize the MEX of all subarrays. MEX (Minimum Excluded) of an array is the smallest non-negative integer that does not appear in the array.

To solve this problem, we can use dynamic programming. Let `dp[i][j][mex]` be the MEX of the subarray from index `i` to `j` if the last number added to the subarray was `mex`. We can compute `dp[i][j][mex]` as follows:

```
dp[i][j][mex] = min(dp[i + 1][j][mex], dp[i][j - 1][mex], mex)
```

* `dp[i + 1][j][mex]`: This is the MEX of the subarray from index `i + 1` to `j` if the last number added to the subarray was `mex`.
* `dp[i][j - 1][mex]`: This is the MEX of the subarray from index `i` to `j - 1` if the last number added to the subarray was `mex`.
* `mex`: This is the MEX of the subarray from index `i` to `j` if the last number added to the subarray was not `mex`.

We can compute the MEX of the entire sequence by finding the minimum MEX for all possible values of `mex`.

```
max_mex = min(dp[0][n - 1][mex] for mex in range(n))
```

## Time and Space Complexity Analysis

The time complexity of this solution is `O(n^3)`, where `n` is the length of the sequence. This is because we need to compute `dp[i][j][mex]` for all possible values of `i`, `j`, and `mex`.

The space complexity of this solution is `O(n^3)`, as we need to store the `dp` table.

## Well-commented Implementation

```python
def max_mex_subarray(arr):
    """
    Finds the maximum MEX of all subarrays in a given array.

    Args:
        arr (list): The input array.

    Returns:
        int: The maximum MEX of all subarrays.
    """

    n = len(arr)
    dp = [[[-1 for k in range(n)] for j in range(n)] for i in range(n)]

    def solve(i, j, mex):
        if i > j:
            return mex

        if dp[i][j][mex] != -1:
            return dp[i][j][mex]

        dp[i][j][mex] = min(solve(i + 1, j, mex), solve(i, j - 1, mex), mex)

        if arr[i] != mex:
            dp[i][j][mex] = min(dp[i][j][mex], solve(i + 1, j, arr[i]))
            dp[i][j][mex] = min(dp[i][j][mex], solve(i, j - 1, arr[i]))

        return dp[i][j][mex]

    max_mex = min(solve(0, n - 1, mex) for mex in range(n))

    return max_mex
```

## Example Test Cases

```
assert max_mex_subarray([1, 2, 3, 4, 5]) == 5
assert max_mex_subarray([1, 2, 3, 4, 5, 6]) == 6
assert max_mex_subarray([1, 2, 3, 4, 5, 6, 7]) == 7
assert max_mex_subarray([1, 2, 3, 4, 5, 6, 7, 8]) == 8
assert max_mex_subarray([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
```

## Alternative Approaches

One alternative approach to this problem is to use a greedy algorithm. The greedy algorithm works as follows:

1. Sort the array in ascending order.
2. Iterate over the array and add each number to the subarray if it is greater than the MEX of the current subarray.

The time complexity of the greedy algorithm is `O(n log n)`, where `n` is the length of the sequence. The space complexity of the greedy algorithm is `O(n)`, as we need to store the sorted array.

The greedy algorithm is not always optimal, but it is often a good approximation for the optimal solution.

# Connect with me: https://github.com/ohkrahul
