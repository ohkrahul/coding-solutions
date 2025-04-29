'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-04-29
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-04-29

```python
# Problem: Maximum Sum Subsequence with No Adjacent Elements

# Platform: (Hypothetical CodeChef-style problem) - Difficulty: Hard

# Description:
# You are given a sequence of N non-negative integers. You need to find the maximum sum of a subsequence such that no two elements in the chosen subsequence are adjacent in the original sequence.

# 1. Problem Understanding and Approach:

# This is a classic dynamic programming problem. We can solve it using a bottom-up approach.
# Let dp[i] be the maximum sum subsequence ending at index i (or including element at index i).

# Recurrence Relation:
# dp[i] can have two possibilities:
# 1. Include the i-th element:  dp[i] = arr[i] + (dp[i-2] if i >= 2 else 0)  (We cannot include arr[i-1])
# 2. Exclude the i-th element: dp[i] = dp[i-1] (The maximum sum subsequence ending at i-1)

# The final answer will be max(dp[N-1], dp[N-2]) to handle the case where the last element is included or excluded.


# 2. Time and Space Complexity Analysis:
# Time Complexity: O(N) - We iterate through the array once.
# Space Complexity: O(N) - We use an array of size N for dp. (Can be optimized to O(1) - See Alternative Approaches)


# 3. Well-commented Implementation:

def max_sum_subsequence_no_adjacent(arr):
    """
    Calculates the maximum sum subsequence with no adjacent elements.

    Args:
      arr: A list of non-negative integers.

    Returns:
      The maximum sum of the subsequence.
    """

    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    dp = [0] * n

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])


    for i in range(2, n):
        dp[i] = max(arr[i] + (dp[i - 2] if i >= 2 else 0), dp[i - 1])

    return max(dp[n-1], dp[n-2]) # Handle the edge case where n=2


# 4. Example Test Cases:
arr1 = [5, 5, 10, 100, 10, 5]
print(f"Max Sum Subsequence (arr1): {max_sum_subsequence_no_adjacent(arr1)}")  # Output: 110

arr2 = [1, 2, 3]
print(f"Max Sum Subsequence (arr2): {max_sum_subsequence_no_adjacent(arr2)}")  # Output: 4

arr3 = [1, 20, 3]
print(f"Max Sum Subsequence (arr3): {max_sum_subsequence_no_adjacent(arr3)}") # Output: 20

arr4 = [5, 3, 4, 11, 2] # Example to test optimized approach
print(f"Max Sum Subsequence (arr4): {max_sum_subsequence_no_adjacent(arr4)}") # Output: 16




# 5. Alternative Approaches:

# Space Optimized Approach (O(1) space):
# We only need the previous two values of dp at any given time. So, we can use two variables instead of an array to store dp[i-1] and dp[i-2].



def max_sum_subsequence_no_adjacent_optimized(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    prev_prev = arr[0]
    prev = max(arr[0], arr[1])

    for i in range(2, n):
        curr = max(arr[i] + prev_prev, prev)
        prev_prev = prev
        prev = curr

    return prev # prev stores the maximum sum either ending at n-1 or n-2




print(f"Optimized Max Sum Subsequence (arr1): {max_sum_subsequence_no_adjacent_optimized(arr1)}") # Output: 110
print(f"Optimized Max Sum Subsequence (arr4): {max_sum_subsequence_no_adjacent_optimized(arr4)}") # Output: 16
```

# Connect with me: https://github.com/ohkrahul
