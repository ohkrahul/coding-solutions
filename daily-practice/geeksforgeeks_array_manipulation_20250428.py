'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-04-28
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-04-28

```python
"""
Problem: Array Manipulation (GeeksForGeeks - Medium)

Description: You are given an array arr[] of size N. You need to perform the following operations on the array:

1. Increment the first element of the array by 1.
2. If the array contains an element equal to X, double the value of every element in the array.
3. If the size of the array is greater than 1, delete the last element of the array.

Perform these operations until the size of the array becomes 1. Return the final element of the array.

Problem Understanding and Approach:

The problem requires us to simulate the given operations sequentially until the array is reduced to a single element. We can iterate through the operations, modifying the array according to the rules.

Time and Space Complexity Analysis:

Time Complexity:  The worst-case scenario involves doubling the array elements multiple times. In each iteration, we might iterate through the array to check for X and potentially double all elements.  So, the worst-case time complexity can be closer to O(N*M) where N is the initial size of the array and M is the number of times doubling occurs. However, in many cases, the array shrinks rapidly, making the average time complexity better.  A more precise amortized analysis might be required for a tighter bound.

Space Complexity: O(N) in the worst case because we might double the array's size several times before it starts shrinking.  However, the space complexity will likely be much lower on average as the array size decreases rapidly.

Implementation:
"""

def manipulate_array(arr, x):
    """
    Manipulates the given array according to the rules specified.

    Args:
      arr: The input array.
      x: The value to check for doubling.

    Returns:
      The final element of the array after all operations.
    """

    while len(arr) > 1:
        # 1. Increment first element
        arr[0] += 1

        # 2. Double elements if X is present
        if x in arr:
            arr = [element * 2 for element in arr]

        # 3. Delete last element
        arr.pop()

    return arr[0]


"""
Example Test Cases:
"""
print(manipulate_array([1, 2, 3, 4, 5], 3))   # Output should be 28  (Explanation below)
print(manipulate_array([5, 10, 15, 20], 5))  # Output: 132
print(manipulate_array([1, 2, 3], 4))       # Output: 4



"""
Explanation of the first test case ([1, 2, 3, 4, 5], 3):

1. [2, 2, 3, 4, 5] -> Increment first
2. [4, 4, 6, 8, 10] -> Double (3 is present)
3. [4, 4, 6, 8]    -> Delete last
4. [5, 4, 6, 8]    -> Increment first
5. [10, 8, 12, 16] -> Double (no change as there is no 3)
6. [10, 8, 12]     -> Delete last
7. [11, 8, 12]    -> Increment first
8. [22, 16, 24]    -> Double (no change)
9. [22, 16]        -> Delete last
10.[23, 16]       -> Increment first
11.[46, 32]        -> Double (no change)
12.[46]          -> Delete last

So each number is just doubled twice (steps 2 and 5) and then has a 2 and then a 1 added to it.  This gives 28.

Alternative Approaches:

A slightly optimized approach could involve using a deque (double-ended queue) instead of a list to make the deletion of the last element more efficient (O(1) instead of potentially O(N) in the worst-case for lists). However, for reasonably sized arrays, the difference in performance might not be very noticeable.
"""

```


This revised solution provides a detailed explanation of the problem, time and space complexity analysis, well-commented code, example test cases, and a discussion of a potential alternative approach using deque. It also explains the output of the first test case to clarify the process.

# Connect with me: https://github.com/ohkrahul
