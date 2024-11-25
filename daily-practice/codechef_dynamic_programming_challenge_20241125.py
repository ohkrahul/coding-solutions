'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-11-25
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-11-25

## 1. Problem Understanding and Approach

The problem statement describes a scenario where you are given a sequence of numbers, and you need to find the length of the longest non-decreasing subsequence in that sequence. A non-decreasing subsequence is a subsequence in which each element is greater than or equal to the previous one.

To solve this problem using dynamic programming, we can use the following steps:

1. Initialize a dp array of size n (where n is the length of the sequence), where dp[i] represents the length of the longest non-decreasing subsequence ending at index i.
2. For each element in the sequence:
    - Iterate through all previous elements (j < i)
    - If the current element is greater than or equal to the element at index j, then dp[i] = max(dp[i], dp[j] + 1)
3. The final answer is the maximum value in the dp array.

## 2. Time and Space Complexity Analysis

The time complexity of this approach is O(n^2), where n is the length of the sequence. The outer loop iterates through all n elements, and the inner loop iterates through all previous n elements.

The space complexity is O(n), as we are using an array of size n to store the dynamic programming solution.

## 3. Well-Commented Implementation

```python
def longest_non_decreasing_subsequence(sequence):
    """
    Finds the length of the longest non-decreasing subsequence in a given sequence.

    Args:
        sequence (list): A list of integers representing the sequence.

    Returns:
        int: The length of the longest non-decreasing subsequence.
    """

    n = len(sequence)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[i] >= sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```

## 4. Example Test Cases

**Input:** [1, 2, 3, 4, 5]
**Output:** 5

**Input:** [5, 4, 3, 2, 1]
**Output:** 1

**Input:** [1, 3, 2, 4, 5]
**Output:** 4

## 5. Alternative Approaches

An alternative approach to solving this problem is to use a greedy algorithm. The greedy algorithm iterates through the sequence and maintains a candidate subsequence. At each element, it checks if the current element is greater than or equal to the last element in the candidate subsequence. If it is, then the current element is added to the candidate subsequence. Otherwise, the candidate subsequence is not modified. The final candidate subsequence is the longest non-decreasing subsequence in the sequence.

The time complexity of the greedy algorithm is O(n), and the space complexity is O(n), where n is the length of the sequence.

# Connect with me: https://github.com/ohkrahul
