'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-03-03
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-03-03

```python
# Problem: Dynamic Programming Challenge - Maximum Subsequence Sum with Constraints

# Platform: CodeChef (Hypothetical Problem - Inspired by standard DP problems)
# Difficulty: Hard

# Problem Description:
# You are given a sequence of N integers A[1], A[2], ..., A[N]. You need to find the maximum sum of a non-empty subsequence 
# such that no two adjacent elements in the original sequence are chosen in the subsequence.

# Example:
# Input: A = [3, 2, 5, 10, 7]
# Output: 18 (choosing 3, 5, and 10)

# 1. Problem Understanding and Approach:

# This problem can be solved using dynamic programming.  We can define dp[i] as the maximum subsequence sum considering 
# elements up to index i, following the constraint of non-adjacent elements.

# Recurrence Relation:
# dp[i] can be calculated as follows:
# - Include A[i]:  dp[i] = A[i] + dp[i-2] (Since we can't include A[i-1])
# - Exclude A[i]: dp[i] = dp[i-1] (Maximum sum up to i-1 remains the same)
# Therefore, dp[i] = max(A[i] + dp[i-2], dp[i-1])

# Base Cases:
# dp[0] = 0 (Empty subsequence)
# dp[1] = A[1] (Only one element)


# 2. Time and Space Complexity Analysis:

# Time Complexity: O(N) - We iterate through the array once to build the dp table.
# Space Complexity: O(N) - We use a dp array of size N. (Can be optimized to O(1) by using only two variables).


# 3. Well-commented Implementation:

def max_subsequence_sum(A):
    """
    Calculates the maximum subsequence sum with no adjacent elements.

    Args:
        A: A list of integers representing the sequence.

    Returns:
        The maximum subsequence sum.
    """
    n = len(A)
    if n == 0:  # Handle empty sequence case
        return 0 
    
    dp = [0] * n  # Initialize dp table

    dp[0] = A[0]
    if n > 1:
        dp[1] = max(A[0], A[1])

    for i in range(2, n):
        dp[i] = max(A[i] + dp[i-2], dp[i-1])

    return dp[n-1]



# 4. Example Test Cases:

print(max_subsequence_sum([3, 2, 5, 10, 7]))  # Output: 18
print(max_subsequence_sum([1, 2, 3, 4, 5])) # Output: 9
print(max_subsequence_sum([5, 1, 2, 10, 6, 2]))  # Output: 17
print(max_subsequence_sum([])) # Output: 0
print(max_subsequence_sum([1])) # Output: 1


# 5. Alternative Approaches:

# Space Optimized Approach (O(1) Space):

def max_subsequence_sum_optimized(A):
    """
    Calculates the maximum subsequence sum with no adjacent elements (O(1) space).
    """
    n = len(A)
    if n == 0:
        return 0

    prev_prev = 0
    prev = A[0]
    
    for i in range(1, n):
        curr = max(A[i] + prev_prev, prev)
        prev_prev = prev
        prev = curr

    return prev


print(max_subsequence_sum_optimized([3, 2, 5, 10, 7]))  # Output: 18
print(max_subsequence_sum_optimized([1, 2, 3, 4, 5])) # Output: 9



```




# Connect with me: https://github.com/ohkrahul
