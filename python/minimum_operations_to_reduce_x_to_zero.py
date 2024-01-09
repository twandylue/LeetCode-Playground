class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        intervalLen: int = 0
        target: int = sum(nums) - x
        accu: int = 0
        l: int = 0
        flag: bool = False
        for r in range(len(nums)):
            accu += nums[r]
            currLen: int = r - l + 1
            while l <= r and accu > target:
                accu -= nums[l]
                l += 1
                currLen -= 1

            if accu == target:
                flag = True
                intervalLen = max(intervalLen, currLen)

        return -1 if not flag else len(nums) - intervalLen


def test_minOperations_case_1():
    # arrange
    nums: list[int] = [1, 1, 4, 2, 3]
    x: int = 5
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.minOperations(nums, x)

    # assert
    assert expected == actual


def test_minOperations_case_2():
    # arrange
    nums: list[int] = [5, 6, 7, 8, 9]
    x: int = 4
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.minOperations(nums, x)

    # assert
    assert expected == actual


def test_minOperations_case_3():
    # arrange
    nums: list[int] = [3, 2, 20, 1, 1, 3]
    x: int = 10
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.minOperations(nums, x)

    # assert
    assert expected == actual


def test_minOperations_case_4():
    # arrange
    nums: list[int] = [1, 1, 3, 2, 5]
    x: int = 5
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.minOperations(nums, x)

    # assert
    assert expected == actual


def test_minOperations_case_5():
    # arrange
    nums: list[int] = [1, 1]
    x: int = 3
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.minOperations(nums, x)

    # assert
    assert expected == actual


def test_minOperations_case_6():
    # arrange
    nums: list[int] = [
        8828,
        9581,
        49,
        9818,
        9974,
        9869,
        9991,
        10000,
        10000,
        10000,
        9999,
        9993,
        9904,
        8819,
        1231,
        6309,
    ]
    x: int = 134365
    expected: int = 16

    # act
    solution = Solution()
    actual = solution.minOperations(nums, x)

    # assert
    assert expected == actual
