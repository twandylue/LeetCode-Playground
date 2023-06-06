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
    expected: list[int] = [0, 1]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    assert expected.sort() == actual.sort()


def test_two_sum_case_2():
    # arrange
    numbers: list[int] = [3, 2, 4]
    target: int = 6
    expected: list[int] = [1, 2]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    assert expected.sort() == actual.sort()


def test_two_sum_case_3():
    # arrange
    numbers: list[int] = [3, 3]
    target: int = 6
    expected: list[int] = [0, 1]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    assert expected.sort() == actual.sort()
