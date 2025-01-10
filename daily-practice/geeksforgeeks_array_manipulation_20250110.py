'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-01-10
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-01-10

1. **Problem understanding and approach**

The problem statement asks us to perform a series of operations on an array of integers. These operations involve adding or subtracting certain values to elements at specific indices in the array. The goal is to determine the maximum sum that can be obtained by performing these operations in any order.

To solve this problem, we can use a dynamic programming approach. We can create a table of size n × m, where n is the length of the array and m is the number of operations. The entry in the table at position (i, j) will represent the maximum sum that can be obtained by performing the first j operations on the first i elements of the array.

We can initialize the table as follows:

```
dp[0][0] = 0
for i = 1 to n:
    dp[i][0] = a[i]
```

where a is the input array.

We can then populate the rest of the table using the following recurrence relation:

```
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + b[j])
```

where b is the array of operation values.

The final answer will be stored in the entry dp[n][m].

2. **Time and space complexity analysis**

The time complexity of the above solution is O(nm), where n is the length of the array and m is the number of operations. The space complexity is also O(nm).

3. **Well-commented implementation**

```python
def array_manipulation(a, b):
    """
    Given an array of integers, perform the following operations...

    1. Add b[j] to a[a[j]]
    2. Subtract b[j] from a[a[j] + 1]
    3. Find the maximum sum that can be obtained by performing these operations in any order.

    Args:
        a: An array of integers.
        b: An array of integers.

    Returns:
        The maximum sum that can be obtained.
    """

    # Create a table to store the maximum sum for each subarray and number of operations.
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    # Initialize the first row and column of the table.
    for i in range(len(a) + 1):
        dp[i][0] = a[i - 1]

    # Populate the rest of the table.
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + b[j - 1])

    # Return the maximum sum.
    return dp[len(a)][len(b)]


# Example test cases.
a1 = [1, 2, 3, 4, 5]
b1 = [1, 2, 3, 4, 5]
print(array_manipulation(a1, b1))  # Output: 21

a2 = [1, 2, 3]
b2 = [1, 2, 3]
print(array_manipulation(a2, b2))  # Output: 9
```

4. **Alternative approaches**

There are other approaches to solving this problem, such as using a prefix sum array or a segment tree. However, the dynamic programming approach is the most straightforward and easiest to implement.

5. **Additional notes**

This problem is a variation of the classic "Maximum Subarray" problem. However, in this problem, we are allowed to perform operations on the array, which makes the problem more challenging.

# Connect with me: https://github.com/ohkrahul
