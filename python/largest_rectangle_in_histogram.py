class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea: int = 0
        stack: list[tuple[int, int]] = list()
        for i in range(0, len(heights)):
            frontIndex: int = i
            while len(stack) > 0:
                if stack[-1][1] > heights[i]:
                    index, h = stack.pop()
                    frontIndex = index
                    area: int = (i - index) * h
                    maxArea = max(maxArea, area)
                else:
                    break
            stack.append((frontIndex, heights[i]))

        while len(stack) > 0:
            print(stack)
            i, h = stack.pop()
            area: int = (len(heights) - i) * h
            maxArea = max(maxArea, area)

        return maxArea


def test_LargestRectangleArea_case_1():
    # Arrange
    input: list[int] = [2, 1, 5, 6, 2, 3]
    expected: int = 10

    # Act
    actual: int = Solution().largestRectangleArea(input)

    # Assert
    assert actual == expected


def test_LargestRectangleArea_case_2():
    # Arrange
    input: list[int] = [2, 4]
    expected: int = 4

    # Act
    actual: int = Solution().largestRectangleArea(input)

    # Assert
    assert actual == expected


def test_LargestRectangleArea_case_3():
    # Arrange
    input: list[int] = [2, 1, 2]
    expected: int = 3

    # Act
    actual: int = Solution().largestRectangleArea(input)

    # Assert
    assert actual == expected
