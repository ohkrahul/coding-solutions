'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium

Solved this one during my practice session. Interesting problem that tests array manipulation.
The key insight was to think about edge cases first.

Link: https://practice.geeksforgeeks.org/problems/array-manipulation
'''

```python
# Just solved this interesting problem! Here's my approach...

# First I tried brute force but realized we can optimize using prefix sums.
# This reminds me of a similar problem I solved earlier...

# Edge case: What if the array is empty?
if not nums:
    return 

# Iterate over the array. At each step, keep track of the maximum value so far.
max_sum = nums[0]
current_sum = 0
for num in nums:
    # Note: Remember to handle negative numbers.
    current_sum = max(0, current_sum + num)  # Reset negative sums
    max_sum = max(max_sum, current_sum)

# TODO: Could probably improve the space complexity further.
# Better approach might be using a heap.

# Return the maximum sum.
return max_sum
```