class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        result: list[int] = list()
        l: int = len(nums) // 2 - 1 if len(nums) % 2 == 0 else len(nums) // 2
        h: int = l
        r: int = len(nums) - 1
        while len(nums) != len(result):
            if l >= 0:
                result.append(nums[l])
                l -= 1
            if r > h:
                result.append(nums[r])
                r -= 1

        for i in range(len(result)):
            nums[i] = result[i]


def test_wiggleSort_case_1():
    # arrange
    nums: list[int] = [1, 5, 1, 1, 6, 4]
    expected: list[int] = [1, 6, 1, 5, 1, 4]

    # act
    solution = Solution()
    solution.wiggleSort(nums)

    # assert
    assert expected == nums


def test_wiggleSort_case_2():
    # arrange
    nums: list[int] = [1, 3, 2, 2, 3, 1]
    expected: list[int] = [2, 3, 1, 3, 1, 2]

    # act
    solution = Solution()
    solution.wiggleSort(nums)

    # assert
    assert expected == nums


def test_wiggleSort_case_3():
    # arrange
    nums: list[int] = [4, 5, 5, 6]
    expected: list[int] = [5, 6, 4, 5]

    # act
    solution = Solution()
    solution.wiggleSort(nums)

    # assert
    assert expected == nums


def test_wiggleSort_case_4():
    # arrange
    nums: list[int] = [1, 4, 3, 4, 1, 2, 1, 3, 1, 3, 2, 3, 3]
    expected: list[int] = [3, 4, 2, 4, 2, 3, 1, 3, 1, 3, 1, 3, 1]

    # act
    solution = Solution()
    solution.wiggleSort(nums)

    # assert
    assert expected == nums
