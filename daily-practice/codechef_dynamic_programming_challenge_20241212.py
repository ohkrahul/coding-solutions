'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-12
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-12

## Problem Understanding and Approach

The problem statement provides a sequence of numbers and asks us to find the longest non-decreasing subsequence within that sequence. A non-decreasing subsequence is a subsequence where each element is greater than or equal to the previous element.

To solve this problem, we will use dynamic programming. Dynamic programming is a technique that breaks down a complex problem into smaller subproblems and stores the solutions to those subproblems in a table. This allows us to reuse solutions to subproblems that have already been solved, which can greatly improve the efficiency of the algorithm.

**Algorithm:**

1. Create a table `dp` of size `n x 2`, where `n` is the number of elements in the sequence.
2. Initialize all cells in `dp` to 0.
3. For each element `i` in the sequence:
   - For each element `j` in the sequence such that `j < i`:
      - If `sequence[i] >= sequence[j]`, then `dp[i][1] = max(dp[i][1], dp[j][1] + 1)`
      - If `sequence[i] > sequence[j]`, then `dp[i][0] = max(dp[i][0], dp[j][0] + 1)`
4. The longest non-decreasing subsequence is the maximum value in the `dp` table.

## Time and Space Complexity Analysis

The time complexity of this algorithm is O(n^2), where n is the number of elements in the sequence. This is because the algorithm iterates over each element in the sequence and performs a loop over all previous elements.

The space complexity of this algorithm is O(n), since the algorithm uses a table of size n x 2.

## Well-Commented Implementation

```python
def longest_non_decreasing_subsequence(sequence):
  """
  Finds the longest non-decreasing subsequence in a given sequence of numbers.
  
  Args:
    sequence: A list of numbers.
  
  Returns:
    The length of the longest non-decreasing subsequence.
  """

  # Create a table to store the solutions to the subproblems.
  dp = [[0 for _ in range(2)] for _ in range(len(sequence))]

  # Initialize the table.
  for i in range(len(sequence)):
    dp[i][0] = 1
    dp[i][1] = 1

  # Fill in the table using dynamic programming.
  for i in range(1, len(sequence)):
    for j in range(i):
      if sequence[i] >= sequence[j]:
        dp[i][1] = max(dp[i][1], dp[j][1] + 1)
      if sequence[i] > sequence[j]:
        dp[i][0] = max(dp[i][0], dp[j][0] + 1)

  # Return the longest non-decreasing subsequence.
  return max(max(row) for row in dp)
```

## Example Test Cases

```python
assert longest_non_decreasing_subsequence([1, 2, 3, 4, 5]) == 5
assert longest_non_decreasing_subsequence([1, 3, 2, 4, 5]) == 4
assert longest_non_decreasing_subsequence([5, 4, 3, 2, 1]) == 1
```

## Alternative Approaches

**Greedy Approach:**

The greedy approach to this problem is to start with the first element in the sequence and add each subsequent element to the subsequence if it is greater than or equal to the last element in the subsequence. This approach is not guaranteed to find the longest non-decreasing subsequence, but it can be much faster than the dynamic programming approach, especially for large sequences.

```python
def longest_non_decreasing_subsequence_greedy(sequence):
  """
  Finds a non-decreasing subsequence of a given sequence of numbers using a greedy approach.

  Args:
    sequence: A list of numbers.

  Returns:
    A list of numbers that is a non-decreasing subsequence of the given sequence.
  """

  subsequence = []

  for number in sequence:
    if not subsequence or number >= subsequence[-1]:
      subsequence.append(number)

  return subsequence
```

**Divide-and-Conquer Approach:**

The divide-and-conquer approach to this problem is to divide the sequence into two halves, find the longest non-decreasing subsequence in each half, and then merge the two subsequences into a single non-decreasing subsequence. This approach can be implemented using a recursive function.

```python
def longest_non_decreasing_subsequence_divide_and_conquer(sequence):
  """
  Finds the longest non-decreasing subsequence of a given sequence of numbers using a divide-and-conquer approach.

  Args:
    sequence: A list of numbers.

  Returns:
    A list of numbers that is the longest non-decreasing subsequence of the given sequence.
  """

  if len(sequence) <= 1:
    return sequence

  # Divide the sequence into two halves.
  mid = len(sequence) // 2
  left_half = sequence[:mid]
  right_half = sequence[mid:]

  # Find the longest non-decreasing subsequence in each half.
  left_subsequence = longest_non_decreasing_subsequence(left_half)
  right_subsequence = longest_non_decreasing_subsequence(right_half)

  # Merge the two subsequences into a single non-decreasing subsequence.
  merged_subsequence = merge_subsequences(left_subsequence, right_subsequence)

  return merged_subsequence

def merge_subsequences(left_subsequence, right_subsequence):
  """
  Merges two non-decreasing subsequences into a single non-decreasing subsequence.

  Args:
    left_subsequence: A list of numbers that is a non-decreasing subsequence.
    right_subsequence: A list of numbers that is a non-decreasing subsequence.

  Returns:
    A list of numbers that is the merged non-decreasing subsequence.
  """

  merged_subsequence = []

  i = 0  # Index into left_subsequence
  j = 0  # Index into right_subsequence

  while i < len(left_subsequence) and j < len(right_subsequence):
    if left_subsequence[i] <= right_subsequence[j]:
      merged_subsequence.append(left_subsequence[i])
      i += 1
    else:
      merged_subsequence.append(right_subsequence[j])
      j += 1

  # Append the remaining elements from left_subsequence.
  while i < len(left_subsequence):
    merged_subsequence.append(left_subsequence[i])
    i += 1

  # Append the remaining elements from right_subsequence.
  while j < len(right_subsequence):
    merged_subsequence.append(right_subsequence[j])
    j += 1

  return merged_subsequence
```

# Connect with me: https://github.com/ohkrahul
