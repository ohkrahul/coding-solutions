'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
Link: https://www.codechef.com/problems/DYNAMO
'''
```
def max_subarray(nums: List[int]) -> int:
    """
    Finds the maximum sum of a contiguous subarray in a given list of numbers.

    Args:
        nums: List of integers

    Returns:
        Maximum sum of a contiguous subarray
    """
    # Create a table to store the maximum sum at each index
    dp = [0] * len(nums)
    
    # Initialize the first element of the table
    dp[0] = nums[0]
    
    # Iterate over the list and update the table
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
    
    # Return the maximum sum in the table
    return max(dp)
```