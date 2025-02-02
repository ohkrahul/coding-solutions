'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-02-02
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-02-02

## Problem Understanding and Approach

### Problem Summary

Given a sequence of integers, the problem is to find the longest increasing subsequence (LIS) within the sequence. LIS is a subsequence where each element is greater than the previous one.

### Approach

The problem can be solved using dynamic programming. We create an array `dp` of the same length as the input sequence, where `dp[i]` stores the length of the longest increasing subsequence ending at index `i`.

We initialize the `dp` array to 1 for all elements. Then, we iterate over the sequence from left to right and for each element at index `i`, we check all previous elements at indices `j < i` and if `nums[j] < nums[i]`, then we update `dp[i]` to `max(dp[i], dp[j] + 1)`.

### Time and Space Complexity Analysis

- **Time Complexity**: O(n^2), where n is the length of the input sequence. We iterate over the sequence once to initialize the `dp` array and once to perform the dynamic programming computation.
- **Space Complexity**: O(n), as we create an array of size n to store the LIS lengths.

## Well-Commented Implementation

```python
def longest_increasing_subsequence(nums):
  """
  Finds the longest increasing subsequence (LIS) in a given sequence.

  Args:
    nums: A list of integers.

  Returns:
    The length of the LIS.
  """

  n = len(nums)
  dp = [1] * n

  for i in range(1, n):
    for j in range(i):
      if nums[j] < nums[i]:
        dp[i] = max(dp[i], dp[j] + 1)

  return max(dp)


# Example test cases
nums1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(nums1))  # Output: 6

nums2 = [1, 2, 3, 4, 5]
print(longest_increasing_subsequence(nums2))  # Output: 5

nums3 = [50, 3, 10, 7, 40, 80]
print(longest_increasing_subsequence(nums3))  # Output: 4
```

## Alternative Approaches

Another approach to solve this problem is using binary search. We can maintain a sorted list of increasing subsequence lengths and use binary search to find the longest increasing subsequence ending at each index in the input sequence. This approach has a time complexity of O(n log n), but it requires more space as we need to store the sorted list.

# Connect with me: https://github.com/ohkrahul
