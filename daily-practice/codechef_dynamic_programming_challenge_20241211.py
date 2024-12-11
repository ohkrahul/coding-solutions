'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-11
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-11

## Problem Understanding and Approach

The problem statement requires us to find the length of the longest increasing subsequence in a given sequence of numbers. A subsequence is a sequence that can be obtained by removing elements from the original sequence while preserving the order of the remaining elements.

We can solve this problem using dynamic programming. Let dp[i] denote the length of the longest increasing subsequence ending at index i. We can compute dp[i] using the following recurrence relation:

```
dp[i] = max(dp[j] + 1) for all j < i such that arr[j] < arr[i]
```

## Time and Space Complexity Analysis

The time complexity of the dynamic programming algorithm is O(n²) because we need to consider all possible pairs of indices (i, j) to compute dp[i]. The space complexity is O(n) because we need to store the dp array.

## Well-Commented Implementation

```python
def longest_increasing_subsequence(arr):
    """
    Returns the length of the longest increasing subsequence in the given sequence.

    Args:
        arr: The sequence of numbers.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```

## Example Test Cases

```
>>> longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
6
>>> longest_increasing_subsequence([1, 2, 3, 4, 5])
5
>>> longest_increasing_subsequence([5, 4, 3, 2, 1])
1
```

## Alternative Approaches

There are several alternative approaches to solving this problem:

* **Brute force:** We can try all possible subsequences and find the one with the longest increasing length. This approach has a time complexity of O(2^n) and is not practical for large sequences.
* **Binary search:** We can use binary search to find the longest increasing subsequence in a given sequence. This approach has a time complexity of O(n log n) and is more efficient than the brute force approach.
* **Greedy algorithm:** We can try to greedily add elements to the longest increasing subsequence. This approach has a time complexity of O(n) and is less efficient than the dynamic programming approach.

# Connect with me: https://github.com/ohkrahul
