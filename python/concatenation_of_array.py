class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        result: list[int] = [0] * 2 * n
        for i in range(len(nums)):
            result[i] = nums[i]
            result[i + n] = nums[i]

        return result


def test_getConcatenation_case_1():
    # Arrange
    nums: list[int] = [1, 2, 1]
    expected: list[int] = [1, 2, 1, 1, 2, 1]

    # Act
    solution = Solution()
    actual = solution.getConcatenation(nums)

    # Assert
    assert expected == actual
