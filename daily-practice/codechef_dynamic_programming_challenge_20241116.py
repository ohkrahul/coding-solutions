'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-11-16
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-11-16

### Problem understanding

The problem statement presents us with a sequence of `N` integers. For each pair of indices `(i, j)` such that `1 <= i <= j <= N`, we have to find the minimum value in the subarray from `i` to `j`. The output should be a list of `N` integers, where the `j`th integer in the output is the minimum value in the subarray from `1` to `j`.

### Approach

We can use dynamic programming to solve this problem. Let `dp[i][j]` be the minimum value in the subarray from `i` to `j`. We can compute `dp[i][j]` in O(1) time using the following recurrence relation:

```
dp[i][j] = min(dp[i][j-1], a[j])
```

where `a` is the given sequence of integers.

### Time and space complexity analysis

The time complexity of the algorithm is O(N^2) and the space complexity is O(N^2).

### Implementation

Here is a Python implementation of the above algorithm:

```python
def min_in_subarrays(a):
    n = len(a)
    dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n):
        dp[i][i] = a[i]

    for i in range(n-1,-1,-1):
        for j in range(i+1,n+1):
            dp[i][j] = min(dp[i][j-1], a[j])

    return [dp[i][n] for i in range(1,n+1)]

a = [1, 3, 2, 5, 4]
print(min_in_subarrays(a))
```

### Example test cases

**Input:**
```
5
1 3 2 5 4
```

**Output:**
```
1 1 2 2 4
```

**Input:**
```
6
7 2 6 4 3 1
```

**Output:**
```
7 2 2 4 3 1
```

### Alternative approaches

There are other approaches to solving this problem, such as using a segment tree or a binary indexed tree. However, the dynamic programming approach is relatively simple to implement and has a time complexity of O(N^2), which is optimal for this problem.

# Connect with me: https://github.com/ohkrahul
