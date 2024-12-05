'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2024-12-05
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2024-12-05

## Problem Understanding and Approach

The problem requires us to calculate the maximum element in an array of integers after performing a series of operations. Each operation involves incrementing the elements within a specified range by a given value. To solve this problem, we can use a prefix sum array to keep track of the cumulative changes made to each element.

## Time and Space Complexity Analysis

* **Time Complexity**: O(N + Q), where N is the size of the input array and Q is the number of operations. We traverse the array once to calculate the prefix sum array and perform Q operations.
* **Space Complexity**: O(N), as we create a prefix sum array of size N.

## Well-Commented Implementation in C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    vector<int> arr(n + 1);  // 1-based indexing for prefix sum array
    for (int i = 0; i < q; i++) {
        int a, b, k;
        cin >> a >> b >> k;
        arr[a] += k;  // Increment arr[a] by k
        arr[b + 1] -= k;  // Decrement arr[b + 1] by k
    }

    // Calculate the prefix sum array
    for (int i = 1; i <= n; i++) {
        arr[i] += arr[i - 1];
    }

    // Find the maximum element in the prefix sum array
    int max_element = *max_element(arr.begin(), arr.end());
    cout << max_element << endl;

    return 0;
}
```

## Example Test Cases

**Input 1:**
```
5 3
1 2 100
2 5 100
3 4 100
```
**Output 1:**
```
200
```

**Input 2:**
```
10 4
2 6 8
3 5 7
1 8 3
5 9 1
```
**Output 2:**
```
10
```

## Alternative Approaches

**Naive Approach:**

We can brute-force the solution by simulating each operation and updating the elements in the array. This approach has a time complexity of O(QN), where N is the size of the array and Q is the number of operations.

# Connect with me: https://github.com/ohkrahul
