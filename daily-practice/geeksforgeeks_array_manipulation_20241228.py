'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-12-28
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-12-28

## **1. Problem Understanding and Approach**

The problem statement requires us to perform operations on an array of integers. The operations are as follows:

- Each operation is represented by a triplet [a, b, d].
- For each triplet, add value `d` to all elements of the array at indices from `a` to `b` (inclusive).

Our approach to solving this problem is to use a prefix sum array. The prefix sum array is an array that stores the cumulative sum of the elements in the original array.

To perform the operations on the prefix sum array, we can apply the following steps for each operation:

- Increment the value at index `a` by `d`.
- Decrement the value at index `b + 1` by `d`.

This will effectively add `d` to all elements from index `a` to index `b` in the original array.

## **2. Time and Space Complexity Analysis**

- **Time Complexity:** O(N + Q), where N is the length of the input array and Q is the number of operations.
- **Space Complexity:** O(N), as we need to store the prefix sum array.

## **3. Well-Commented Implementation**

```python
def array_manipulation(n, queries):
    """
    Performs operations on an array and returns the maximum element in the modified array.

    Args:
        n (int): The size of the input array.
        queries (list): A list of triplets representing the operations.

    Returns:
        int: The maximum element in the modified array.
    """

    # Create a prefix sum array
    prefix_sum = [0] * (n + 1)

    # Apply the operations on the prefix sum array
    for a, b, d in queries:
        prefix_sum[a - 1] += d
        prefix_sum[b] -= d

    # Calculate the modified array by applying the prefix sum
    modified_array = [0] * n
    modified_array[0] = prefix_sum[0]
    for i in range(1, n):
        modified_array[i] = modified_array[i - 1] + prefix_sum[i]

    # Find the maximum element in the modified array
    max_element = max(modified_array)

    return max_element
```

## **4. Example Test Cases**

**Input:**
```
n = 5
queries = [[1, 2, 10], [2, 4, 5], [3, 5, 20]]
```

**Output:**
```
35
```

**Explanation:**
- The first operation adds 10 to elements at indices 1 and 2.
- The second operation adds 5 to elements at indices 2, 3, and 4.
- The third operation adds 20 to elements at indices 3, 4, and 5.

The modified array is [10, 15, 35, 30, 20]. The maximum element in the modified array is 35.

## **5. Alternative Approaches**

**1. Brute Force Approach:**

This approach would involve applying the operations directly to the input array and then finding the maximum element. The time complexity of this approach would be O(N * Q), where N is the length of the input array and Q is the number of operations. This approach is more inefficient than the prefix sum approach.

**2. Segment Tree Approach:**

A segment tree could also be used to solve this problem. The time complexity of this approach would be O(log N + Q), where N is the length of the input array and Q is the number of operations. However, the implementation of a segment tree is more complex than the prefix sum approach.

# Connect with me: https://github.com/ohkrahul
