import math


class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        ratioMap: dict[float, int] = dict()
        count: int = 0

        for rectangle in rectangles:
            if rectangle[0] / rectangle[1] not in ratioMap:
                ratioMap[rectangle[0] / rectangle[1]] = 1
            else:
                ratioMap[rectangle[0] / rectangle[1]] += 1

        for _, v in ratioMap.items():
            if v > 1:
                count += int(
                    math.factorial(v) / (math.factorial(2) * math.factorial(v - 2))
                )

        return count


def test_interchangeableRectangles_case_1():
    # arrange
    rectangles: list[list[int]] = [[4, 8], [3, 6], [10, 20], [15, 30]]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.interchangeableRectangles(rectangles)

    # assert
    assert expected == actual
