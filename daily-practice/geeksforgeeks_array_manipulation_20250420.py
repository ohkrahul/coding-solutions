'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-04-20
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-04-20

```python
"""
Problem: Array Manipulation (GeeksForGeeks - Medium)

Description: You are given an array arr[] of size N. You need to perform the following operations:

1. Remove all occurrences of the smallest element from the array.
2. Remove all occurrences of the largest element from the array.
3. Repeat steps 1 and 2 until the array becomes empty or only one unique element is left.

Return the final array.


1. Problem Understanding and Approach:

The problem requires us to iteratively remove the smallest and largest elements from the array until a specific condition is met (empty or only one unique element). We can achieve this using a loop and some helper functions.  The key is to efficiently find and remove elements. Using a sorted list can simplify this.

2. Time and Space Complexity Analysis:

- Time Complexity: O(N log N) in the worst case, dominated by sorting the array. Each iteration of removal takes at most O(N) time, and we potentially iterate at most N/2 times.
- Space Complexity: O(N) due to using a sorted list (or other auxiliary data structures in alternative approaches).

3. Well-commented Implementation:
"""


def solve(arr):
    """
    Manipulates the array by removing smallest and largest elements iteratively.

    Args:
        arr: The input array of integers.

    Returns:
        The resulting array after the operations.
    """
    if not arr:  # Handle empty input
        return []

    while True:
        n = len(arr)
        if n <= 1:  # Base case: empty or single unique element
            return arr

        arr.sort()  # Sort the array to easily find min/max

        min_val = arr[0]
        max_val = arr[-1]

        if min_val == max_val:  # Only one unique element left
            return arr


        new_arr = [] # Construct the new array by filtering 
        for x in arr:
            if x != min_val and x != max_val:
                new_arr.append(x)

        arr = new_arr


"""
4. Example Test Cases:
"""
print(solve([2, 4, 1, 3, 5]))  # Output: [3]
print(solve([1, 1, 1, 1]))  # Output: [1, 1, 1, 1]
print(solve([2, 4, 6, 8]))  # Output: []
print(solve([1, 2]))       # Output: []
print(solve([1]))        # Output: [1]
print(solve([]))         # Output: []



"""
5. Alternative Approaches:

- Using a Counter (from collections): This could be slightly more efficient for removing elements.
- Using a Min/Max Heap:  If the input array is very large and we want to avoid the initial sort which takes O(N log N) time. We could use a min-heap and max-heap data structure to quickly get min/max elements which are O(1) and removal which would be O(log n). But constructing the heap would take O(N).  So this approach is beneficial for streaming data where you don't have all the elements at the start.



"""
```

# Connect with me: https://github.com/ohkrahul
