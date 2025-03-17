'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-03-17
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-03-17

```python
# Problem: Maximum Sum Subsequence with No Adjacent Elements

# Platform: CodeChef (Hypothetical -  adapted for a more general audience)
# Difficulty: Hard

# Description:
# You are given a sequence of N non-negative integers A[1], A[2], ..., A[N]. 
# Your task is to find the maximum sum of a subsequence such that no two elements in the chosen subsequence are adjacent in the original sequence.

# 1. Problem Understanding and Approach:

# This problem exhibits optimal substructure and overlapping subproblems, making it suitable for dynamic programming. 
# We can define dp[i] as the maximum sum subsequence ending at index i (or including element A[i]). 

# Recurrence relation:
# dp[i] = max(
#     dp[i-1],  # Exclude A[i] - The max sum so far without A[i]
#     dp[i-2] + A[i],  # Include A[i] - Max sum ending two positions before plus A[i] 
#     A[i]       # If i < 2, A[i] itself could be the maximum
# )

# Base Cases:
# dp[0] = A[0] if N > 0 else 0
# dp[1] = max(A[0], A[1]) if N > 1 else dp[0]

# 2. Time and Space Complexity Analysis:

# Time Complexity: O(N) - We iterate through the array once.
# Space Complexity: O(N) - Can be optimized to O(1) (see alternative approach)

# 3. Well-commented Implementation:


def max_sum_non_adjacent(A):
    """
    Calculates the maximum sum of a non-adjacent subsequence.

    Args:
        A: A list of non-negative integers.

    Returns:
        The maximum sum.
    """
    n = len(A)
    if n == 0:
        return 0

    dp = [0] * n

    dp[0] = A[0]  # Base case
    if n > 1:
        dp[1] = max(A[0], A[1]) # Base case

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + A[i], A[i])

    return dp[n-1]


# 4. Example Test Cases:


print(max_sum_non_adjacent([5, 5, 10, 100, 10, 5]))  # Output: 110 (5+100+5)
print(max_sum_non_adjacent([1, 2, 3]))  # Output: 4 (1+3)
print(max_sum_non_adjacent([1, 20, 3]))  # Output: 20
print(max_sum_non_adjacent([1]))  # Output: 1
print(max_sum_non_adjacent([]))  # Output: 0

# 5. Alternative Approaches (Space Optimization):

# We can optimize the space complexity to O(1) by storing only the previous two values of dp:

def max_sum_non_adjacent_optimized(A):
    n = len(A)
    if n == 0:
        return 0

    prev_prev = 0
    prev = A[0] if n > 0 else 0

    for i in range(1, n):
        curr = max(prev, prev_prev + A[i], A[i])
        prev_prev = prev
        prev = curr

    return prev

print("Optimized:")
print(max_sum_non_adjacent_optimized([5, 5, 10, 100, 10, 5])) # Output: 110
print(max_sum_non_adjacent_optimized([1, 2, 3]))  # Output: 4
print(max_sum_non_adjacent_optimized([1, 20, 3]))  # Output: 20


```

# Connect with me: https://github.com/ohkrahul
