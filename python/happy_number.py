class Solution:
    def isHappy(self, n: int) -> bool:
        number_set: set[int] = set()
        while n not in number_set:
            if n == 1:
                return True
            number_set.add(n)
            n = self.sumOfSquares(n)

        return False

    def sumOfSquares(self, n: int) -> int:
        output: int = 0
        while n > 0:
            digit: int = n % 10
            output += digit**2
            n = n // 10

        return output


def test_isHappy_case_1():
    # Arrange
    input = 19
    expected_output = True

    # Act
    solution = Solution()
    actual_output = solution.isHappy(input)

    # Assert
    assert actual_output == expected_output


def test_isHappy_case_2():
    # Arrange
    input = 2
    expected_output = False

    # Act
    solution = Solution()
    actual_output = solution.isHappy(input)

    # Assert
    assert actual_output == expected_output


def test_isHappy_case_3():
    # Arrange
    input = 7
    expected_output = True

    # Act
    solution = Solution()
    actual_output = solution.isHappy(input)

    # Assert
    assert actual_output == expected_output
