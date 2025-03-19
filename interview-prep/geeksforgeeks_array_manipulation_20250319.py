'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-03-19
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-03-19

```python
"""
Problem: Array Manipulation (GeeksForGeeks - Medium)

Description:
You are given an array arr[] of size N. You need to perform the following operations:

1. Swap the first and last elements of the array.
2. Replace the second element with the sum of the first and last elements.
3. Replace the third element with the product of the first and last elements.

Return the modified array.

Problem Understanding and Approach:

The problem is straightforward. We need to perform three specific operations on the given array. We can directly manipulate the array using its indices to achieve the desired modifications.

Time and Space Complexity Analysis:

Time Complexity: O(1) - We are performing constant time operations regardless of the input array size.
Space Complexity: O(1) -  We are modifying the array in-place, using constant extra space.


"""


def array_manipulation(arr):
    """
    Modifies the array according to the specified operations.

    Args:
        arr: The input array of integers.

    Returns:
        The modified array.
        Returns None if the array has fewer than 3 elements.

    """
    n = len(arr)

    if n < 3:
        return None  # or raise an exception, depending on desired behavior

    # Operation 1: Swap first and last elements
    arr[0], arr[-1] = arr[-1], arr[0]

    # Operation 2: Replace the second element with the sum of the first and last
    arr[1] = arr[0] + arr[-1]

    # Operation 3: Replace the third element with the product of the first and last
    arr[2] = arr[0] * arr[-1]

    return arr




# Example Test Cases
test_case_1 = [1, 2, 3, 4, 5]
result_1 = array_manipulation(test_case_1)
print(f"Test Case 1: Input = {test_case_1}, Output = {result_1}")  # Output: [5, 6, 5, 4, 1]

test_case_2 = [10, 20, 30]
result_2 = array_manipulation(test_case_2)
print(f"Test Case 2: Input = {test_case_2}, Output = {result_2}")  # Output: [30, 40, 300]


test_case_3 = [1] # Test with less than 3 elements
result_3 = array_manipulation(test_case_3)
print(f"Test Case 3: Input = {test_case_3}, Output = {result_3}") # Output: None



# Alternative Approaches (Not Applicable):

# For this specific problem, the direct manipulation approach is the most efficient and simplest.  
# There are no significantly different alternative approaches that would offer any advantages.


```


Explanation of improvements:

1. **Clearer Problem Description:** Added a more explicit description of the problem, including the exact operations to be performed.
2. **Docstrings:**  Added comprehensive docstrings to the `array_manipulation` function, explaining its purpose, arguments, return value, and any special cases (like what to do if the array has fewer than 3 elements).
3. **Error Handling:** Included a check for the array size being less than 3 and returning `None` in that case (you could also raise an exception if that's preferred in your context).
4. **Comprehensive Test Cases:**  Added more test cases, including an edge case with an array smaller than 3 elements.  The test cases now also clearly print both the input and the expected output.
5. **Detailed Comments:** Improved the comments in the code to explain the purpose of each section and operation more clearly.
6. **Alternative Approaches Section:** Added a section discussing alternative approaches (or the lack thereof in this case).  This shows a more complete thought process.
7. **f-strings:**  Used f-strings for clearer and more concise output in the test cases.


This improved solution is more readable, better documented, and handles edge cases. It also clearly explains the approach, time and space complexity, and potential alternative solutions (if applicable).  It looks more professional and is closer to what you'd see in a real development environment.

# Connect with me: https://github.com/ohkrahul
