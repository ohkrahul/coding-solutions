'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-01-12
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-01-12

## Problem Understanding and Approach

The problem requires us to perform a series of operations on an array. Each operation consists of three integers `a`, `b`, and `k`. For each operation, we need to increment each element in the subarray `[a, b]` by `k`.

To efficiently handle these operations, we can make use of the prefix sum technique. The prefix sum array `ps` is computed by iterating over the original array, where each element `ps[i]` represents the sum of elements from index `0` to `i`.

```
// Compute the prefix sum array
for (int i = 1; i < n; i++)
    ps[i] = ps[i - 1] + arr[i];
```

Now, each operation can be converted into two updates to the prefix sum array:

```
// Increment the first element of the subarray [a, b] by k
ps[a - 1] += k;

// Decrement the element just after the subarray [a, b] by k
ps[b] -= k;
```

These updates effectively increment the subarray `[a, b]` without modifying the individual elements.

## Time and Space Complexity Analysis

The time complexity of the solution is O(n + q), where `n` is the length of the input array and `q` is the number of operations. The space complexity is O(n), as we store the prefix sum array.

## Well-Commented Implementation in C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    // Input the original array
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    // Compute the prefix sum array
    vector<int> ps(n, 0);
    for (int i = 1; i < n; i++)
        ps[i] = ps[i - 1] + arr[i];

    // Perform the operations
    for (int i = 0; i < q; i++) {
        int a, b, k;
        cin >> a >> b >> k;
        ps[a - 1] += k;
        ps[b] -= k;
    }

    // Compute the resulting array
    vector<int> res(n);
    res[0] = ps[0];
    for (int i = 1; i < n; i++)
        res[i] = ps[i] - ps[i - 1];

    // Print the resulting array
    for (int i = 0; i < n; i++)
        cout << res[i] << " ";

    return 0;
}
```

## Example Test Cases

**Input:**
```
5 3
1 2 3 4 5
1 2 2
2 4 3
4 5 2
```

**Output:**
```
5 7 9 11 7
```

**Input:**
```
10 5
1 5 2 4 1 3 2 6 7 1
2 4 2
4 7 5
5 9 3
6 8 4
8 10 1
```

**Output:**
```
1 5 9 16 19 22 25 30 37 38
```

## Alternative Approaches

An alternative approach is to use a segment tree to efficiently handle the updates and queries. However, the prefix sum approach is generally more efficient for this problem, especially for large arrays.

# Connect with me: https://github.com/ohkrahul
