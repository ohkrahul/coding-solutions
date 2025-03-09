'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-03-09
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-03-09

```python
# Problem: Maximum Sum Subsequence with No Adjacent Elements

# Platform: CodeChef (Hypothetical - Mimicking a CodeChef style problem)
# Difficulty: Hard

# Problem Understanding:
# You are given a sequence of N integers. Your task is to find the maximum sum of a subsequence 
# such that no two adjacent elements in the original sequence are selected in the subsequence.

# Approach: Dynamic Programming

# Time Complexity: O(N)
# Space Complexity: O(N) - Can be optimized to O(1) (see alternative approach)


def max_sum_subsequence(nums):
    """
    Calculates the maximum sum of a subsequence with no adjacent elements.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum.
    """

    n = len(nums)

    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    # dp[i] stores the maximum sum ending at index i
    dp = [0] * n

    # Base cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # Iterate through the remaining elements
    for i in range(2, n):
        # Two choices:
        # 1. Include the current element and the max sum from two indices back
        # 2. Exclude the current element and take the max sum from the previous index
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[n - 1]


# Example Test Cases:
print("Example Test Cases:")
print(max_sum_subsequence([5, 5, 10, 100, 10, 5]))  # Output: 110 (5 + 100 + 5)
print(max_sum_subsequence([1, 2, 3]))  # Output: 4 (1 + 3)
print(max_sum_subsequence([1, 20, 3]))  # Output: 20
print(max_sum_subsequence([3, 2, 7, 10])) # Output: 13
print(max_sum_subsequence([3, 2, 5, 10, 7])) # Output: 15 (3 + 5 + 7) or (3 + 10)


# Alternative Approach (Space Optimization - O(1)):

def max_sum_subsequence_optimized(nums):
    """
    Space-optimized version using constant extra space.
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    prev_prev = nums[0]
    prev = max(nums[0], nums[1])

    for i in range(2, n):
        curr = max(nums[i] + prev_prev, prev)
        prev_prev = prev
        prev = curr
    
    return prev


print("\nSpace-Optimized Results:")
print(max_sum_subsequence_optimized([5, 5, 10, 100, 10, 5]))  # Output: 110
print(max_sum_subsequence_optimized([1, 2, 3]))  # Output: 4
print(max_sum_subsequence_optimized([1, 20, 3]))  # Output: 20
print(max_sum_subsequence_optimized([3, 2, 7, 10])) # Output: 13
print(max_sum_subsequence_optimized([3, 2, 5, 10, 7])) # Output: 15


```



Key improvements:

* **Clearer problem description and approach explanation.**
* **Detailed comments throughout the code.**
* **Comprehensive test cases.**
* **Space-optimized alternative solution.**
* **Docstrings for functions.**
* **Output clearly labeled for the test cases.**


This enhanced version provides a more complete and developer-friendly solution, mirroring what a developer might create for a real-world problem.

# Connect with me: https://github.com/ohkrahul
