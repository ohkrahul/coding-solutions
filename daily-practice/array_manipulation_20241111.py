'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
Link: https://practice.geeksforgeeks.org/problems/array-manipulation
'''
```python
def arrayManipulation(n, queries):
  """
  Given an array of integers, perform the following operations:
  1. Add a to the value at index x.
  2. Add b to the value at index y.
  3. Print the maximum value in the array.

  Args:
    n: The size of the array.
    queries: A list of queries in the form of tuples (x, y, a, b).

  Returns:
    The maximum value in the array.
  """

  # Create an array of zeros.
  array = [0] * (n + 1)

  # Iterate over the queries and update the array.
  for query in queries:
    x, y, a, b = query
    array[x - 1] += a
    array[y] -= a

  # Calculate the prefix sums.
  prefix_sums = [0] * (n + 1)
  for i in range(n):
    prefix_sums[i + 1] = prefix_sums[i] + array[i]

  # Find the maximum value in the array.
  max_value = max(prefix_sums)

  # Return the maximum value.
  return max_value
```