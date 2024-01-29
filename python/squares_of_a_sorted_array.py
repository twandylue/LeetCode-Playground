class Solution:
    # NOTE: time complexity: O(n)
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result: list[int] = [0] * len(nums)
        l: int = 0
        r: int = len(nums) - 1
        i: int = len(nums) - 1
        while l <= r and i >= 0:
            if nums[l] ** 2 >= nums[r] ** 2:
                result[i] = nums[l] ** 2
                l += 1
            else:
                result[i] = nums[r] ** 2
                r -= 1
            i -= 1

        return result


def test_sortedSquares_case_1():
    # arrange
    nums: list[int] = [-4, -1, 0, 3, 10]
    expected: list[int] = [0, 1, 9, 16, 100]

    # act
    solution = Solution()
    actual = solution.sortedSquares(nums)

    # assert
    assert expected == actual


def test_sortedSquares_case_2():
    # arrange
    nums: list[int] = [-7, -3, 2, 3, 11]
    expected: list[int] = [4, 9, 9, 49, 121]

    # act
    solution = Solution()
    actual = solution.sortedSquares(nums)

    # assert
    assert expected == actual
