'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-05-05
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-05-05

```python
# Problem: Array Manipulation (GeeksForGeeks - Medium)

# 1. Problem Understanding and Approach

# Problem Description:
# You are given an array 'arr' of size 'n' and an integer 'k'. 
# You need to perform the following operation 'k' times:
#   - Find the maximum element in the array.
#   - Add the maximum element to all the elements of the array.

# Approach:
#  - Naive Approach: In each iteration, find the maximum element and update all elements. This would have a time complexity of O(n*k).
#  - Optimized Approach: Observe that after each operation, the relative difference between elements remains the same. 
#    Therefore, we only need to find the maximum element ONCE and then calculate the final array elements based on that initial maximum and 'k'.

# 2. Time and Space Complexity Analysis

# Time Complexity:
#   - Optimized Approach: O(n) - We iterate through the array once to find the initial maximum and once to calculate the final elements.
#   - Naive Approach: O(n*k)

# Space Complexity: 
#   - Both approaches: O(1) (In-place modification or returning a new array of the same size doesn't significantly increase space with respect to input size 'n')



# 3. Well-commented Implementation (Optimized)

def array_manipulation(arr, n, k):
    """
    Performs k operations on the array as described above.

    Args:
        arr: The input array of integers.
        n: The size of the array.
        k: The number of operations to perform.

    Returns:
        A list representing the final state of the array.
    """

    if n == 0:  # Handle empty array edge case
        return []
    
    maximum = arr[0]
    for i in range(1, n):
        maximum = max(maximum, arr[i]) # Find the initial maximum element

    result = []
    for x in arr:
        result.append(x + maximum * k)  # Calculate the final value for each element

    return result


# 4. Example Test Cases

arr1 = [1, 2, 3]
n1 = 3
k1 = 2
print(f"Test Case 1: Input: {arr1}, k={k1}, Output: {array_manipulation(arr1, n1, k1)}") # Expected: [7, 8, 9]


arr2 = [5, 5, 5]
n2 = 3
k2 = 1
print(f"Test Case 2: Input: {arr2}, k={k2}, Output: {array_manipulation(arr2, n2, k2)}") # Expected: [10, 10, 10]

arr3 = []
n3 = 0
k3 = 5
print(f"Test Case 3 (Empty array): Input: {arr3}, k={k3}, Output: {array_manipulation(arr3, n3, k3)}") # Expected: []



# 5. Alternative Approaches (Naive - For Comparison)


def array_manipulation_naive(arr, n, k):  # Less efficient approach
    """
    Naive approach for array manipulation (for comparison).
    """

    for _ in range(k):
        maximum = -float('inf')
        for x in arr:
            maximum = max(maximum, x)

        for i in range(n):
            arr[i] += maximum

    return arr




```

# Connect with me: https://github.com/ohkrahul
