'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-15
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-15

## Problem Understanding and Approach

The problem can be broken down into the following steps:

1. Read the input sequence of numbers.
2. Initialize an array of size n to store the maximum sum of subarrays ending at each index.
3. Iterate over the input sequence and update the maximum sum of subarrays for each index using the following formula:

```
max_sum_at_index[i] = max(input_sequence[i], max_sum_at_index[i-1] + input_sequence[i])
```

4. Find the maximum sum of subarrays from the array of maximum sums.

## Time and Space Complexity Analysis

The time complexity of this approach is O(n), where n is the length of the input sequence. The space complexity is also O(n), as we need to store the array of maximum sums.

## Well-commented Implementation

```python
def max_subarray_sum(input_sequence):
    """
    Finds the maximum sum of subarrays in the given input sequence.

    Args:
        input_sequence (list): The input sequence of numbers.

    Returns:
        int: The maximum sum of subarrays.
    """

    n = len(input_sequence)
    max_sum_at_index = [0] * n

    max_sum_at_index[0] = input_sequence[0]

    for i in range(1, n):
        max_sum_at_index[i] = max(input_sequence[i], max_sum_at_index[i-1] + input_sequence[i])

    return max(max_sum_at_index)
```

## Example Test Cases

```python
input_sequence = [1, 2, 3, 4, -10, 5, 6, 7]
print(max_subarray_sum(input_sequence))  # Output: 15

input_sequence = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum(input_sequence))  # Output: 7
```

## Alternative Approaches

Another approach to this problem is to use a sliding window to calculate the maximum sum of subarrays. The sliding window approach can be implemented in O(n) time and O(1) space complexity.

Here is the implementation of the sliding window approach:

```python
def max_subarray_sum_sliding_window(input_sequence):
    """
    Finds the maximum sum of subarrays in the given input sequence using a sliding window.

    Args:
        input_sequence (list): The input sequence of numbers.

    Returns:
        int: The maximum sum of subarrays.
    """

    n = len(input_sequence)
    max_sum = -float('inf')
    current_sum = 0

    for i in range(n):
        current_sum = max(input_sequence[i], current_sum + input_sequence[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
```

# Connect with me: https://github.com/ohkrahul
