'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
Link: https://www.codechef.com/problems/DYNAMO
'''
```python
# Dynamic Programming Challenge

# Problem:
# You are given a sequence of numbers. Determine the length of the longest increasing subsequence.

# Solution:
def longest_increasing_subsequence(sequence):
    # Initialize a table to store the length of the longest increasing subsequence for each element in the sequence.
    dp_table = [1 for _ in range(len(sequence))]

    # Iterate over the sequence.
    for i in range(1, len(sequence)):
        # For each element in the sequence, find the longest increasing subsequence that ends with that element.
        for j in range(i):
            if sequence[i] > sequence[j] and dp_table[i] < dp_table[j] + 1:
                dp_table[i] = dp_table[j] + 1

    # Return the maximum value in the table.
    return max(dp_table)
```