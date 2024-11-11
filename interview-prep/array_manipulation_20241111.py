'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
Link: https://practice.geeksforgeeks.org/problems/array-manipulation
'''
```python
def arrayManipulation(n: int, queries: list[list]) -> int:
    """
    Given an array of integers, perform the following operations:

    For each (a, b, k) tuple in queries, add the value k to all elements from index a to b (both inclusive).

    Return the maximum value in the array after performing all operations.

    Args:
        n (int): Length of the array
        queries (list[list]): List of tuples (a, b, k)

    Returns:
        int: Maximum value in the array after performing all operations
    """

    # Create a frequency array
    freq = [0] * (n + 2)

    # Iterate over the queries
    for a, b, k in queries:
        freq[a] += k
        freq[b + 1] -= k

    # Calculate the prefix sum of the frequency array
    prefix = [0] * (n + 2)
    for i in range(1, n + 2):
        prefix[i] = prefix[i - 1] + freq[i]

    # Iterate over the prefix sum array and find the maximum value
    max_value = 0
    for i in range(1, n + 2):
        max_value = max(max_value, prefix[i])

    # Return the maximum value
    return max_value
```