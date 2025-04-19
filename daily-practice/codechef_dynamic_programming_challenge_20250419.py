'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-04-19
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-04-19

```python
# Problem: Maximum Sum Subsequence with no adjacent elements

# Platform: CodeChef (Hypothetical problem - inspired by classic DP problems)
# Difficulty: Hard

# Description: You are given a sequence of N integers A1, A2, ..., AN. You need to find the maximum sum of a subsequence of this sequence such that no two adjacent elements in the original sequence are selected in the subsequence.


# 1. Problem Understanding and Approach

# We can solve this using dynamic programming.  Let dp[i] represent the maximum sum subsequence ending at index i (or including A[i]).  There are two possibilities for dp[i]:

# 1. Include A[i]: In this case, we can't include A[i-1], so we must take the maximum sum up to A[i-2] and add A[i]. So, dp[i] = dp[i-2] + A[i].
# 2. Exclude A[i]: In this case, the maximum sum up to i is the same as the maximum sum up to i-1.  So, dp[i] = dp[i-1].

# We take the maximum of these two possibilities.  The base cases are dp[0] = A[0] (if the sequence has at least one element) and dp[1] = max(A[0], A[1]) (if the sequence has at least two elements).

# 2. Time and Space Complexity Analysis

# Time Complexity: O(N) - We iterate through the sequence once.
# Space Complexity: O(N) -  We use a DP array of size N.  This can be optimized to O(1) as we only need the previous two values.

# 3. Well-commented Implementation

def max_sum_subsequence_no_adjacent(A):
    """
    Calculates the maximum sum subsequence with no adjacent elements.

    Args:
        A: A list of integers.

    Returns:
        The maximum sum.
    """
    n = len(A)

    if n == 0:
        return 0
    elif n == 1:
        return A[0]
    
    dp = [0] * n
    dp[0] = A[0]
    dp[1] = max(A[0], A[1])


    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + A[i]) # Either exclude A[i] or include it

    return dp[n - 1]


# 4. Example Test Cases

print(max_sum_subsequence_no_adjacent([5, 5, 10, 100, 10, 5])) # Output: 110 (5 + 100 + 5)
print(max_sum_subsequence_no_adjacent([1, 2, 3])) # Output: 4 (1 + 3)
print(max_sum_subsequence_no_adjacent([1, 20, 3])) # Output: 20
print(max_sum_subsequence_no_adjacent([2, 7, 9, 3, 1])) # Output: 12 (2+9+1 or 7 + 1)
print(max_sum_subsequence_no_adjacent([]))  # Output: 0


# 5. Alternative Approaches (Space Optimization)

def max_sum_subsequence_no_adjacent_optimized(A):
    """
    Space-optimized version using only two variables.
    """
    n = len(A)

    if n == 0:
        return 0
    elif n == 1:
        return A[0]
    
    prev_prev = A[0]
    prev = max(A[0], A[1])


    for i in range(2, n):
        curr = max(prev, prev_prev + A[i])
        prev_prev = prev
        prev = curr

    return prev



print(max_sum_subsequence_no_adjacent_optimized([5, 5, 10, 100, 10, 5])) # Output: 110
print(max_sum_subsequence_no_adjacent_optimized([1, 2, 3])) # Output: 4
print(max_sum_subsequence_no_adjacent_optimized([1, 20, 3])) # Output: 20
print(max_sum_subsequence_no_adjacent_optimized([2, 7, 9, 3, 1])) # Output: 12



```

# Connect with me: https://github.com/ohkrahul
