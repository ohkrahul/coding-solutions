'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
Link: https://practice.geeksforgeeks.org/problems/array-manipulation
'''
```python
from typing import List

def arrayManipulation(n: int, queries: List[List[int]]) -> int:
  """
  Given an array of integers, perform the following operations:

  - For each query, add the value at index b to the value at index a inclusive.
  - Return the maximum value in the array.

  Args:
    n (int): The size of the array.
    queries (List[List[int]]): A list of queries, where each query is a list of three integers [a, b, k].

  Returns:
    int: The maximum value in the array.
  """

  # Create an array of size n filled with zeros.
  arr = [0] * n

  # Iterate over the queries and update the array accordingly.
  for a, b, k in queries:
    arr[a - 1] += k
    if b < n:
      arr[b] -= k

  # Find the maximum value in the array.
  max_value = 0
  for i in range(n):
    arr[i] += arr[i - 1] if i > 0 else 0
    max_value = max(max_value, arr[i])

  return max_value
```