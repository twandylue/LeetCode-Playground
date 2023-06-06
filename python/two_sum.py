class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary: dict[int, int] = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dictionary:
                return [i, dictionary[diff]]
            else:
                dictionary[nums[i]] = i

        return []


def test_two_sum_case_1():
    # arrange
    numbers: list[int] = [2, 7, 11, 15]
    target: int = 9
    expected: list[int] = [1, 2]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    assert actual == expected


def test_two_sum_case_2():
    # arrange
    numbers: list[int] = [2, 3, 4]
    target: int = 6
    expected: list[int] = [1, 3]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    assert actual == expected


def test_two_sum_case_3():
    # arrange
    numbers: list[int] = [-1, 0]
    target: int = -1
    expected: list[int] = [1, 2]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    assert actual == expected
