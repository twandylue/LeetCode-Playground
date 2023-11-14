class Solution:
    def minSwaps(self, s: str) -> int:
        result: int = 0
        maxClosePre: int = 0
        currClosePre: int = 0
        for i in range(len(s)):
            if s[i] == "]":
                currClosePre += 1
            else:
                currClosePre -= 1

            maxClosePre = max(currClosePre, maxClosePre)

        result = int((maxClosePre + 1) / 2)
        return result


def test_minSwaps_case_1():
    # arrange
    s: str = "][]["
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.minSwaps(s)

    # assert
    assert expected == actual


def test_minSwaps_case_2():
    # arrange
    s: str = "]]][[["
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.minSwaps(s)

    # assert
    assert expected == actual


def test_minSwaps_case_3():
    # arrange
    s: str = "[]"
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.minSwaps(s)

    # assert
    assert expected == actual
