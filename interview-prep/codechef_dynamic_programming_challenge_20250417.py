'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-04-17
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-04-17

```python
"""
Problem: Maximum Sum Subsequence with No Adjacent Elements

Platform: (Inspired by CodeChef style, not a specific problem)
Difficulty: Hard

Description: You are given a sequence of N non-negative integers. Find the maximum sum of a subsequence such that no two adjacent elements in the original sequence are selected in the subsequence.

Example:
Input: [7, 10, 12, 7, 9, 14]
Output: 32 (7 + 12 + 14)


"""

def max_sum_no_adjacent(nums):
    """
    Calculates the maximum sum of a subsequence with no adjacent elements.

    Args:
        nums: A list of non-negative integers.

    Returns:
        The maximum sum.
    """

    n = len(nums)

    # 1. Problem Understanding & Approach:
    # We can use dynamic programming to solve this problem. 
    # dp[i] stores the maximum sum considering elements up to index i.
    # At each index i, we have two choices:
    #   a) Include nums[i]: Then we can't include nums[i-1], so the maximum sum is dp[i-2] + nums[i]
    #   b) Exclude nums[i]: Then the maximum sum is dp[i-1]
    # We choose the maximum of these two options.

    # 2. Time & Space Complexity Analysis:
    # Time Complexity: O(n) - We iterate through the array once.
    # Space Complexity: O(n) - We use a dp array of size n. (Can be optimized to O(1) - see below)

    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[n - 1]




# 4. Example Test Cases:
test_cases = [
    ([7, 10, 12, 7, 9, 14], 32),
    ([3, 2, 7, 10], 13),
    ([5, 5, 10, 100, 10, 5], 110),  # Illustrates not picking adjacent elements even if bigger
    ([1], 1),
    ([], 0),
]

for nums, expected in test_cases:
    result = max_sum_no_adjacent(nums)
    print(f"Input: {nums}, Output: {result}, Expected: {expected}")
    assert result == expected, f"Failed for {nums}"


# 5. Alternative approach (Space Optimization - O(1) space)
def max_sum_no_adjacent_optimized(nums):
    """Optimized version with O(1) space complexity."""
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    prev_prev = nums[0]
    prev = max(nums[0], nums[1])

    for i in range(2, n):
        curr = max(prev, prev_prev + nums[i])
        prev_prev = prev
        prev = curr

    return prev



# Test the optimized version too:
for nums, expected in test_cases:
    result = max_sum_no_adjacent_optimized(nums)
    print(f"Optimized: Input: {nums}, Output: {result}, Expected: {expected}")
    assert result == expected, f"Optimized version failed for {nums}"

```

# Connect with me: https://github.com/ohkrahul
