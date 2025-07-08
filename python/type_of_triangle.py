class Solution:
    def triangleType(self, nums: list[int]) -> str:
        if (
            nums[0] + nums[1] <= nums[2]
            or nums[0] + nums[2] <= nums[1]
            or nums[1] + nums[2] <= nums[0]
        ):
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"
        return "scalene"


def test_triangleType_case_1():
    # arrange
    nums: list[int] = [3, 3, 3]
    expected: str = "equilateral"

    # act
    actual = Solution().triangleType(nums)

    # assert
    assert expected == actual


def test_triangleType_case_2():
    # arrange
    nums: list[int] = [3, 4, 5]
    expected: str = "scalene"

    # act
    actual = Solution().triangleType(nums)

    # assert
    assert expected == actual
