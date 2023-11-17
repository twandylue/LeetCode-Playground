class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap: dict[int, int] = dict()

        for i in range(0, len(nums)):
            remain: int = target - nums[i]
            if remain not in numMap:
                numMap[nums[i]] = i
            else:
                return [numMap[remain], i]

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
    expected.sort()
    actual.sort()
    assert expected == actual


def test_two_sum_case_2():
    # arrange
    numbers: list[int] = [3, 2, 4]
    target: int = 6
    expected: list[int] = [1, 2]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_two_sum_case_3():
    # arrange
    numbers: list[int] = [3, 3]
    target: int = 6
    expected: list[int] = [0, 1]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
