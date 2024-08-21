class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        """time complexity: O(n)"""
        l: int = 0
        result: int = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    result += neededTime[l]
                    l = r
                else:
                    result += neededTime[r]
            else:
                l = r
        return result


def test_minCost_case_1():
    # arrange
    colors: str = "abaac"
    neededTime: list[int] = [1, 2, 3, 4, 5]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.minCost(colors, neededTime)

    # assert
    assert expected == actual


def test_minCost_case_2():
    # arrange
    colors: str = "abc"
    neededTime: list[int] = [1, 2, 3]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.minCost(colors, neededTime)

    # assert
    assert expected == actual


def test_minCost_case_3():
    # arrange
    colors: str = "aabaa"
    neededTime: list[int] = [1, 2, 3, 4, 1]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.minCost(colors, neededTime)

    # assert
    assert expected == actual
