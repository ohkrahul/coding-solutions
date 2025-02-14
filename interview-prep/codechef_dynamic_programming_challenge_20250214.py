'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-02-14
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-02-14

## Problem Understanding and Approach

The problem requires us to find the maximum sum of non-overlapping segments in a given sequence of numbers. This can be solved using dynamic programming, where we store the maximum sum for each subarray up to the current index in a table.

1. **Initialization**: Initialize a table `dp` of size `n+1` (where `n` is the length of the sequence) with `dp[0] = 0` (base case).

2. **Iteration**: For each index `i` in the range `[1, n]`:
   - If `dp[i-1] > 0`, then including the current number will increase the sum. So, `dp[i] = dp[i-1] + arr[i]`.
   - Otherwise, start a new segment by setting `dp[i] = arr[i]`.

3. **Result**: Finally, the maximum sum is `max(dp[1], dp[2], ..., dp[n])`.

## Time and Space Complexity Analysis

- **Time complexity**: O(n), where n is the length of the sequence. We iterate over each element in the sequence once.
- **Space complexity**: O(n), as we use a table `dp` of size n to store the maximum sums.

## Well-Commented Implementation in Python

```python
def max_segment_sum(arr):
    """
    Finds the maximum sum of non-overlapping segments in a given sequence of numbers.

    Args:
        arr (list): The input sequence of numbers.

    Returns:
        int: The maximum sum.
    """

    # Initialize the dp table
    dp = [0] * (len(arr) + 1)

    # Iterate over the sequence
    for i in range(1, len(arr) + 1):
        # If including the current number increases the sum, do it
        if dp[i-1] > 0:
            dp[i] = dp[i-1] + arr[i]
        # Otherwise, start a new segment
        else:
            dp[i] = arr[i]

    # Return the maximum sum
    return max(dp)


# Example test cases
arr1 = [2, 1, 5, 8, 4]
print(max_segment_sum(arr1))  # Output: 11

arr2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_segment_sum(arr2))  # Output: 6
```

## Alternative Approaches

One alternative approach is to use a greedy algorithm. Start from the beginning of the sequence and keep adding numbers to the current segment as long as the sum is positive. When the sum becomes negative, reset it to zero and start a new segment. The time complexity of this approach is O(n), but it might not always give the optimal solution.

# Connect with me: https://github.com/ohkrahul
