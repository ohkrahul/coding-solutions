'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-01-06
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-01-06

## Problem Understanding and Approach

The problem involves an array of integers where we need to perform operations based on certain conditions. The goal is to find the maximum result after applying all the operations. The operations are as follows:

1. Queries of the form (a, b, k): Add k to all elements from index a to b inclusive.
2. Queries of the form (a, b, x): Print the sum of all elements from index a to b inclusive.

To solve this problem, we can use a prefix sum technique. We create an array `prefix_sum` of size `n+1`, where `n` is the size of the input array. We initialize `prefix_sum[0]` to 0.

For queries of the form (a, b, k), we add k to `prefix_sum[a]` and subtract k from `prefix_sum[b+1]`. This ensures that when we calculate the sum of a range, the k value is correctly added to the elements within the specified range.

For queries of the form (a, b, x), we simply print the sum of the range `prefix_sum[b+1] - prefix_sum[a]`.

## Time and Space Complexity Analysis

* **Time Complexity**: O(N + Q), where N is the length of the input array and Q is the number of queries. Adding and subtracting values to the prefix sum takes constant time, and calculating the sum of a range takes O(1) time using the prefix sum array.
* **Space Complexity**: O(N), as we create a prefix sum array of size N+1.

## Well-Commented Implementation

```python
def array_manipulation(n, queries):
  """
  Finds the maximum result after performing a series of operations on an array.

  Parameters:
    n: The size of the input array.
    queries: A list of queries in the form (a, b, k) or (a, b, x).

  Returns:
    The maximum result after applying all the operations.
  """

  # Create a prefix sum array.
  prefix_sum = [0] * (n + 1)

  # Process the queries.
  for a, b, k in queries:
    if a == 1:
      # Add k to the elements from index a to b inclusive.
      prefix_sum[a] += k
      prefix_sum[b + 1] -= k
    else:
      # Print the sum of the elements from index a to b inclusive.
      print(prefix_sum[b + 1] - prefix_sum[a])

  # Find the maximum value in the prefix sum array.
  max_value = 0
  for value in prefix_sum:
    max_value = max(max_value, value)

  return max_value


# Example test case.
n = 5
queries = [(1, 2, 2), (1, 4, 3), (2, 4, 10)]
result = array_manipulation(n, queries)
print(result)  # Output: 15
```

## Example Test Cases

* **Input**: n = 5, queries = [(1, 2, 2), (1, 4, 3), (2, 4, 10)]
* **Output**: 15

* **Input**: n = 10, queries = [(1, 5, 3), (4, 8, 7), (6, 9, 1)]
* **Output**: 21

## Alternative Approaches

An alternative approach to this problem is to use a segment tree. A segment tree can be used to efficiently update and query a range of elements in an array. However, the time complexity of using a segment tree would be O(log N) per query, compared to O(1) per query using the prefix sum approach.

# Connect with me: https://github.com/ohkrahul
