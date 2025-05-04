'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-05-04
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-05-04

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
Problem: Longest Increasing Subsequence with a Twist (Hypothetical CodeChef Problem)
Platform: CodeChef
Difficulty: Hard

Description: You are given a sequence of N integers A[1], A[2], ..., A[N]. You need to find the length of the longest increasing subsequence (LIS) with the following twist:
- If two elements in the subsequence have the same parity (both even or both odd), their difference must be at least K.
- If two elements have different parity, there's no restriction on their difference.

1. Problem Understanding and Approach:

This problem is a variation of the standard Longest Increasing Subsequence problem. The added constraint about the difference between elements of the same parity makes it more challenging. We can solve this using dynamic programming.

We'll maintain two DP arrays:
- dp_even[i]: Stores the length of the LIS ending at index i, considering only even numbers that satisfy the constraint.
- dp_odd[i]: Stores the length of the LIS ending at index i, considering only odd numbers that satisfy the constraint.

The overall LIS length will be the maximum of the maximum values in dp_even and dp_odd.

2. Time and Space Complexity Analysis:

- Time Complexity: O(N^2) due to the nested loops for calculating dp_even and dp_odd.
- Space Complexity: O(N) for storing the dp arrays.


3. Implementation:
*/

int solve() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> dp_even(n, 1);
    vector<int> dp_odd(n, 1);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[i] > a[j]) {
                if (a[i] % 2 == 0 && a[j] % 2 == 0) { // Both even
                    if (a[i] - a[j] >= k) {
                        dp_even[i] = max(dp_even[i], dp_even[j] + 1);
                    }
                } else if (a[i] % 2 != 0 && a[j] % 2 != 0) { // Both odd
                    if (a[i] - a[j] >= k) {
                        dp_odd[i] = max(dp_odd[i], dp_odd[j] + 1);
                    }
                } else { // Different parity
                    if (a[i] % 2 == 0) {
                        dp_even[i] = max(dp_even[i], dp_odd[j] + 1);
                    } else {
                        dp_odd[i] = max(dp_odd[i], dp_even[j] + 1);
                    }
                }
            }
        }
    }

    int max_len = 0;
    for (int i = 0; i < n; ++i) {
        max_len = max({max_len, dp_even[i], dp_odd[i]});
    }
    return max_len;
}


int main() {
    int t = 1; // For CodeChef, you might need to read the number of test cases.
    // cin >> t;
    while (t--) {
        cout << solve() << endl;
    }
    return 0;
}


/*
4. Example Test Cases:

Input:
5 3
1 4 7 8 10

Output:
4 (LIS: 1 4 7 10)

Input:
4 2
2 4 6 8

Output:
2 (LIS: 2 6 or 4 8)

5. Alternative Approaches:

-  A segment tree or Fenwick tree could potentially be used to optimize finding the maximum dp value for elements satisfying the K difference constraint, reducing the time complexity to O(N log N). However, implementation can be more complex.

*/

```

# Connect with me: https://github.com/ohkrahul
