class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # Time complexity: O(n), Space complexity: O(1)
        target: int = sum(nums) - x
        longest: int = -1
        l: int = 0
        accu: int = 0
        for r in range(len(nums)):
            accu += nums[r]
            while accu > target and l <= r:
                accu -= nums[l]
                l += 1
            if accu == target:
                longest = max(longest, r - l + 1)
        return len(nums) - longest if longest > -1 else -1


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
