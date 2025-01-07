class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """time complexity: O(n)"""
        l: int = 0
        for r in range(len(nums)):
            if nums[r] == val:
                continue
            nums[l] = nums[r]
            l += 1
        return l


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
