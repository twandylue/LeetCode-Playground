class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp: list[int] = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1


def test_coinChange_case_1():
    # arrange
    coins: list[int] = [1, 2, 5]
    amount: int = 11
    expected: int = 3

    # act
    solution = Solution()
    result = solution.coinChange(coins, amount)

    # assert
    assert result == expected


def test_coinChange_case_2():
    # arrange
    coins: list[int] = [2]
    amount: int = 3
    expected: int = -1

    # act
    solution = Solution()
    result = solution.coinChange(coins, amount)

    # assert
    assert result == expected


def test_coinChange_case_3():
    # arrange
    coins: list[int] = [1]
    amount: int = 0
    expected: int = 0

    # act
    solution = Solution()
    result = solution.coinChange(coins, amount)

    # assert
    assert result == expected
