# Making Change

## Introduction

The "Making Change" problem is a classic algorithmic problem that involves finding the minimum number of coins needed to make a given amount of money using a specified set of coin denominations.

## Problem Statement

Given a set of coin denominations and a target amount, determine the minimum number of coins required to make that amount. If it is not possible to make the amount with the given denominations, return -1.

## Example

Consider the coin denominations `[1, 2, 5]` and the target amount `11`. The minimum number of coins needed to make `11` is `3` (using coins `5`, `5`, and `1`).

## Approach

### Dynamic Programming

One common approach to solve this problem is using dynamic programming. The idea is to build a table `dp` where `dp[i]` represents the minimum number of coins needed to make the amount `i`.

#### Steps:

1. Initialize a list `dp` of size `amount + 1` with a large value (e.g., `float('inf')`), except `dp[0]` which should be `0` (since no coins are needed to make `0`).
2. Iterate through each coin denomination and update the `dp` list.
3. For each coin, iterate through all amounts from the coin value to the target amount.
4. Update `dp[i]` as the minimum of `dp[i]` and `dp[i - coin] + 1`.

### Example Code

```python
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

### Sources

- [LeetCode - Coin Change Problem](https://leetcode.com/problems/coin-change/)
- [GeeksforGeeks - Coin Change Problem](https://www.geeksforgeeks.org/coin-change-dp-7/)

## Conclusion

The "Making Change" problem is a fundamental problem in computer science that can be efficiently solved using dynamic programming. Understanding this problem helps in grasping key concepts in algorithm design and optimization.
