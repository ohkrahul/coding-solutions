'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-11-24
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-11-24

**1. Problem Understanding and Approach**

The problem can be understood as follows:

- We are given a sequence of numbers A1, A2, ..., An.
- We want to find the longest increasing subsequence of this sequence.

A longest increasing subsequence is a subsequence of the original sequence such that the elements of the subsequence are in strictly increasing order, and the subsequence is as long as possible.

One way to solve this problem is to use dynamic programming. We can define a table dp such that dp[i] is the length of the longest increasing subsequence of the subarray A1, A2, ..., Ai.

We can then compute the table dp in bottom-up fashion, starting with dp[1] = 1 (since the longest increasing subsequence of a single element is just that element itself). For each subsequent element Ai, we can consider all elements Aj with j < i and check if Ai is greater than Aj. If it is, then we can extend the longest increasing subsequence ending at Aj to include Ai. The length of the longest increasing subsequence ending at Ai is then the maximum of the lengths of the longest increasing subsequences ending at all such Aj, plus 1.

**2. Time and Space Complexity Analysis**

The time complexity of the algorithm is O(n^2), where n is the length of the input sequence. This is because we need to consider all pairs of elements in the sequence to compute the table dp.

The space complexity of the algorithm is O(n), since we need to store the table dp.

**3. Well-commented Implementation**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
  // Read the input sequence
  int n;
  cin >> n;
  vector<int> A(n);
  for (int i = 0; i < n; i++) {
    cin >> A[i];
  }

  // Initialize the table dp
  vector<int> dp(n, 1);

  // Compute the table dp
  for (int i = 1; i < n; i++) {
    for (int j = 0; j < i; j++) {
      if (A[i] > A[j] && dp[i] < dp[j] + 1) {
        dp[i] = dp[j] + 1;
      }
    }
  }

  // Find the length of the longest increasing subsequence
  int max_len = 0;
  for (int i = 0; i < n; i++) {
    max_len = max(max_len, dp[i]);
  }

  // Print the length of the longest increasing subsequence
  cout << max_len << endl;

  return 0;
}
```

**4. Example Test Cases**

- Input:
```
5
1 2 3 4 5
```
Output:
```
5
```

- Input:
```
5
5 4 3 2 1
```
Output:
```
1
```

- Input:
```
10
1 3 2 4 5 3 6 7 8 9
```
Output:
```
6
```

**5. Alternative Approaches**

There are other algorithms for finding the longest increasing subsequence of a sequence. One such algorithm is the binary search algorithm. This algorithm has a time complexity of O(n log n). However, it is not as easy to implement as the dynamic programming algorithm.

# Connect with me: https://github.com/ohkrahul
