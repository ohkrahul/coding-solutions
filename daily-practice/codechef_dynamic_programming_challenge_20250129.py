'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-01-29
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-01-29

## Problem Understanding and Approach

This problem requires us to find the longest strictly increasing subsequence in a sequence of numbers. We can solve this problem using dynamic programming, where we maintain a table that stores the length of the longest increasing subsequence ending at each index.

The base case for this problem is when the index is 0. In this case, the longest increasing subsequence is just the number itself, so the length is 1.

For the inductive case, when the index is greater than 0, we can consider two possibilities:

1. The current number is not part of the longest increasing subsequence. In this case, the length of the longest increasing subsequence is the same as the length of the longest increasing subsequence ending at the previous index.
2. The current number is part of the longest increasing subsequence. In this case, the length of the longest increasing subsequence is 1 more than the length of the longest increasing subsequence ending at the previous index that is smaller than the current number.

By considering these two possibilities, we can compute the length of the longest increasing subsequence for each index in the sequence. The overall time complexity of this algorithm is O(n^2), where n is the length of the sequence. The space complexity is O(n), as we need to store the length of the longest increasing subsequence for each index.

## Implementation

```python
def longest_increasing_subsequence(sequence):
  """
  Finds the length of the longest strictly increasing subsequence in a sequence of numbers.

  Args:
    sequence: The sequence of numbers.

  Returns:
    The length of the longest strictly increasing subsequence.
  """

  n = len(sequence)
  lis_lengths = [1] * n

  for i in range(1, n):
    for j in range(i):
      if sequence[i] > sequence[j]:
        lis_lengths[i] = max(lis_lengths[i], lis_lengths[j] + 1)

  return max(lis_lengths)
```

## Example Test Cases

```
# Example 1
sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = longest_increasing_subsequence(sequence)
print(result)  # Output: 6

# Example 2
sequence = [1, 2, 3, 4, 5]
result = longest_increasing_subsequence(sequence)
print(result)  # Output: 5

# Example 3
sequence = [5, 4, 3, 2, 1]
result = longest_increasing_subsequence(sequence)
print(result)  # Output: 1
```

## Alternative Approaches

There are several alternative approaches to solving this problem, including:

1. Using a binary search tree to store the longest increasing subsequence. This approach has a time complexity of O(n log n) and a space complexity of O(n).
2. Using a greedy algorithm to construct the longest increasing subsequence. This approach has a time complexity of O(n) and a space complexity of O(n).
3. Using a segment tree to store the longest increasing subsequence. This approach has a time complexity of O(n log n) and a space complexity of O(n log n).

# Connect with me: https://github.com/ohkrahul
