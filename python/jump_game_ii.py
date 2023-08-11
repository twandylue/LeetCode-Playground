class Solution:
    def jump(self, nums: list[int]) -> int:
        result: int = 0
        r: int = 0
        l: int = 0
        while r < len(nums) - 1:
            farthest: int = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            result += 1

        return result


def test_jump_case_1():
    # arrange
    nums: list[int] = [2, 3, 1, 1, 4]
    expected: int = 2

    # act
    actual: int = Solution().jump(nums)

    # assert
    assert actual == expected


def test_jump_case_2():
    # arrange
    nums: list[int] = [2, 3, 0, 1, 4]
    expected: int = 2

    # act
    actual: int = Solution().jump(nums)

    # assert
    assert actual == expected
