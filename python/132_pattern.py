class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack: list[tuple[int, int]] = list()
        minNum: int = nums[0]
        for i in range(1, len(nums)):
            while len(stack) > 0 and stack[-1][0] <= nums[i]:
                stack.pop()
            if len(stack) > 0 and nums[i] > stack[-1][1]:
                return True

            stack.append((nums[i], minNum))
            minNum = min(minNum, nums[i])

        return False


def test_find132pattern_case_1():
    # arrange
    nums: list[int] = [1, 2, 3, 4]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.find132pattern(nums)

    # assert
    assert expected == actual


def test_find132pattern_case_2():
    # arrange
    nums: list[int] = [3, 1, 4, 2]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.find132pattern(nums)

    # assert
    assert expected == actual


def test_find132pattern_case_3():
    # arrange
    nums: list[int] = [-1, 3, 2, 0]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.find132pattern(nums)

    # assert
    assert expected == actual


def test_find132pattern_case_4():
    # arrange
    nums: list[int] = [1, 0, 1, -4, -3]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.find132pattern(nums)

    # assert
    assert expected == actual


def test_find132pattern_case_5():
    # arrange
    nums: list[int] = [1, 4, 0, -1, -2, -3, -1, -2]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.find132pattern(nums)

    # assert
    assert expected == actual
