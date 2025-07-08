class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total: int = 0
        for c in str(x):
            total += int(c)
        return total if x % total == 0 else -1


def test_sumOfTheDigitsOfHarshadNumber_case_1():
    # Arrange
    x: int = 18
    expected: int = 9

    # Act
    actual = Solution().sumOfTheDigitsOfHarshadNumber(x)

    # Assert
    assert expected == actual


def test_sumOfTheDigitsOfHarshadNumber_case_2():
    # Arrange
    x: int = 23
    expected: int = -1

    # Act
    actual = Solution().sumOfTheDigitsOfHarshadNumber(x)

    # Assert
    assert expected == actual
