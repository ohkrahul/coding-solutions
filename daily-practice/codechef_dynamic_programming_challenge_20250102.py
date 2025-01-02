'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-01-02
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-01-02

## Dynamic Programming Challenge
### Problem understanding and approach
We are given an array of n positive integers, and we wish to find the longest increasing subsequence (LIS) in the array. An LIS is a subsequence where each element is greater than the previous one.
We can use dynamic programming to solve this problem. We define a dp array of n elements, where dp[i] stores the length of the LIS ending at index i.
We can compute the dp array as follows:
```
dp[i] = max(dp[j] + 1) for all j < i and a[j] < a[i]
```
This approach has a time complexity of O(n^2).

### Time and space complexity analysis

* **Time complexity:** O(n^2)
* **Space complexity:** O(n)

### Well-commented implementation
```python
def lis(arr):
    """
    Returns the length of the longest increasing subsequence in the given array.

    Args:
        arr: A list of positive integers.

    Returns:
        The length of the longest increasing subsequence in the given array.
    """

    # Create a dp array to store the length of the LIS ending at each index.
    dp = [1] * len(arr)

    # Compute the dp array.
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array.
    return max(dp)
```

## Example test cases
Example 1:
```
Input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: 6
Explanation: The longest increasing subsequence is [10, 22, 33, 50, 60, 80].
```
Example 2:
```
Input: [1, 3, 6, 7, 9, 4, 10, 5, 6, 11, 8]
Output: 5
Explanation: The longest increasing subsequence is [1, 3, 6, 9, 10].
```
Example 3:
```
Input: [7, 7, 7, 7, 7]
Output: 1
Explanation: The longest increasing subsequence is [7].
```

## Alternative approaches
This problem can also be solved using a binary search tree. The idea is to construct a BST where each node stores an element of the array. The LIS ending at each node is then the length of the longest path from that node to a leaf node. This approach has a time complexity of O(n log n) and a space complexity of O(n).

# Connect with me: https://github.com/ohkrahul
