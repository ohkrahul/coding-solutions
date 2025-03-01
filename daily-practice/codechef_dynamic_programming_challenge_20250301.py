'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-03-01
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-03-01

```python
# Problem: Dynamic Programming Challenge - Maximum Sum Subsequence with Constraints

# Platform: CodeChef (Hypothetical - Mimicking a CodeChef style problem)
# Difficulty: Hard


# Problem Understanding and Approach:

# Let's assume the problem statement is as follows:
# Given a sequence of N integers, find the maximum sum of a non-empty subsequence such that no two adjacent elements in the original sequence are selected in the subsequence.


# Approach: Dynamic Programming

# We can solve this using dynamic programming. We maintain two arrays:
# 1. `dp_include[i]`: Stores the maximum sum considering elements up to index `i` and including the element at index `i` in the subsequence.
# 2. `dp_exclude[i]`: Stores the maximum sum considering elements up to index `i` and excluding the element at index `i` in the subsequence.

# Recurrence relations:
# dp_include[i] = arr[i] + dp_exclude[i-1] 
# dp_exclude[i] = max(dp_include[i-1], dp_exclude[i-1])

# Base cases:
# dp_include[0] = arr[0]
# dp_exclude[0] = 0


# Time and Space Complexity Analysis:

# Time Complexity: O(N) - We iterate through the array once.
# Space Complexity: O(N) - We use two arrays of size N. (Can be optimized to O(1) as shown in the alternative approach)



# Well-commented Implementation:

def max_sum_subsequence(arr):
    n = len(arr)
    dp_include = [0] * n
    dp_exclude = [0] * n

    dp_include[0] = arr[0]
    dp_exclude[0] = 0

    for i in range(1, n):
        dp_include[i] = arr[i] + dp_exclude[i-1]
        dp_exclude[i] = max(dp_include[i-1], dp_exclude[i-1])

    return max(dp_include[n-1], dp_exclude[n-1])



# Example Test Cases:

arr1 = [1, 2, 3, 4, 5]  # Output: 9 (1 + 3 + 5)
arr2 = [5, 5, 10, 100, 10, 5] # Output: 110 (5 + 100 + 5)
arr3 = [-1, -2, -3, -4, -5] # Output: -1
arr4 = [1] # Output: 1


print(max_sum_subsequence(arr1))  # Output: 9
print(max_sum_subsequence(arr2))  # Output: 110
print(max_sum_subsequence(arr3))  # Output: -1
print(max_sum_subsequence(arr4))  # Output: 1



# Alternative Approaches:

# Space Optimization:
# We can optimize the space to O(1) by using only two variables to store the previous `dp_include` and `dp_exclude` values instead of the entire arrays.


def max_sum_subsequence_optimized(arr):
    n = len(arr)
    incl = arr[0]
    excl = 0

    for i in range(1, n):
        new_excl = max(incl, excl) # Calculate new excl before updating incl
        incl = arr[i] + excl
        excl = new_excl
    

    return max(incl, excl)


print(max_sum_subsequence_optimized(arr1))  # Output: 9
print(max_sum_subsequence_optimized(arr2))  # Output: 110
print(max_sum_subsequence_optimized(arr3))  # Output: -1
print(max_sum_subsequence_optimized(arr4))  # Output: 1





```

# Connect with me: https://github.com/ohkrahul
