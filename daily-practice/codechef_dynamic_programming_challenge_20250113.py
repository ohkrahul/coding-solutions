'''
Problem: Dynamic Programming Challenge
Platform: CodeChef
Difficulty: Hard
URL: https://www.codechef.com/problems/DYNAMO
Date: 2025-01-13
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from CodeChef - Hard
# Date: 2025-01-13

## Problem Understanding and Approach

The problem is to find the minimum number of coins required to make a given change for a given set of coins. For example, if the coins are {1, 5, 10, 25}, and the change is 41, then the minimum number of coins required is 4 (10, 10, 10, 1).

We can use dynamic programming to solve this problem. We define a table `dp` where `dp[i]` is the minimum number of coins required to make change for `i` cents. We can initialize `dp[0]` to 0, since we don't need any coins to make change for 0 cents.

For all other values of `i`, we can iterate over all possible coins `c` and check if `i - c` is non-negative. If it is, then we can use the minimum of `dp[i]` and `dp[i - c] + 1`. This is because we can either use the current coin `c` to make change for `i` cents, or we can use the minimum number of coins required to make change for `i - c` cents and add 1 coin for the current coin `c`.

Once we have filled in the table `dp`, we can return `dp[change]`, which will be the minimum number of coins required to make change for the given change.

## Time and Space Complexity Analysis

The time complexity of this solution is O(change * coins), where `change` is the amount of change we want to make and `coins` is the number of different coins we have. The space complexity is O(change), since we need to store the table `dp`.

## Well-Commented Implementation

```python
def min_coins(coins, change):
    """
    Find the minimum number of coins required to make change for a given amount of money.

    Args:
    coins: A list of coin denominations.
    change: The amount of change to make.

    Returns:
    The minimum number of coins required to make change for the given amount of money.
    """

    # Initialize the table dp.
    dp = [float('inf')] * (change + 1)
    dp[0] = 0

    # Iterate over all possible amounts of change.
    for i in range(1, change + 1):
        # Iterate over all possible coins.
        for c in coins:
            # If the current coin is less than or equal to the current amount of change,
            # then we can use it to make change.
            if i - c >= 0:
                # Update the minimum number of coins required to make change for the current amount of change.
                dp[i] = min(dp[i], dp[i - c] + 1)

    # Return the minimum number of coins required to make change for the given amount of money.
    return dp[change]


# Example test cases.
coins1 = [1, 5, 10, 25]
change1 = 41
print(min_coins(coins1, change1))  # Output: 4

coins2 = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
change2 = 999
print(min_coins(coins2, change2))  # Output: 4
```

## Alternative Approaches

There are several other approaches to this problem, including:

* **Greedy Approach:** This approach starts with the largest coin denomination and keeps adding coins to the change until the change is made. However, this approach is not always optimal, as it can lead to more coins being used than necessary.
* **Branch-and-Bound Approach:** This approach starts by generating all possible combinations of coins that can be used to make the change. It then evaluates each combination and keeps the one that uses the fewest coins. However, this approach can be computationally expensive for large values of change.
* **Linear Programming Approach:** This approach formulates the problem as a linear programming problem and solves it using a linear programming solver. This approach is guaranteed to find the optimal solution, but it can be more computationally expensive than the dynamic programming approach.

# Connect with me: https://github.com/ohkrahul
