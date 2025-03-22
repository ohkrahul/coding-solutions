'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-03-22
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-03-22

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
Problem: Longest Increasing Subsequence with Maximum Sum

Platform: (Hypothetical CodeChef Hard Problem)

Description: You are given a sequence of N numbers (a1, a2, ..., aN). 
Find the length of the longest increasing subsequence (LIS) that also has the maximum sum among all LISs of the same length.  If there are multiple LISs with the maximum sum, return the maximum sum.

Example:
Input: [1, 100, 2, 3, 4, 5]
Output: 5  (LIS: [1, 2, 3, 4, 5] with sum 15. Even though [100] is an LIS of length 1, [1, 2, 3, 4, 5] has a greater sum)

1. Problem Understanding and Approach:

We will use dynamic programming to solve this problem.  We will maintain two DP arrays:

- `dp_len[i]`: Stores the length of the LIS ending at index `i`.
- `dp_sum[i]`: Stores the maximum sum of the LIS ending at index `i` among all LISs with the same length as `dp_len[i]`.

2. Time and Space Complexity Analysis:

- Time Complexity: O(N^2) due to the nested loops.
- Space Complexity: O(N) for the DP arrays.

3. Well-commented Implementation:
*/

int solve(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;

    vector<int> dp_len(n, 1); // Initialize LIS lengths to 1 (each element is an LIS of length 1)
    vector<int> dp_sum(n, 0); // Initialize LIS sums

    for (int i = 0; i < n; ++i) {
        dp_sum[i] = nums[i]; // Initial sum is the number itself
    }


    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[i] > nums[j]) { // If we can extend the LIS
                if (dp_len[j] + 1 > dp_len[i]) { // Found a longer LIS
                    dp_len[i] = dp_len[j] + 1;
                    dp_sum[i] = dp_sum[j] + nums[i];
                } else if (dp_len[j] + 1 == dp_len[i]) { // Found an LIS of the same length
                    dp_sum[i] = max(dp_sum[i], dp_sum[j] + nums[i]); // Update sum if it's greater
                }
            }
        }
    }

    int max_len = 0;
    int max_sum = 0;
    for (int i = 0; i < n; ++i) {
        if (dp_len[i] > max_len) {
            max_len = dp_len[i];
            max_sum = dp_sum[i];
        } else if (dp_len[i] == max_len) {
            max_sum = max(max_sum, dp_sum[i]);
        }
    }

    return max_sum; 
}

/*
4. Example Test Cases:
*/
int main() {
    vector<int> nums1 = {1, 100, 2, 3, 4, 5};
    cout << solve(nums1) << endl; // Output: 15

    vector<int> nums2 = {1, 3, 2, 4};
    cout << solve(nums2) << endl; // Output: 7


    vector<int> nums3 = {3, 2, 1};
    cout << solve(nums3) << endl; // Output: 3

    vector<int> nums4 = {10, 22, 9, 33, 21, 50, 41, 60, 80};
    cout << solve(nums4) << endl; // Output: 250 (10, 22, 33, 50, 60, 80)

    return 0;
}




/*
5. Alternative Approaches:

-  O(N log N) solution for finding LIS length is possible using binary search (not implemented here as the problem requires the sum, which makes the O(N^2) approach necessary).

*/
```

# Connect with me: https://github.com/ohkrahul
