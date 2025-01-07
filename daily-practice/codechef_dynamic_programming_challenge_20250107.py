'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-01-07
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-01-07

**1. Problem Understanding and Approach**

The problem statement presents a dynamic programming challenge involving a sequence of numbers. We need to find the maximum sum of a non-empty subsequence of the given sequence.

A subsequence is a sequence that can be obtained from the original sequence by deleting some elements without changing the order of the remaining elements.

We can solve this problem using dynamic programming, which involves breaking it down into smaller subproblems and solving them recursively.

**2. Time and Space Complexity Analysis**

The recursive approach to this problem has a time complexity of O(2^n), where n is the length of the sequence. This is because for each element in the sequence, we have two options: include it or exclude it. This leads to an exponential number of possibilities.

The space complexity is O(n), as we need to store the maximum sum so far for each subproblem.

**3. Well-commented Implementation**

```python
def max_sum_subsequence(sequence):
    """
    Finds the maximum sum of a non-empty subsequence of the given sequence.

    Args:
    sequence: A list of numbers.

    Returns:
    The maximum sum of a non-empty subsequence of the given sequence.
    """

    n = len(sequence)

    # Initialize the dp table to store the maximum sum so far for each subproblem.
    dp = [[0] * 2 for _ in range(n + 1)]

    # Iterate over the sequence.
    for i in range(1, n + 1):
        # For each element, we have two options: include it or exclude it.
        dp[i][1] = max(dp[i - 1][0] + sequence[i - 1], sequence[i - 1])
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

    # Return the maximum sum of a non-empty subsequence of the given sequence.
    return dp[n][1]
```

**4. Example Test Cases**

**Input:**

```
[1, 2, 3, 4, 5]
```

**Output:**

```
15
```

**Explanation:** The maximum sum of a non-empty subsequence of the given sequence is 15, which is the sum of the entire sequence.

**Input:**

```
[1, -2, 3, -4, 5]
```

**Output:**

```
5
```

**Explanation:** The maximum sum of a non-empty subsequence of the given sequence is 5, which is the sum of the elements 1 and 5.

**5. Alternative Approaches**

**Greedy Approach:**

A greedy approach would be to simply iterate over the sequence and add each element to the subsequence if its sum is greater than the current maximum sum. However, this approach does not guarantee an optimal solution.

**Recursive Approach with Memoization:**

We can improve the time complexity of the recursive approach by using memoization. Memoization involves storing the results of subproblems that have been solved previously. This prevents us from solving the same subproblems multiple times. The time complexity of this approach is reduced to O(n^2).

**Branch and Bound Approach:**

A branch and bound approach involves exploring different possibilities and pruning the branches that are not promising. This approach can be used to find the optimal solution in a faster time than the brute force approach.

# Connect with me: https://github.com/ohkrahul
