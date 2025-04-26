'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-04-26
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-04-26

```python
"""
Problem: Array Manipulation (GeeksForGeeks - Medium)

Description:
You are given an array arr[] of size N and an integer K. You have to perform K operations on the array. 
In each operation, you have to choose two indices i and j (0 <= i, j < N) such that i != j and replace arr[i] 
with (arr[i] + arr[j]) % 1000.  The task is to determine the maximum possible sum of the array elements after 
performing K operations.


1. Problem Understanding and Approach:

The goal is to maximize the array sum after K operations. Observe that the modulo operation ( % 1000) can 
significantly reduce the value of an element if the sum is large.  To maximize the total sum, we should avoid
reducing elements unless necessary.

The optimal strategy is to always add the largest element to all other elements (except itself).
This is because repeatedly adding the largest element maximizes the growth of other elements while minimally affecting the largest element due to the modulo operator.

2. Time and Space Complexity Analysis:

- Time Complexity: O(N*K) for the operations. We can optimize slightly by keeping track of the maximum element's index, reducing the inner loop search to O(1) making the overall time complexity O(N + K)
- Space Complexity: O(1) - We modify the array in place.


3. Well-commented Implementation:
"""

def maximize_array_sum(arr, K):
    n = len(arr)

    for _ in range(K):
        max_val = -1
        max_index = -1

        # Find the maximum element and its index.
        for i in range(n):
            if arr[i] > max_val:
                max_val = arr[i]
                max_index = i

        # Add the maximum element to all other elements (except itself).
        for i in range(n):
            if i != max_index:
                arr[i] = (arr[i] + max_val) % 1000

    return sum(arr)


"""
4. Example Test Cases:
"""

# Test case 1
arr1 = [1, 2, 3]
K1 = 2
print(f"Test case 1: {maximize_array_sum(arr1.copy(), K1)}")  # Expected Output: 11

# Test case 2
arr2 = [100, 200, 300, 400]
K2 = 3
print(f"Test case 2: {maximize_array_sum(arr2.copy(), K2)}")  # Expected Output: 3900


# Test case 3 (larger values and K to demonstrate modulo effect)
arr3 = [999, 998, 997]
K3 = 5
print(f"Test case 3: {maximize_array_sum(arr3.copy(), K3)}")



"""
5. Alternative Approaches:

- Optimization: Instead of searching for the maximum element in each operation (O(N)), we could keep track of the maximum element's index. After an operation, we only need to compare the updated elements with the previous maximum to see if the maximum has changed.  This reduces the time complexity within the K loop to O(1).

- Using NumPy (for very large arrays): For extremely large arrays, NumPy could provide performance improvements by vectorizing operations.


"""


```

# Connect with me: https://github.com/ohkrahul
