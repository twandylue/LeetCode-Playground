class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea: int = 0
        l: int = 0
        r: int = len(height) - 1

        while l < r:
            area: int = (r - l) * min(height[l], height[r])
            print(area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            maxArea = max(maxArea, area)

        return maxArea


def test_maxArea_case_1():
    # arrange
    height: list[int] = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected: int = 49

    # act
    solution = Solution()
    actual = solution.maxArea(height)

    # assert
    assert expected == actual


def test_maxArea_case_2():
    # arrange
    height: list[int] = [1, 1]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.maxArea(height)

    # assert
    assert expected == actual


def test_maxArea_case_3():
    # arrange
    height: list[int] = [2, 3, 4, 5, 18, 17, 6]

    expected: int = 17

    # act
    solution = Solution()
    actual = solution.maxArea(height)

    # assert
    assert expected == actual
