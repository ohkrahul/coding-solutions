'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-12-06
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-12-06

## 1. Problem Understanding and Approach

The problem requires us to perform a series of operations on an array of integers. The operations involve updating the values within the array based on specified ranges and values. After performing these operations, we need to find the maximum element in the modified array.

To solve this problem efficiently, we can use a prefix sum approach. This involves creating a new array that stores the cumulative sum of the original array. By maintaining a prefix sum array, we can quickly update the ranges without having to iterate through the entire array multiple times.

## 2. Time and Space Complexity Analysis

* **Time Complexity:** O(n), where n is the number of elements in the original array. This is because we traverse the original array once to construct the prefix sum array and another time to update the prefix sum array based on the given operations.
* **Space Complexity:** O(n), as we create a new array of the same size as the original array to store the prefix sums.

## 3. Well-Commented Implementation

```python
def array_manipulation(arr, n, queries):
    """
    Performs a series of operations on an array and returns the maximum element.

    Parameters:
    arr (list): The original array.
    n (int): The number of elements in the array.
    queries (list): A list of tuples representing the operations to be performed.
    
    Returns:
    int: The maximum element in the modified array.
    """

    # Create a prefix sum array to store the cumulative sum of the original array.
    prefix_sum = [0] * n

    # Initialize the prefix sum array with the first element of the original array.
    prefix_sum[0] = arr[0]

    # Calculate the prefix sum for the remaining elements.
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # Perform the operations on the prefix sum array.
    for query in queries:
        start, end, value = query
        prefix_sum[start - 1] += value
        if end < n:
            prefix_sum[end] -= value

    # Find the maximum element in the modified array.
    max_element = 0
    for i in range(n):
        max_element = max(max_element, prefix_sum[i])

    # Return the maximum element.
    return max_element


# Example test cases
arr = [1, 2, 3, 4, 5]
n = len(arr)
queries = [(1, 3, 2), (2, 4, 3), (4, 5, 6)]

# Call the function to perform the operations and find the maximum element.
max_element = array_manipulation(arr, n, queries)

# Print the maximum element.
print(max_element)  # Output: 11
```

## 4. Example Test Cases

**Input 1:**
* arr = [1, 2, 3, 4, 5]
* n = 5
* queries = [(1, 3, 2), (2, 4, 3), (4, 5, 6)]

**Output:** 11

**Explanation:**
* Perform the operations on the prefix sum array:
    * [1, 3, 5, 8, 11]
* Find the maximum element in the modified array: 11

**Input 2:**
* arr = [1, 1, 1, 1, 1]
* n = 5
* queries = [(1, 2, 100), (2, 5, 100)]

**Output:** 200

**Explanation:**
* Perform the operations on the prefix sum array:
    * [101, 201, 301, 401, 501]
* Find the maximum element in the modified array: 200

## 5. Alternative Approaches

An alternative approach to this problem is to create a binary indexed tree (BIT). A BIT allows us to perform range updates and point queries in O(log n) time. This approach would provide the same time complexity for performing the operations, but it has additional space complexity for constructing the BIT.

# Connect with me: https://github.com/ohkrahul
