'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-11-12
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-11-12

## Problem Understanding and Approach

The problem statement provides a sequence of numbers, and the task is to find the longest non-decreasing subsequence of these numbers. A non-decreasing subsequence is a subsequence where each element is greater than or equal to the previous element.

To solve this problem, we can use dynamic programming. We will create a table `dp` of size `n`, where `n` is the length of the sequence. The `dp[i]` value will store the length of the longest non-decreasing subsequence ending at index `i`.

We can populate the `dp` table using the following recurrence relation:

```
dp[i] = 1 + max(dp[j]) for all j < i such that a[j] <= a[i]
```

In other words, the length of the longest non-decreasing subsequence ending at index `i` is 1 plus the maximum of the lengths of the longest non-decreasing subsequences ending at any index `j` less than `i` such that `a[j]` is less than or equal to `a[i]`.

## Time and Space Complexity Analysis

The time complexity of the solution is O(n^2), where `n` is the length of the sequence. This is because we need to consider all possible pairs of indices in the sequence to compute the `dp` table.

The space complexity of the solution is O(n), as we need to store the `dp` table.

## Well-Commented Implementation

```python
# Function to find the longest non-decreasing subsequence
def longest_non_decreasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] <= arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example test cases
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 2, 1]
arr3 = [5, 4, 3, 2, 1]

print(longest_non_decreasing_subsequence(arr1))  # Output: 5
print(longest_non_decreasing_subsequence(arr2))  # Output: 3
print(longest_non_decreasing_subsequence(arr3))  # Output: 1
```

## Alternative Approaches

There are other approaches to solve this problem, such as:

* **Greedy approach:** This approach involves iterating over the sequence and maintaining a list of the elements in the longest non-decreasing subsequence found so far. When a new element is encountered, it is compared to the last element in the list. If the new element is greater than or equal to the last element, it is added to the list. Otherwise, the list is truncated to the index of the last element that is less than or equal to the new element. The time complexity of this approach is O(n^2), and the space complexity is O(n).
* **Binary search approach:** This approach involves using a binary search to find the longest non-decreasing subsequence. The time complexity of this approach is O(n log n), and the space complexity is O(n).

# Connect with me: https://github.com/ohkrahul
