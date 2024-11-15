'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-11-14
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-11-14

### 1. Problem understanding and approach

We are given an array of integers and we have to find the longest increasing subsequence. A subsequence is a sequence that can be obtained from the original sequence by deleting some elements while maintaining the relative order of the remaining elements.

We can solve this problem using dynamic programming. We can define a state dp[i] as the length of the longest increasing subsequence ending at index i. Then, we can compute dp[i] as follows:

```
dp[i] = max(dp[j] + 1) for all j < i such that a[j] < a[i]
```

The base case is dp[0] = 1.

Once we have computed dp[i] for all i, the length of the longest increasing subsequence is max(dp[i]) for all i.

### 2. Time and space complexity analysis

The time complexity of this solution is O(n^2), where n is the length of the array. The space complexity is O(n).

### 3. Well-commented implementation

```python
def longest_increasing_subsequence(arr):
  """
  Finds the length of the longest increasing subsequence in an array.

  Parameters:
    arr: The array to search.

  Returns:
    The length of the longest increasing subsequence.
  """

  n = len(arr)

  # Initialize the dynamic programming table.
  dp = [1] * n

  # Compute the length of the longest increasing subsequence ending at each index.
  for i in range(1, n):
    for j in range(i):
      if arr[j] < arr[i]:
        dp[i] = max(dp[i], dp[j] + 1)

  # Return the length of the longest increasing subsequence.
  return max(dp)


# Example test cases.
arr1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(arr1))  # 6

arr2 = [1, 2, 3, 4, 5]
print(longest_increasing_subsequence(arr2))  # 5

arr3 = [5, 4, 3, 2, 1]
print(longest_increasing_subsequence(arr3))  # 1
```

### 4. Example test cases

The following are the example test cases from the problem statement:

| Input | Output |
|---|---|
| 10 22 9 33 21 50 41 60 80 | 6 |
| 1 2 3 4 5 | 5 |
| 5 4 3 2 1 | 1 |

### 5. Alternative approaches

There are several alternative approaches to this problem, including:

* **Binary search:** We can use binary search to find the longest increasing subsequence in O(n log n) time.
* **Segment tree:** We can use a segment tree to compute the length of the longest increasing subsequence ending at each index in O(n log n) time.
* **Greedy algorithm:** We can use a greedy algorithm to find the longest increasing subsequence in O(n) time. However, this algorithm is not guaranteed to find the optimal solution.

# Connect with me: https://github.com/ohkrahul
