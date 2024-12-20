'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-20
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-20

## Problem Understanding and Approach

The problem involves finding the longest strictly increasing subsequence in a given sequence of numbers. We define a dynamic programming table `dp` where `dp[i]` represents the length of the longest strictly increasing subsequence ending at index `i`.

We initialize `dp[i] = 1` for all `i`, indicating that the subsequence of length 1 ending at each index is the number itself. For each element, we iterate through all the previous elements and check if the current element forms a strictly increasing subsequence with any of the previous elements. If it does, we update `dp[i]` to be the maximum of its current value and the length of the subsequence ending at the previous element plus 1. This ensures that we find the longest strictly increasing subsequence ending at each index. Once the sequence has been processed, the maximum value in `dp` represents the length of the longest strictly increasing subsequence in the original sequence.

## Time and Space Complexity Analysis

* **Time complexity**: O(N^2), where N is the length of the given sequence. The outer loop iterates through the elements of the sequence, and for each element, the inner loop iterates through all the previous elements.
* **Space complexity**: O(N), as we use an array `dp` to store the length of the longest strictly increasing subsequence ending at each index.

## Well-Commented Implementation in Python

```python
def longest_increasing_subsequence(arr):
    """
    Finds the length of the longest strictly increasing subsequence in a given sequence.

    Args:
    arr (list): The sequence of numbers to process.

    Returns:
    int: The length of the longest strictly increasing subsequence.
    """

    # Initialize the dp table
    dp = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            # Check if the current element forms a strictly increasing subsequence with any previous element
            if arr[i] > arr[j]:
                # Update dp[i] to be the maximum of its current value and the length of the subsequence ending at j plus 1
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in dp
    return max(dp)

# Example test cases
arr1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Length of the longest strictly increasing subsequence in", arr1, ":", longest_increasing_subsequence(arr1))

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Length of the longest strictly increasing subsequence in", arr2, ":", longest_increasing_subsequence(arr2))

arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Length of the longest strictly increasing subsequence in", arr3, ":", longest_increasing_subsequence(arr3))
```

## Example Test Cases

* **Example 1:**
    * Input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
    * Output: 6
* **Example 2:**
    * Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    * Output: 9
* **Example 3:**
    * Input: [9, 8, 7, 6, 5, 4, 3, 2, 1]
    * Output: 1

## Alternative Approaches

Another approach to solve this problem is using a binary search tree. We can create a binary search tree to represent the longest strictly increasing subsequence. We initialize the tree with the first element of the sequence. For each subsequent element, we search for the node in the tree that represents the largest element that is smaller than the current element. If such a node exists, we update its value to the current element and insert the current element as its right child. Otherwise, we insert the current element as the rightmost leaf node. The height of the tree represents the length of the longest strictly increasing subsequence.

# Connect with me: https://github.com/ohkrahul
