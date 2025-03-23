'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-03-23
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-03-23

```python
# Problem: Maximum Sum Subsequence with Non-Adjacent Elements

# Platform: CodeChef (Hypothetical - Similar problems exist)
# Difficulty: Hard

# Description:
# You are given a sequence of N non-negative integers. Find the maximum sum of a subsequence such that no two elements in the subsequence are adjacent in the original sequence.


def max_sum_non_adjacent(nums):
    """
    Calculates the maximum sum of a non-adjacent subsequence.

    Args:
        nums: A list of non-negative integers.

    Returns:
        The maximum sum.
    """

    n = len(nums)

    # Base cases:
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])


    # dp[i] stores the maximum sum ending at index i (inclusive or exclusive of nums[i])
    dp = [0] * n

    # Initialize the first two elements of dp:
    dp[0] = nums[0] 
    dp[1] = max(nums[0], nums[1])

    # Iterate and build the dp table:
    for i in range(2, n):
        # Option 1: Include nums[i].  In this case, we cannot include nums[i-1]
        # so we take the max sum up to i-2 and add nums[i].
        # Option 2: Exclude nums[i]. In this case, the maximum sum is the same as the
        # maximum sum up to i-1.
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1]) 

    return dp[n - 1]



# 1. Problem Understanding and Approach:
#    We use dynamic programming to solve this problem.  `dp[i]` stores the maximum 
#    sum of a non-adjacent subsequence ending at index i (inclusive or exclusive of nums[i]).
#    We have two choices at each index i: include nums[i] or exclude it.
#    This leads to the recurrence relation used in the code.

# 2. Time and Space Complexity Analysis:
#    Time Complexity: O(N) - We iterate through the list once.
#    Space Complexity: O(N) - We use a DP table of size N.  (Can be optimized to O(1) 
#                                by storing only the previous two values)

# 3. Example Test Cases:
print(max_sum_non_adjacent([2, 7, 9, 3, 1]))  # Output: 12 (2 + 9 + 1)
print(max_sum_non_adjacent([5, 5, 10, 100, 10, 5])) # Output: 110 (5 + 100 + 5)
print(max_sum_non_adjacent([1, 2, 3])) # Output: 4
print(max_sum_non_adjacent([1, 20, 3])) # Output: 20
print(max_sum_non_adjacent([5, 1, 1, 5]))  # Output: 10 (5 + 5)

# 5. Alternative Approaches (Space Optimization):
#    We can optimize the space complexity to O(1) by storing only the previous two values 
#    of the DP table instead of the entire table. This is possible because the current 
#    DP value only depends on the previous two.


def max_sum_non_adjacent_optimized(nums):
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]

    prev_prev = nums[0]
    prev = max(nums[0], nums[1])

    for i in range(2, n):
        curr = max(nums[i] + prev_prev, prev)
        prev_prev = prev
        prev = curr
    return prev



print(max_sum_non_adjacent_optimized([2, 7, 9, 3, 1]))  # Output: 12
print(max_sum_non_adjacent_optimized([5, 5, 10, 100, 10, 5])) # Output: 110



```

# Connect with me: https://github.com/ohkrahul
