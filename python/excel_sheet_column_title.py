class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result: str = ""
        while columnNumber > 0:
            offset: int = (columnNumber - 1) % 26
            result += chr(ord("A") + offset)
            columnNumber = (columnNumber - 1) // 26
        return result[::-1]


def test_convertToTitle_case_1():
    # arrange
    columnNumber: int = 1
    expected: str = "A"

    # act
    actual = Solution().convertToTitle(columnNumber)

    # assert
    assert actual == expected


def test_convertToTitle_case_2():
    # arrange
    columnNumber: int = 28
    expected: str = "AB"

    # act
    actual = Solution().convertToTitle(columnNumber)

    # assert
    assert actual == expected


def test_convertToTitle_case_3():
    # arrange
    columnNumber: int = 701
    expected: str = "ZY"

    # act
    actual = Solution().convertToTitle(columnNumber)

    # assert
    assert actual == expected
