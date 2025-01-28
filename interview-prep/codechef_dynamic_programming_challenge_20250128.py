'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-01-28
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-01-28

## Problem: Dynamic Programming Challenge (CodeChef)

### Problem understanding and approach

The problem asks to find the length of the longest increasing subsequence (LIS) of a given sequence of numbers. A LIS is a subsequence of the original sequence, which is sorted in ascending order and has the maximum possible length.

One approach to solving this problem is using dynamic programming. We can define a dp array of the same length as the original sequence, where dp[i] represents the length of the longest increasing subsequence ending at index i.

We can initialize the dp array as follows:
```
dp[0] = 1
```
This is because the longest increasing subsequence ending at index 0 is always of length 1.

We can then iterate through the original sequence, and for each index i, we can consider all the previous indices j such that a[j] < a[i]. For each such j, we can update dp[i] as follows:
```
dp[i] = max(dp[i], dp[j] + 1)
```

This is because if a[j] < a[i], then we can extend the longest increasing subsequence ending at index j by adding a[i] to it, and the length of the resulting increasing subsequence will be dp[j] + 1.

After iterating through the entire sequence, the maximum value in the dp array will be the length of the longest increasing subsequence of the original sequence.

### Time and space complexity analysis

The time complexity of the above solution is O(n^2), where n is the length of the original sequence. This is because we iterate through the original sequence once, and for each index i, we consider all the previous indices j such that a[j] < a[i].

The space complexity of the above solution is O(n), as we use an array of length n to store the dp array.

### Well-commented implementation

```python
def longest_increasing_subsequence(arr):
  """
  Finds the length of the longest increasing subsequence of a given sequence of numbers.

  Args:
    arr: The sequence of numbers.

  Returns:
    The length of the longest increasing subsequence.
  """

  # Initialize the dp array.
  dp = [1] * len(arr)

  # Iterate through the original sequence.
  for i in range(1, len(arr)):
    # Consider all the previous indices j such that a[j] < a[i].
    for j in range(i):
      if arr[j] < arr[i]:
        # Update dp[i] as the maximum of its current value and dp[j] + 1.
        dp[i] = max(dp[i], dp[j] + 1)

  # Return the maximum value in the dp array.
  return max(dp)


# Example test cases.
print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))  # Output: 6
print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]))  # Output: 5
print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50]))  # Output: 4
```

### Alternative approaches

There are other approaches to solving this problem, such as using a binary search tree or a segment tree. These approaches can have better time complexity than the dynamic programming approach, but they are also more complex to implement.

# Connect with me: https://github.com/ohkrahul
