'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-02-01
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-02-01

## Problem Understanding and Approach

The problem statement is a classic example of a dynamic programming problem. The key idea behind dynamic programming is to break down a complex problem into smaller subproblems and store the solutions to these subproblems in a table. This way, when you need to solve a larger subproblem, you can simply look up the solution in the table instead of recomputing it from scratch.

In this problem, we are given a sequence of numbers and we need to find the longest increasing subsequence (LIS) in this sequence. A LIS is a subsequence of the original sequence in which the elements are in strictly increasing order.

We can solve this problem using dynamic programming by defining a table `dp` where `dp[i]` stores the length of the LIS ending at index `i` in the original sequence. We can initialize the table to 1 for all indices, since the LIS ending at any index is at least of length 1 (the element itself).

We then iterate over the sequence and, for each element, we consider all previous elements. If the current element is greater than the previous element, then we can extend the LIS ending at the previous element by 1. We update the table `dp` accordingly.

Finally, the LIS in the original sequence is the longest LIS ending at any index in the sequence, which can be found by taking the maximum value in the table `dp`.

## Time and Space Complexity Analysis

The time complexity of the above algorithm is O(n<sup>2</sup>), where n is the length of the sequence. This is because we iterate over the sequence twice, once to initialize the table `dp` and once to update it. The space complexity is O(n), since we use a table of size n to store the LIS lengths.

## Well-Commented Implementation

```python
def longest_increasing_subsequence(sequence):
    """
    Finds the longest increasing subsequence in a given sequence.

    Args:
        sequence: The sequence to search.

    Returns:
        The length of the longest increasing subsequence.
    """

    # Initialize the table to 1 for all indices.
    dp = [1] * len(sequence)

    # Iterate over the sequence and update the table.
    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Find the maximum value in the table.
    return max(dp)
```

## Example Test Cases

```python
assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
assert longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 8
```

## Alternative Approaches

There are other approaches to solving this problem, such as using a binary search tree or a segment tree. However, the dynamic programming approach presented here is the simplest and most efficient for this problem.

# Connect with me: https://github.com/ohkrahul
