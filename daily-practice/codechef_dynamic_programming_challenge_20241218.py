'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2024-12-18
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2024-12-18

## Problem Understanding and Approach

The problem statement asks to find the longest contiguous subsequence with a given sum. We can solve this problem using dynamic programming. We will create a 2D table `dp` where `dp[i][j]` represents the length of the longest contiguous subsequence with sum `j` ending at index `i`.

We can initialize the `dp` table as follows:

```cpp
for (int i = 0; i < n; i++) {
  dp[i][0] = 1;
}
```

This is because the empty sequence has a sum of 0, and its length is 1.

Now, for each index `i` and each sum `j`, we can compute `dp[i][j]` as follows:

```cpp
dp[i][j] = 0;
if (arr[i] <= j) {
  dp[i][j] = max(dp[i - 1][j], 1 + dp[i - 1][j - arr[i]]);
} else {
  dp[i][j] = dp[i - 1][j];
}
```

If `arr[i]` is less than or equal to `j`, then we have two options:

1. Include `arr[i]` in the subsequence. In this case, the length of the longest contiguous subsequence with sum `j` ending at index `i` is `1 + dp[i - 1][j - arr[i]]`.
2. Exclude `arr[i]` from the subsequence. In this case, the length of the longest contiguous subsequence with sum `j` ending at index `i` is `dp[i - 1][j]`.

We take the maximum of these two options because we want to find the longest contiguous subsequence.

If `arr[i]` is greater than `j`, then we cannot include `arr[i]` in the subsequence, so we set `dp[i][j]` to `dp[i - 1][j]`.

## Time and Space Complexity Analysis

The time complexity of this solution is `O(n * sum)`, where `n` is the length of the input sequence and `sum` is the maximum possible sum of a subsequence. The space complexity of this solution is `O(n * sum)`.

## Well-commented Implementation

```cpp
#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1000;
const int MAXSUM = 10000;

int main() {
  int n, sum;
  cin >> n >> sum;

  int arr[n];
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  int dp[n][MAXSUM + 1];

  // Initialize the dp table
  for (int i = 0; i < n; i++) {
    dp[i][0] = 1;
  }

  // Compute the dp table
  for (int i = 1; i < n; i++) {
    for (int j = 1; j <= sum; j++) {
      dp[i][j] = 0;
      if (arr[i] <= j) {
        dp[i][j] = max(dp[i - 1][j], 1 + dp[i - 1][j - arr[i]]);
      } else {
        dp[i][j] = dp[i - 1][j];
      }
    }
  }

  // Print the answer
  cout << dp[n - 1][sum] << endl;

  return 0;
}
```

## Example Test Cases

**Input:**

```
5 10
1 2 3 4 5
```

**Output:**

```
2
```

**Input:**

```
6 15
1 2 3 4 5 6
```

**Output:**

```
3
```

**Input:**

```
3 8
1 2 7
```

**Output:**

```
0
```

## Alternative Approaches

There are several alternative approaches to solving this problem.

1. **Greedy approach:** This approach tries to greedily build the longest contiguous subsequence with sum `j` at each index `i`. It starts by including `arr[i]` in the subsequence. If this makes the sum of the subsequence greater than `j`, then the approach removes `arr[i]` from the subsequence and continues to the next element. The time complexity of this approach is `O(n * sum)`.

2. **Recursive approach:** This approach uses recursion to find the longest contiguous subsequence with sum `j` at each index `i`. It has a base case when `i` is equal to `n` and a recursive case when `i` is less than `n`. In the recursive case, it tries two options: including `arr[i]` in the subsequence and excluding `arr[i]` from the subsequence. It then returns the maximum length of the longest contiguous subsequence with sum `j` ending at index `i`. The time complexity of this approach is `O(2^n)`, which is exponential.

3. **Segment tree approach:** This approach uses a segment tree to find the longest contiguous subsequence with sum `j` for a given range of indices. It has a time complexity of `O(n log n + q log n)`, where `q` is the number of queries. This approach is more efficient than the dynamic programming approach when the number of queries is large.

# Connect with me: https://github.com/ohkrahul
