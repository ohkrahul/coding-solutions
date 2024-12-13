'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-13
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-13

## Problem Understanding and Approach

We are given a sequence of numbers, and we need to find the length of the longest increasing sub-sequence in the sequence. This is a classic dynamic programming problem that can be solved using tabulation.

We will create a table `dp` of size `n`, where `n` is the length of the sequence. For each element in the sequence, we will iterate over the previous elements and check if the current element is greater than any of the previous elements. If it is, then we will update the corresponding value in the `dp` table to the maximum of the current value and the value in the `dp` table for the previous element plus 1.

After iterating over all the elements in the sequence, the maximum value in the `dp` table will be the length of the longest increasing sub-sequence.

## Time and Space Complexity Analysis

The time complexity of the solution is O(n^2), where `n` is the length of the sequence. This is because we iterate over each element in the sequence and compare it to all the previous elements.

The space complexity of the solution is O(n), as we create a table of size `n` to store the longest increasing sub-sequence lengths for each element in the sequence.

## Well-Commented Implementation

```python
def longest_increasing_subsequence(sequence):
    """
    Finds the length of the longest increasing sub-sequence in a given sequence of numbers.

    Parameters:
    sequence: The sequence of numbers to search.

    Returns:
    The length of the longest increasing sub-sequence.
    """

    # Create a table to store the longest increasing sub-sequence lengths for each element in the sequence.
    dp = [1] * len(sequence)

    # Iterate over each element in the sequence.
    for i in range(1, len(sequence)):

        # Iterate over all the previous elements.
        for j in range(i):

            # If the current element is greater than the previous element, then update the corresponding value in the `dp` table to the maximum of the current value and the value in the `dp` table for the previous element plus 1.
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the `dp` table will be the length of the longest increasing sub-sequence.
    return max(dp)


# Example test cases.
sequence1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(sequence1))  # Output: 6

sequence2 = [1, 2, 3, 4, 5]
print(longest_increasing_subsequence(sequence2))  # Output: 5

sequence3 = [5, 4, 3, 2, 1]
print(longest_increasing_subsequence(sequence3))  # Output: 1
```

## Alternative Approaches

There are a few other approaches that can be used to solve this problem. One approach is to use a binary search tree to store the elements in the sequence. This approach has a time complexity of O(n log n), which is better than the O(n^2) time complexity of the tabulation approach. However, the binary search tree approach is more complex to implement and requires more memory.

Another approach is to use a sliding window to find the longest increasing sub-sequence. This approach has a time complexity of O(n), but it is not as easy to implement as the tabulation approach.

# Connect with me: https://github.com/ohkrahul
