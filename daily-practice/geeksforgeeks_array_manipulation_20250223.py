'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-23
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-23

## Problem Understanding and Approach

The problem boils down to finding the maximum element in the modified array where we can apply any operation on any index any number of times. The operation is to add the value at that index to the previous element.

To understand the problem better, let's consider an example:

```
Input: arr[] = {2, 1, 5, 1, 3, 2}
Output: 11
```

The modified array will look like:
```
arr[] = {2, 3, 8, 9, 12, 14}
```

The maximum element in the modified array is 14, which is at index 5.

To solve this problem, we can use a greedy approach. We can start from the first element and keep adding the element at the current index to the element at the previous index until we reach the end of the array. We can store the maximum value encountered in a variable and return it as the result.

## Time and Space Complexity Analysis

- **Time Complexity**: O(N), where N is the size of the input array. We iterate over the array once.
- **Space Complexity**: O(1), as we don't use any additional data structures.

## Implementation

```python
def array_manipulation(arr):
    """
    Finds the maximum element in the modified array
    where we can apply any operation on any index any number of times.
    The operation is to add the value at that index to the previous element.

    Parameters:
    arr: The input array

    Returns:
    The maximum element in the modified array
    """

    # Initialize the maximum element to the first element of the array
    max_element = arr[0]

    # Iterate over the array
    for i in range(1, len(arr)):

        # Add the element at the current index to the element at the previous index
        arr[i] += arr[i - 1]

        # Update the maximum element if the current element is greater
        max_element = max(max_element, arr[i])

    # Return the maximum element
    return max_element


## Example Test Cases

```python
# Test Case 1
arr = [2, 1, 5, 1, 3, 2]
max_element = array_manipulation(arr)
print(max_element)  # Output: 14

# Test Case 2
arr = [1, 2, 3, 4, 5]
max_element = array_manipulation(arr)
print(max_element)  # Output: 15

# Test Case 3
arr = [1, 1, 1, 1, 1]
max_element = array_manipulation(arr)
print(max_element)  # Output: 5
```

## Alternative Approaches

Another approach to solving this problem is to use a prefix sum array. We can create a prefix sum array by adding all the elements of the array from left to right. Then, we can find the maximum element in the prefix sum array in O(N) time.

However, the greedy approach is generally more efficient than the prefix sum approach, as it doesn't require creating an additional array.

# Connect with me: https://github.com/ohkrahul
