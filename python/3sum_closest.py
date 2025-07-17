class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        result: int = float("inf")
        diff: int = float("inf")
        nums.sort()
        for i in range(len(nums) - 2):
            j: int = i + 1
            k: int = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    return target
                if abs(target - nums[i] - nums[j] - nums[k]) < diff:
                    diff = abs(target - nums[i] - nums[j] - nums[k])
                    result = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return result


def test_threeSumClosest_case_1():
    # arrange
    nums: list[int] = [-1, 2, 1, -4]
    target: int = 1
    expected: int = 2

    # act
    actual = Solution().threeSumClosest(nums, target)

    # assert
    assert expected == actual


def test_threeSumClosest_case_2():
    # arrange
    nums: list[int] = [0, 0, 0]
    target: int = 1
    expected: int = 0

    # act
    actual = Solution().threeSumClosest(nums, target)

    # assert
    assert expected == actual
