'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium

Solved this one during my practice session. Interesting problem that tests tree algorithms.
The key insight was to optimize the space complexity.

Link: https://practice.geeksforgeeks.org/problems/array-manipulation
'''

// Just solved this interesting problem! Here's my approach...

// First I tried brute force but realized we can optimize using cumulative sum
// This reminds me of a similar problem I solved earlier using a sliding window

// Edge case: What if the array is empty?
if (nums.length == 0) {
  return 0;
}

// Initialize the cumulative sum array
int[] cumulativeSum = new int[nums.length];
cumulativeSum[0] = nums[0];
// Calculate the cumulative sum
for (int i = 1; i < nums.length; i++) {
  cumulativeSum[i] = cumulativeSum[i - 1] + nums[i];
}

// Initialize the maximum sum
int maxSum = Integer.MIN_VALUE;

// Iterate over the cumulative sum array and calculate the maximum sum
for (int i = 0; i < nums.length; i++) {
  // Note: Remember to handle negative numbers
  int currSum = cumulativeSum[i];
  if (i > 0) {
    currSum -= cumulativeSum[i - 1];
  }
  maxSum = Math.max(maxSum, currSum);
}

// Return the maximum sum
return maxSum;

// TODO: Could probably improve the space complexity further
// TODO: Better approach might be using a heap