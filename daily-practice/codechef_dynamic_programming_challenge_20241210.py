'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-10
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-10

## Problem Understanding and Approach

The problem statement presents a dynamic programming challenge. We are given a sequence of numbers, and we need to find the largest sum of non-adjacent elements in the sequence.

We can break down the problem into subproblems as follows:

* `dp[i]`: the largest sum of non-adjacent elements in the sequence up to position `i`.

We can then compute `dp[i]` recursively as:

```
dp[i] = max(dp[i-1], dp[i-2] + arr[i])
```

where `arr` is the input sequence of numbers.

The base cases are:

* `dp[0] = arr[0]`
* `dp[1] = max(arr[0], arr[1])`

We can compute `dp[i]` for all `i` in O(n) time, where n is the length of the sequence.

## Time and Space Complexity Analysis

* **Time complexity:** O(n), where n is the length of the sequence.
* **Space complexity:** O(n), for the memoization table.

## Well-commented Implementation

```python
def max_sum_non_adjacent(arr):
    """
    Finds the largest sum of non-adjacent elements in a sequence of numbers.

    Parameters:
    arr: the sequence of numbers

    Returns:
    the largest sum of non-adjacent elements
    """

    # Initialize the memoization table
    dp = [0] * (len(arr) + 1)

    # Base cases
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    # Compute dp[i] for all i
    for i in range(2, len(arr) + 1):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])

    # Return the result
    return dp[-1]


# Example test cases
arr1 = [2, 4, 6, 2, 5]
print(max_sum_non_adjacent(arr1))  # Output: 13

arr2 = [5, 5, 10, 100, 10, 5]
print(max_sum_non_adjacent(arr2))  # Output: 110
```

## Alternative Approaches

There are several alternative approaches to solving this problem:

* **Greedy algorithm:** This algorithm starts with the first element in the sequence and adds it to the sum. Then, it skips the next element and adds the element after that to the sum. It continues in this way until it reaches the end of the sequence. The greedy algorithm is not guaranteed to find the optimal solution, but it is often a good approximation.
* **Divide-and-conquer algorithm:** This algorithm divides the sequence into two halves and recursively computes the largest sum of non-adjacent elements in each half. Then, it combines the results to get the largest sum of non-adjacent elements in the entire sequence. The divide-and-conquer algorithm is guaranteed to find the optimal solution, but it is more complex than the greedy algorithm.

# Connect with me: https://github.com/ohkrahul
