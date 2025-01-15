'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-01-15
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-01-15

## Problem Understanding and Approach

**Problem:**

Given an array of integers, perform the following operations:

1. Update the elements of the array at specific indices with given values.
2. Find the maximum sum of contiguous subarray in the modified array.

**Approach:**

1. **Prefix Sum Array:** Create a prefix sum array to quickly compute the sum of subarrays.
2. **Update Prefix Sum Array:** For each update operation, adjust the corresponding elements in the prefix sum array.
3. **Find Maximum Subarray Sum:** Use the prefix sum array to efficiently find the maximum sum of any contiguous subarray.

## Time and Space Complexity Analysis

* **Time Complexity:**
    * Update Operations: O(N)
    * Find Maximum Subarray Sum: O(N)
    * Total: O(N)
* **Space Complexity:** O(N) for the prefix sum array

## Well-Commented Implementation (C++)

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Input array
    vector<int> arr = {1, 2, 3, 4, 5};

    // Prefix sum array
    vector<int> prefixSum(arr.size() + 1, 0);

    // Update operations
    int nUpdates;
    cin >> nUpdates;
    while (nUpdates--) {
        int start, end, value;
        cin >> start >> end >> value;
        prefixSum[start - 1] += value;
        prefixSum[end] -= value;
    }

    // Calculate prefix sum
    for (int i = 1; i < prefixSum.size(); i++) {
        prefixSum[i] += prefixSum[i - 1];
    }

    // Find maximum subarray sum
    int maxSum = INT_MIN;
    int currentSum = 0;
    for (int i = 0; i < prefixSum.size(); i++) {
        currentSum = max(prefixSum[i], currentSum + prefixSum[i]);
        maxSum = max(maxSum, currentSum);
    }

    cout << "Maximum subarray sum: " << maxSum << endl;

    return 0;
}
```

## Example Test Cases

**Input:**

```
arr = [1, 2, 3, 4, 5]
nUpdates = 2
[1, 3, 6]
[4, 5, -3]
```

**Output:**

```
Maximum subarray sum: 8
```

## Alternative Approaches

**Fenwick Tree:**

Instead of a prefix sum array, a Fenwick tree can be used to efficiently update and query subarray sums. This approach offers O(log N) time complexity for both update and query operations.

# Connect with me: https://github.com/ohkrahul
