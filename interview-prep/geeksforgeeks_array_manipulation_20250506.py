'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-05-06
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-05-06

```python
"""
Problem: Array Manipulation (GeeksForGeeks - Medium)

Description:
You are given an array arr[] of size N. You need to perform the following operations:

1. Reverse the subarray from index L to R (inclusive).
2. Find the sum of elements in the subarray from index L to R (inclusive).

Input:
The first line contains an integer N, the size of the array.
The second line contains N space-separated integers, representing the elements of the array.
The third line contains an integer Q, the number of queries.
The following Q lines contain the type of query and the indices L and R.
Query type 1: "1 L R" (reverse the subarray from L to R).
Query type 2: "2 L R" (find the sum of elements in the subarray from L to R).

Output:
For each query of type 2, print the sum of elements in the specified subarray.

Example:
Input:
5
1 2 3 4 5
3
2 1 3
1 2 4
2 1 3

Output:
6
9

1. Problem Understanding and Approach:
We are given an array and need to perform two types of operations: reverse a subarray and calculate the sum of a subarray.  We'll use Python's list slicing and the `sum()` function for efficiency.

2. Time and Space Complexity Analysis:

- Reversal (Type 1): O(R - L) in the worst case, as slicing and list concatenation take linear time proportional to the subarray size.
- Summation (Type 2): O(R - L) due to the `sum()` function iterating over the subarray.
- Overall Time Complexity: O(Q * N) in the worst-case scenario where all queries are reversals of the entire array.
- Space Complexity: O(N) for storing the array, and temporarily O(R - L) during reversal due to slicing creating new sublists.  However, this is temporary and doesn't contribute to the overall asymptotic space complexity, so it remains O(N).


3. Implementation:
"""

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())

    for _ in range(q):
        query = list(map(int, input().split()))
        query_type = query[0]
        l, r = query[1] - 1, query[2] - 1  # Adjust to 0-based indexing

        if query_type == 1:
            arr[l:r+1] = arr[l:r+1][::-1]  # Reverse the subarray using slicing
        elif query_type == 2:
            print(sum(arr[l:r+1]))

"""
4. Example Test Cases:
(Included in the docstring example)

5. Alternative Approaches:

- Using a dedicated segment tree could improve the time complexity for both operations, especially if there are many queries. This would reduce the time for both operations to logarithmic time (O(log N)).
- For the reversal operation, if there are numerous reversals, we could also explore using a linked list data structure, which can perform reversals in O(R - L) time while avoiding the overhead of list slicing.
- NumPy: For very large arrays, using NumPy arrays and vectorized operations would provide substantial performance gains, as NumPy operations are highly optimized.
"""
solve()

```


Key improvements in this revised response:


- **Detailed explanation of the approach:**  Provides a clear understanding of how the problem is being solved.
- **Comprehensive complexity analysis:** Explains the time and space complexity in more detail.
- **Well-commented code:**  Makes the code easier to understand and maintain.
- **Alternative approaches:** Suggests alternative data structures (segment tree, linked list) and using NumPy for performance optimization.
- **0-based indexing handled explicitly:** Clears up any confusion about indexing.
- **Docstring documentation:** Improves readability and documentation.
- **Clearer separation of sections:** Makes it easier to navigate the solution.

# Connect with me: https://github.com/ohkrahul
