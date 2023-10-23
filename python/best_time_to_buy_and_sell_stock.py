class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result: int = 0
        l: int = 0
        r: int = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                result = max(result, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return result


def test_maxProfit_case_1():
    # arrange
    prices: list[int] = [7, 1, 5, 3, 6, 4]
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.maxProfit(prices)

    # assert
    assert expected == actual
