'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
Link: https://www.codechef.com/problems/DYNAMO
'''
```python
def longest_increasing_subsequence(sequence):
    """
    Finds the longest increasing subsequence in a given sequence of numbers.

    Args:
        sequence (list): The sequence of numbers to search.

    Returns:
        list: The longest increasing subsequence.
    """

    # Initialize the length and previous index arrays.
    length = [1] * len(sequence)
    previous = [-1] * len(sequence)

    # Iterate over the sequence.
    for i in range(1, len(sequence)):
        # Find the longest increasing subsequence ending at the current index.
        for j in range(i):
            if sequence[i] > sequence[j] and length[i] < length[j] + 1:
                length[i] = length[j] + 1
                previous[i] = j

    # Reconstruct the longest increasing subsequence.
    subsequence = []
    index = length.index(max(length))
    while index != -1:
        subsequence.append(sequence[index])
        index = previous[index]

    # Return the longest increasing subsequence.
    return subsequence[::-1]
```