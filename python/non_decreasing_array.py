class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        count: int = 0
        max: int = nums[0]
        for i in range(0, len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if count == 1:
                return False

            if i == 0 or nums[i + 1] >= nums[i - 1]:
                # [3, 5, 4, 3]
                nums[i] = nums[i + 1]
            else:
                # [3, 4, 2, 3]
                nums[i + 1] = nums[i]

            count += 1

        return True


def test_checkPossibility_case_1():
    # arrange
    nums: list[int] = [4, 2, 3]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.checkPossibility(nums)

    # assert
    assert expected == actual


def test_checkPossibility_case_2():
    # arrange
    nums: list[int] = [4, 2, 1]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.checkPossibility(nums)

    # assert
    assert expected == actual


def test_checkPossibility_case_3():
    # arrange
    nums: list[int] = [3, 4, 2, 3]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.checkPossibility(nums)

    # assert
    assert expected == actual
