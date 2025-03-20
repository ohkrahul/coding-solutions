'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-03-20
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-03-20

```python
# Problem: Maximum Sum Subsequence with No Adjacent Elements

# Platform: CodeChef (Hypothetical -  Similar problems exist on CodeChef)
# Difficulty: Hard


# 1. Problem Understanding and Approach

"""
Problem Statement: Given a sequence of N non-negative integers, find the maximum sum of a subsequence such that no two adjacent elements in the original sequence are chosen.

Example:
Input: [7, 2, 5, 8, 6]
Output: 18 (7 + 8 + 6 = 18 is one valid subsequence, and 7 + 5 + 6 = 18 is another)

Approach: Dynamic Programming

We can use dynamic programming to solve this problem. We maintain an array `dp` where `dp[i]` represents the maximum sum subsequence ending at index `i` (inclusive).

Recurrence Relation:

dp[i] = max(
    dp[i-1],  // Don't include the current element (inherit the max sum from the previous index)
    dp[i-2] + arr[i] // Include the current element and the max sum from two indices before
    arr[i] if i <=1// Base cases: If the current element is at index 0 or 1
)

"""


# 2. Time and Space Complexity Analysis

# Time Complexity: O(N) - We iterate through the array once.
# Space Complexity: O(N) - We use a DP array of size N. (Can be optimized to O(1))



# 3. Well-commented Implementation

def max_sum_subsequence(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    dp = [0] * n  # Initialize DP array

    dp[0] = arr[0]

    if n > 1:
        dp[1] = max(arr[0], arr[1])


    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i],arr[i])

    return dp[n - 1]


# 4. Example Test Cases

print(max_sum_subsequence([7, 2, 5, 8, 6]))  # Output: 18
print(max_sum_subsequence([1, 2, 3, 1]))  # Output: 4
print(max_sum_subsequence([2, 7, 9, 3, 1]))  # Output: 12
print(max_sum_subsequence([0]))  # Output: 0
print(max_sum_subsequence([])) # Output: 0


# 5. Alternative Approaches (Space Optimization)

def max_sum_subsequence_optimized(arr):
    n = len(arr)
    if n == 0:
        return 0

    prev_prev = 0
    prev = arr[0]  # Initialize previous values

    for i in range(1, n):
        curr = max(prev, prev_prev + arr[i], arr[i]) 
        prev_prev = prev
        prev = curr

    return prev



print("----Optimized Space----")
print(max_sum_subsequence_optimized([7, 2, 5, 8, 6]))  # Output: 18
print(max_sum_subsequence_optimized([1, 2, 3, 1]))  # Output: 4
print(max_sum_subsequence_optimized([2, 7, 9, 3, 1]))  # Output: 12
print(max_sum_subsequence_optimized([0]))  # Output: 0
print(max_sum_subsequence_optimized([])) # Output: 0

#In the optimized approach, we use only constant extra space because we are only keeping track of the previous two dp values, not the whole dp array.


```

# Connect with me: https://github.com/ohkrahul
