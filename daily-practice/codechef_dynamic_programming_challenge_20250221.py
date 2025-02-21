'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-02-21
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-02-21

## Problem Understanding and Approach

The problem is to find the longest increasing subsequence (LIS) in an array of numbers. A subsequence is a sequence of elements that appears in the original sequence in the same order, but not necessarily consecutively. An LIS is a subsequence that is both increasing and has the maximum possible length.

We can solve this problem using dynamic programming. Let dp[i] represent the length of the longest increasing subsequence ending at index i. We can compute dp[i] as follows:

```
dp[i] = 1 + max(dp[j]) for all j < i such that a[j] < a[i]
```

In other words, dp[i] is the maximum of 1 plus the length of the longest increasing subsequence ending at any index j less than i such that a[j] < a[i].

## Time and Space Complexity Analysis

The time complexity of this solution is O(n^2), where n is the length of the input array. This is because we need to consider all possible pairs of indices (i, j) such that j < i and a[j] < a[i]. The space complexity of this solution is O(n), as we need to store the values of dp[i] for all i.

## Well-Commented Implementation

```python
def longest_increasing_subsequence(a):
  """
  Finds the longest increasing subsequence in an array of numbers.

  Parameters:
    a: An array of numbers.

  Returns:
    The length of the longest increasing subsequence.
  """

  n = len(a)
  dp = [1] * n

  for i in range(1, n):
    for j in range(i):
      if a[j] < a[i]:
        dp[i] = max(dp[i], dp[j] + 1)

  return max(dp)


# Example test cases
a = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(a))  # 6

a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_increasing_subsequence(a))  # 6

a = [1, 2, 3, 4, 5, 6]
print(longest_increasing_subsequence(a))  # 6

a = [6, 5, 4, 3, 2, 1]
print(longest_increasing_subsequence(a))  # 1
```

## Alternative Approaches

There are several alternative approaches to solving this problem, including:

* **Binary search:** We can use binary search to find the longest increasing subsequence in O(n log n) time.
* **Tree DP:** We can use tree DP to solve this problem in O(n log n) time.
* **Segment tree:** We can use a segment tree to solve this problem in O(n log n) time.

# Connect with me: https://github.com/ohkrahul
