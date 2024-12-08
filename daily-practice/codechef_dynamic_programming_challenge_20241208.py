'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-08
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-08

## Problem Understanding and Approach

The problem statement describes a dynamic programming problem where we are given a sequence of numbers and we need to find the longest increasing subsequence. A subsequence is a sequence that can be obtained by deleting some elements from the original sequence while maintaining the relative order of the remaining elements. For example, the longest increasing subsequence of the sequence [10, 20, 30, 40, 50] is [10, 20, 30, 40, 50].

The problem can be solved using dynamic programming. We can define a table `dp` such that `dp[i]` stores the length of the longest increasing subsequence of the subarray from index 0 to index `i`. The table can be filled in bottom-up manner starting from index 1. For each index `i`, we iterate over all the elements in the subarray from index 0 to index `i-1` and check if the current element is greater than the previous element. If the current element is greater, then we update `dp[i]` to be the maximum of `dp[i]` and `dp[j] + 1`, where `j` is the index of the previous element.

## Time and Space Complexity Analysis

The time complexity of the solution is O(n^2), where n is the length of the sequence. The outer loop iterates over the elements of the sequence, and the inner loop iterates over the elements in the subarray from index 0 to index `i-1`.

The space complexity of the solution is O(n), as we need to store the table `dp` of size n.

## Well-Commented Implementation

```python
def longest_increasing_subsequence(sequence):
  """Finds the longest increasing subsequence of a sequence.

  Args:
    sequence: The sequence of numbers.

  Returns:
    The length of the longest increasing subsequence.
  """

  # Initialize the table `dp` to store the length of the longest increasing subsequence of the subarray from index 0 to index `i`.
  dp = [1] * len(sequence)

  # Iterate over the elements of the sequence.
  for i in range(1, len(sequence)):
    # Iterate over the elements in the subarray from index 0 to index `i-1`.
    for j in range(i):
      # If the current element is greater than the previous element, then update `dp[i]` to be the maximum of `dp[i]` and `dp[j] + 1`.
      if sequence[i] > sequence[j]:
        dp[i] = max(dp[i], dp[j] + 1)

  # Return the maximum value in the table `dp`.
  return max(dp)
```

## Example Test Cases

```
assert longest_increasing_subsequence([10, 20, 30, 40, 50]) == 5
assert longest_increasing_subsequence([10, 20, 10, 30, 20, 40, 50]) == 4
assert longest_increasing_subsequence([10, 20, 10, 30, 20, 40, 50, 60]) == 6
```

## Alternative Approaches

Another way to solve the problem is to use a greedy algorithm. The greedy algorithm starts with an empty subsequence and iteratively adds the next element in the sequence to the subsequence if it is greater than the last element in the subsequence. The time complexity of the greedy algorithm is O(n), where n is the length of the sequence.

However, the greedy algorithm does not always find the longest increasing subsequence. For example, the greedy algorithm will find the subsequence [10, 20, 30] for the sequence [10, 20, 30, 40, 50], while the longest increasing subsequence is [10, 20, 30, 40, 50].

# Connect with me: https://github.com/ohkrahul
