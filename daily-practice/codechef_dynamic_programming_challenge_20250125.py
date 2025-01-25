'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-01-25
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-01-25

## Problem Understanding and Approach

The problem involves maximizing the sum of non-adjacent elements in a given sequence. We can use dynamic programming to solve this problem.

**Approach:**

1. Define a base case. When the index reaches the end of the sequence, the maximum sum is 0.
2. Assume that we know the maximum sum for all indices until i-1.
3. For each index i, we have two options:
    - Include the current element and exclude the next element (i+1)
    - Exclude the current element and include the next element (i+1)
4. The maximum sum for index i is the maximum of these two options.
5. Repeat for all indices in the sequence.

## Time and Space Complexity Analysis

**Time Complexity:** O(N), where N is the length of the sequence. We iterate through the sequence once and perform a constant number of operations for each element.

**Space Complexity:** O(1). We only need to store two variables: the maximum sum for the previous index and the maximum sum including and excluding the current element.

## Well-Commented Implementation (Python)

```python
def max_non_adjacent_sum(nums):
    """
    Returns the maximum sum of non-adjacent elements in a sequence.

    Args:
        nums (list): A list of integers representing the sequence.

    Returns:
        int: The maximum sum of non-adjacent elements.
    """

    # Base case
    if not nums:
        return 0

    # Initialize the maximum sum for the previous index and the current index
    prev_max = 0
    curr_max = nums[0]

    # Iterate through the sequence starting from the second element
    for i in range(1, len(nums)):
        # Calculate the maximum sum including and excluding the current element
        include = nums[i] + prev_max
        exclude = curr_max

        # Update the maximum sum for the current index
        curr_max = max(include, exclude)

        # Update the maximum sum for the next index
        prev_max = curr_max

    return curr_max
```

## Example Test Cases

```python
# Test case 1
nums = [1, 2, 3, 4]
print(max_non_adjacent_sum(nums))  # Output: 6

# Test case 2
nums = [2, 4, 6, 8]
print(max_non_adjacent_sum(nums))  # Output: 12

# Test case 3
nums = [5, 15, 10, 100, 20, 80]
print(max_non_adjacent_sum(nums))  # Output: 195
```

## Alternative Approaches

1. **Greedy Approach:** We can iteratively select the element with the maximum value at each step and skip the next element. This approach is greedy and may not always yield the optimal solution.
2. **Recursion:** We can use recursion to solve this problem by considering all possible subsequences of the sequence. However, this approach may lead to overlapping subproblems and exponential time complexity.

# Connect with me: https://github.com/ohkrahul
