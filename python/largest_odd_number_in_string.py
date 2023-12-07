class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) % 2 == 0:
                continue
            return num[0 : i + 1]

        return ""


def test_largestOddNumber_case_1():
    # arrange
    num: str = "52"
    expected: str = "5"

    # act
    solution = Solution()
    actual = solution.largestOddNumber(num)

    # assert
    assert expected == actual


def test_largestOddNumber_case_2():
    # arrange
    num: str = "4206"
    expected: str = ""

    # act
    solution = Solution()
    actual = solution.largestOddNumber(num)

    # assert
    assert expected == actual


def test_largestOddNumber_case_3():
    # arrange
    num: str = "35427"
    expected: str = "35427"

    # act
    solution = Solution()
    actual = solution.largestOddNumber(num)

    # assert
    assert expected == actual
