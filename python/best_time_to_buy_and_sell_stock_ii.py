class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxPrice: int = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] < prices[i]:
                continue
            else:
                maxPrice += prices[i + 1] - prices[i]

        return maxPrice


def test_maxProfit_case_1():
    # arrange
    prices: list[int] = [7, 1, 5, 3, 6, 4]
    expected: int = 7

    # act
    solution = Solution()
    actual = solution.maxProfit(prices)

    # assert
    assert expected == actual


def test_maxProfit_case_2():
    # arrange
    prices: list[int] = [1, 2, 3, 4, 5]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.maxProfit(prices)

    # assert
    assert expected == actual


def test_maxProfit_case_3():
    # arrange
    prices: list[int] = [7, 6, 4, 3, 1]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.maxProfit(prices)

    # assert
    assert expected == actual
