class Solution:
    def myPow(self, x: float, n: int) -> float:
        result: float = self.helper(x, abs(n))

        return result if n >= 0 else 1 / result

    def helper(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        result: float = self.helper(x, n // 2)
        result *= result
        return result if n % 2 == 0 else x * result


def test_myPow_case_1():
    # Arrange
    x: float = 2.00000
    n: int = 10
    expected: float = 1024.00000

    # Act
    result: float = Solution().myPow(x, n)

    # Assert
    assert result == expected


# def test_myPow_case_2():
#     # Arrange
#     x: float = 2.10000
#     n: int = 3
#     expected: float = 9.26100
#
#     # Act
#     result: float = Solution().myPow(x, n)
#
#     # Assert
#     assert result == expected


def test_myPow_case_3():
    # Arrange
    x: float = 2.00000
    n: int = -2
    expected: float = 0.25000

    # Act
    result: float = Solution().myPow(x, n)

    # Assert
    assert result == expected
