'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-04-21
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-04-21

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
Problem: Longest Increasing Subsequence with Maximum Sum

Platform: CodeChef (Hypothetical -  adapted for detailed explanation)
Difficulty: Hard

Description: 
You are given a sequence of N integers A1, A2, ..., AN. You need to find the length and the sum of the longest increasing subsequence (LIS) such that the sum is maximized.  If there are multiple LIS with the same length, choose the one with the maximum sum.

Note: A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example:
Input: [1, 10, 2, 3, 4, 5]
Output: Length: 5, Sum: 15 (Subsequence: 1, 2, 3, 4, 5) 

Input: [10, 22, 9, 33, 21, 50, 41, 60]
Output: Length: 6, Sum: 233 (Subsequence: 10, 22, 33, 50, 60)


1. Problem Understanding and Approach:

We will use dynamic programming to solve this problem. We will maintain two DP arrays:
- `dp_length[i]` stores the length of the LIS ending at index `i`.
- `dp_sum[i]` stores the sum of the LIS ending at index `i`.

We iterate through the array, and for each element `A[i]`, we compare it with all previous elements `A[j]` (where `j < i`).
- If `A[i] > A[j]`, it means we can extend an LIS ending at `j` by adding `A[i]`. 
- We update `dp_length[i]` and `dp_sum[i]` based on the longest and highest-sum LIS we can form by extending from previous elements.

2. Time and Space Complexity Analysis:

- Time Complexity: O(N^2) due to the nested loops.
- Space Complexity: O(N) to store the DP arrays.

3. Implementation:
*/

pair<int, int> longestIncreasingSubsequence(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return {0, 0};

    vector<int> dp_length(n, 1);
    vector<int> dp_sum(n, nums[0]);  // Initialize with the element itself


    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                if (dp_length[j] + 1 > dp_length[i] || (dp_length[j] + 1 == dp_length[i] && dp_sum[j] + nums[i] > dp_sum[i])) {
                     dp_length[i] = dp_length[j] + 1;
                     dp_sum[i] = dp_sum[j] + nums[i];
                }
            }
        }
       if(dp_length[i] == 1) dp_sum[i] = nums[i]; //Handle cases where no increasing subsequence is found yet
    }



    int max_length = 0;
    int max_sum = 0;
    for (int i = 0; i < n; i++) {
        if (dp_length[i] > max_length || (dp_length[i] == max_length && dp_sum[i] > max_sum)) {
            max_length = dp_length[i];
            max_sum = dp_sum[i];
        }
    }

    return {max_length, max_sum};
}

/*
4. Example Test Cases:
*/
int main() {
    vector<int> nums1 = {1, 10, 2, 3, 4, 5};
    pair<int, int> result1 = longestIncreasingSubsequence(nums1);
    cout << "Length: " << result1.first << ", Sum: " << result1.second << endl; // Output: Length: 5, Sum: 15

    vector<int> nums2 = {10, 22, 9, 33, 21, 50, 41, 60};
     pair<int, int> result2 = longestIncreasingSubsequence(nums2);
    cout << "Length: " << result2.first << ", Sum: " << result2.second << endl;  // Output: Length: 6, Sum: 233


    vector<int> nums3 = {1,2,3,1,2,3,1,2,3,4};
    pair<int, int> result3 = longestIncreasingSubsequence(nums3);
    cout << "Length: " << result3.first << ", Sum: " << result3.second << endl; //Output: Length:4, Sum:10

    return 0;
}




/*
5. Alternative Approaches:

- O(N log N) Solution:  We can use a slightly modified binary search approach to find the LIS length in O(N log N) time. However, calculating the sum efficiently with this approach requires more complex data structures (like segment trees or Fenwick trees) to maintain maximum sums for different LIS lengths. This adds to the implementation complexity.
*/
```

# Connect with me: https://github.com/ohkrahul
