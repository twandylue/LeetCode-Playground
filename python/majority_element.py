class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        numMap: dict[int, int] = dict()
        for i in range(len(nums)):
            if nums[i] not in numMap:
                numMap[nums[i]] = 1
            else:
                numMap[nums[i]] += 1
                if numMap[nums[i]] > len(nums) / 2:
                    return nums[i]
        return 0

    def majorityElement2(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        count: int = 1
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            if count > len(nums) // 2:
                return nums[i]
        return -1

    def majorityElement3(self, nums: list[int]) -> int:
        # Time Complexity: O(n), Space Complexity: O(1)
        count: int = 0
        candidate: int = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate


def test_majorityElement_case_1():
    # arrange
    nums: list[int] = [3, 2, 3]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.majorityElement(nums)

    # assert
    assert expected == actual


def test_majorityElement_case_2():
    # arrange
    nums: list[int] = [2, 2, 1, 1, 1, 2, 2]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.majorityElement(nums)

    # assert
    assert expected == actual


def test_majorityElement_case_3():
    # arrange
    nums: list[int] = [2, 2, 1, 1, 1, 2, 2]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.majorityElement3(nums)

    # assert
    assert expected == actual
