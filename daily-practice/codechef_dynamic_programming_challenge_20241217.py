'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-17
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-17

### 1. Problem Understanding and Approach

The problem involves finding the maximum sum of a non-empty subsequence of a given sequence of numbers. The sequence can contain both positive and negative numbers.

The problem can be solved using dynamic programming. We define a state dp[i] as the maximum sum of a non-empty subsequence of the sequence up to index i. We can calculate dp[i] using the following recurrence relation:

```
dp[i] = max(dp[i-1] + a[i], a[i])
```

where a[i] is the i-th element of the sequence.

The base case for the recurrence relation is dp[0] = a[0].

### 2. Time and Space Complexity Analysis

The time complexity of the algorithm is O(n), where n is the length of the sequence. The algorithm takes O(n) time to compute the dp[] array.

The space complexity of the algorithm is O(n). The algorithm uses an array of size n to store the dp[] array.

### 3. Well-commented Implementation

```python
def maximum_subsequence_sum(arr):
    """
    Finds the maximum sum of a non-empty subsequence of a given sequence of numbers.

    Parameters:
        arr (list): The sequence of numbers.

    Returns:
        int: The maximum sum of a non-empty subsequence of the sequence.
    """

    # Initialize the dp array.
    dp = [0] * len(arr)

    # Calculate the dp array.
    for i in range(len(arr)):
        dp[i] = max(dp[i-1] + arr[i], arr[i])

    # Return the maximum value in the dp array.
    return max(dp)


# Example test cases.
arr1 = [1, 2, 3, 4, -10]
print(maximum_subsequence_sum(arr1))  # Output: 10

arr2 = [-1, -2, -3, -4, -10]
print(maximum_subsequence_sum(arr2))  # Output: -1
```

### 4. Example Test Cases

The following are some example test cases for the algorithm:

| Input | Output |
|---|---|
| [1, 2, 3, 4, -10] | 10 |
| [-1, -2, -3, -4, -10] | -1 |
| [1, -2, 3, -4, 5] | 6 |

### 5. Alternative Approaches

There are a few alternative approaches to solving this problem:

* **Greedy algorithm:** The greedy algorithm selects the largest element in the sequence and adds it to the subsequence. This algorithm is not guaranteed to find the optimal solution, but it usually performs well in practice.
* **Divide-and-conquer algorithm:** The divide-and-conquer algorithm divides the sequence into two halves and recursively finds the maximum sum of a non-empty subsequence in each half. The maximum sum of a non-empty subsequence in the original sequence is then the maximum of the maximum sums in the two halves.
* **Linear programming:** The linear programming approach formulates the problem as a linear program and solves it using a linear programming solver. This approach is guaranteed to find the optimal solution, but it is more computationally expensive than the other approaches.

# Connect with me: https://github.com/ohkrahul
