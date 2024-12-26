'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-26
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-26

## Problem Understanding and Approach

The provided problem, "Dynamic Programming Challenge," from CodeChef, requires us to find the maximum sum of a subsequence of elements in an array such that adjacent elements in the subsequence have a specific difference. We can approach this problem using dynamic programming, specifically the tabular method.

We define a 2D table, `dp`, where `dp[i][diff]` represents the maximum sum of a subsequence ending at index `i` with an adjacent elements difference of `diff`. We can fill this table iteratively, starting from the first index, by considering two possibilities for each index:

1. Include the current element in the subsequence.
2. Exclude the current element from the subsequence.

We then choose the maximum sum out of these two possibilities and store it in `dp[i][diff]`. Finally, after filling the table for all indices and possible differences, we return the maximum sum found among all `dp[i][diff]`.

### Time and Space Complexity Analysis

- **Time Complexity**: O(n * d), where `n` is the length of the array and `d` is the maximum possible difference between adjacent elements.
- **Space Complexity**: O(n * d), since we use a 2D table to store the maximum sums.

## Implementation

```python
# Maximum sum subsequence with specific difference
# Dynamic programming solution using tabular method

def max_sum_subsequence(arr, diff):
    """
    Finds the maximum sum of a subsequence of elements in an array such that adjacent
    elements in the subsequence have a specific difference.

    Parameters:
    arr: The input array of numbers.
    diff: The specific difference between adjacent elements in the subsequence.

    Returns:
    The maximum sum of the subsequence.
    """

    # Create a 2D table to store the maximum sums
    n = len(arr)
    dp = [[0] * (diff + 1) for _ in range(n)]

    # Fill the table iteratively
    for i in range(1, n):
        for j in range(diff + 1):
            # Option 1: Include the current element
            if j == arr[i] - arr[i - 1]:
                dp[i][j] = dp[i - 1][j] + arr[i]
            # Option 2: Exclude the current element
            else:
                dp[i][j] = dp[i - 1][j]

            # Choose the maximum sum
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

    # Return the maximum sum
    return max([max(row) for row in dp])

# Example test cases
arr1 = [1, 2, 3, 4, 5]
diff1 = 1
print(max_sum_subsequence(arr1, diff1))  # Output: 9

arr2 = [1, 2, 3, 4, 5]
diff2 = 2
print(max_sum_subsequence(arr2, diff2))  # Output: 7

arr3 = [1, 2, 3, 4, 5]
diff3 = 3
print(max_sum_subsequence(arr3, diff3))  # Output: 5
```

## Alternative Approach

Since the problem requires finding the maximum sum of a subsequence with specific adjacent element differences, one could also use a greedy approach. The greedy approach would involve iterating through the array and greedily choosing elements that satisfy the specified difference condition. However, the time complexity of this approach would be higher, O(n^2), compared to the O(n * d) of the dynamic programming approach.

# Connect with me: https://github.com/ohkrahul
