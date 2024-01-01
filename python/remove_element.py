class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val and i < len(nums) - 1:
                for j in range(i + 1, len(nums)):
                    if nums[j] == val:
                        continue
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
        result: int = 0
        for i in range(len(nums)):
            if nums[i] == val:
                break
            result += 1

        return result


def test_removeElement_case_1():
    # arrange
    nums: list[int] = [3, 2, 2, 3]
    val: int = 3
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.removeElement(nums, val)

    # assert
    assert expected == actual


def test_removeElement_case_2():
    # arrange
    nums: list[int] = [0, 1, 2, 2, 3, 0, 4, 2]
    val: int = 2
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.removeElement(nums, val)

    # assert
    assert expected == actual
