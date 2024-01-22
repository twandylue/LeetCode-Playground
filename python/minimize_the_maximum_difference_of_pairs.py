class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        result: int = 0
        l: int = 0
        r: int = 10**9
        while l <= r:
            mid: int = (l + r) // 2
            if self.isValid(mid, nums, p):
                r = mid - 1
                result = mid
            else:
                l = mid + 1

        return result

    def isValid(self, diff: int, nums: list[int], p: int) -> bool:
        i: int = 0
        count: int = 0
        while i < len(nums) - 1:
            if abs(nums[i] - nums[i + 1]) <= diff:
                i += 2
                count += 1
            else:
                i += 1

        return count >= p


def test_minimizeMax_case_1():
    # arrange
    nums: list[int] = [10, 1, 2, 7, 1, 3]
    p: int = 2
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.minimizeMax(nums, p)

    # assert
    assert expected == actual


def test_minimizeMax_case_2():
    # arrange
    nums: list[int] = [4, 2, 1, 2]
    p: int = 1
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.minimizeMax(nums, p)

    # assert
    assert expected == actual
