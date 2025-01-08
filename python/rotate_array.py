class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """time complexity: O(n)"""
        k = k % len(nums)
        if k == 0:
            return
        # Reverse the nums
        self.reverse(nums, 0, len(nums) - 1)
        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # Reverse the rest of the elements
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: list[int], l: int, r: int) -> None:
        while l <= r:
            tmp: int = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1

    def rotate2(self, nums: list[int], k: int) -> None:
        nums.reverse()
        k %= len(nums)
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


def test_rotate_case_1():
    # arrange
    nums: list[int] = [1, 2, 3, 4, 5, 6, 7]
    k: int = 3
    expected: list[int] = [5, 6, 7, 1, 2, 3, 4]

    # act
    solution = Solution()
    solution.rotate(nums, k)

    # assert
    assert expected == nums


def test_rotate_case_2():
    # arrange
    nums: list[int] = [-1, -100, 3, 99]
    k: int = 2
    expected: list[int] = [3, 99, -1, -100]

    # act
    solution = Solution()
    solution.rotate(nums, k)

    # assert
    assert expected == nums


def test_rotate_case_3():
    # arrange
    nums: list[int] = [-1]
    k: int = 2
    expected: list[int] = [-1]

    # act
    solution = Solution()
    solution.rotate(nums, k)

    # assert
    assert expected == nums


def test_rotate_case_4():
    # arrange
    nums: list[int] = [1, 2]
    k: int = 3
    expected: list[int] = [2, 1]

    # act
    solution = Solution()
    solution.rotate(nums, k)

    # assert
    assert expected == nums
