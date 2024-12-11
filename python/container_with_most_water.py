class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """time complexity: O(n), space complexity: O(1)"""
        result: int = 0
        l: int = 0
        r: int = len(heights) - 1
        while l < r:
            area: int = min(heights[l], heights[r]) * (r - l)
            result = max(result, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return result


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
