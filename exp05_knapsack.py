"""Experiment 5: 0/1 Knapsack - maximize value within a weight limit
using bottom-up (tabulation) and top-down (memoization)  -- CO-2"""

from functools import lru_cache


# ---------- Bottom-up (tabulation) ----------
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    # dp[i][w] = best value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]                     # skip item i
            if weights[i - 1] <= w:                     # take item i
                dp[i][w] = max(dp[i][w],
                               values[i - 1] + dp[i - 1][w - weights[i - 1]])

    # find which items were chosen
    chosen, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], sorted(chosen)


# ---------- Top-down (recursion + memoization) ----------
def knapsack_top_down(weights, values, capacity):
    n = len(weights)

    @lru_cache(maxsize=None)
    def solve(i, w):
        if i == n or w == 0:
            return 0
        best = solve(i + 1, w)                          # skip
        if weights[i] <= w:                             # take
            best = max(best, values[i] + solve(i + 1, w - weights[i]))
        return best

    return solve(0, capacity)


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    best, items = knapsack_bottom_up(weights, values, capacity)
    print("Bottom-up : max value =", best, "| item indices chosen =", items)
    print("Top-down  : max value =", knapsack_top_down(weights, values, capacity))
