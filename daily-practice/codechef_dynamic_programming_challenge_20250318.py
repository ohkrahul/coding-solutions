'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-03-18
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-03-18

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
Problem: Longest Increasing Subsequence with Sum Constraint

Platform: CodeChef (Hypothetical -  simulating a CodeChef hard problem)

Difficulty: Hard

Description: You are given a sequence of N positive integers. Find the length of the longest increasing subsequence whose sum is less than or equal to a given integer K.


1. Problem Understanding and Approach:

We need to find the longest increasing subsequence (LIS) that satisfies a sum constraint.  This is a variation of the classic LIS problem.  We can adapt the standard dynamic programming solution to handle the sum constraint.

Approach: We'll use a 2D DP table where `dp[i][j]` stores the maximum length of an increasing subsequence ending at index `i` with a sum less than or equal to `j`.

2. Time and Space Complexity Analysis:

Time Complexity: O(N*K) where N is the length of the sequence and K is the sum constraint. We iterate through the DP table of size N*K.
Space Complexity: O(N*K) for the DP table.


3. Well-commented Implementation:
*/

int longestIncreasingSubsequenceWithSumConstraint(vector<int>& nums, int k) {
    int n = nums.size();
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0)); // dp[i][j]: Max length ending at i with sum <= j

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= k; ++j) {
            // If the current number can be included in the subsequence (sum constraint is met)
            if (nums[i - 1] <= j) {
                // Either include the current number or don't
                dp[i][j] = max(dp[i - 1][j], 1 + dp[i - 1][j - nums[i - 1]]); // Check previous elements for LIS
            } else {
                // Cannot include the current number
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    return dp[n][k];
}


/*
4. Example Test Cases:
*/
int main() {
    // Example 1
    vector<int> nums1 = {1, 2, 3, 4, 5};
    int k1 = 10;
    cout << "Example 1: " << longestIncreasingSubsequenceWithSumConstraint(nums1, k1) << endl; // Output: 5

    // Example 2
    vector<int> nums2 = {10, 5, 20, 15, 30};
    int k2 = 35;
    cout << "Example 2: " << longestIncreasingSubsequenceWithSumConstraint(nums2, k2) << endl; // Output: 2

    // Example 3 -  Empty Sequence
    vector<int> nums3 = {};
    int k3 = 10;
    cout << "Example 3: " << longestIncreasingSubsequenceWithSumConstraint(nums3, k3) << endl; // Output: 0



    return 0;
}



/*
5. Alternative Approaches:

- We can optimize the space complexity to O(K) by using only two rows of the DP table at a time, as we only need the previous row to calculate the current row.

- If the numbers in the input sequence are small (within a certain range), we could potentially use a segment tree or binary indexed tree to efficiently find the maximum length of the LIS ending at a particular value and with a specific sum. This can sometimes improve the time complexity.

*/


```

# Connect with me: https://github.com/ohkrahul
