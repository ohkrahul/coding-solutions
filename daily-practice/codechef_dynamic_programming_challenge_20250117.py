'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-01-17
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-01-17

### Problem understanding and approach

The problem statement provides us with a sequence of numbers and asks us to find the maximum sum of a contiguous subarray within that sequence. A contiguous subarray is a sequence of consecutive numbers from the original sequence.

To solve this problem, we can use a dynamic programming approach. We will define a state dp[i] as the maximum sum of a contiguous subarray ending at index i. 

We can then use the following recurrence relation to compute dp[i]:

dp[i] = max(dp[i-1] + a[i], a[i]) 

where a[i] is the ith number in the sequence.

The base case is dp[0] = a[0].

Once we have computed dp[i] for all i, the maximum sum of a contiguous subarray is given by max(dp[0], dp[1], ..., dp[n-1]), where n is the length of the sequence.

### Time and space complexity analysis

The time complexity of this algorithm is O(n), where n is the length of the sequence. The space complexity is O(n), since we need to store the dp array.

### Well-commented implementation

```python
def max_subarray_sum(a):
    """
    Finds the maximum sum of a contiguous subarray in a given sequence of numbers.

    Args:
        a: A list of numbers.

    Returns:
        The maximum sum of a contiguous subarray.
    """

    # Initialize the dp array.
    dp = [0] * len(a)

    # Compute the dp array.
    dp[0] = a[0]
    for i in range(1, len(a)):
        dp[i] = max(dp[i-1] + a[i], a[i])

    # Return the maximum sum of a contiguous subarray.
    return max(dp)
```

### Example test cases

The following are some example test cases:

```python
>>> max_subarray_sum([1, 2, 3, 4, 5])
15

>>> max_subarray_sum([-1, -2, -3, -4, -5])
-1

>>> max_subarray_sum([1, -2, 3, -4, 5])
6
```

### Alternative approaches

There are a number of alternative approaches to solving this problem, including:

* A divide-and-conquer approach.
* A greedy approach.
* A brute-force approach.

The dynamic programming approach is typically the most efficient approach for large sequences.

# Connect with me: https://github.com/ohkrahul
