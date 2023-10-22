class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        resultSet: set[tuple[int]] = set()
        result: list[list[int]] = list()
        nums.sort()

        for i in range(0, len(nums) - 2):
            j: int = i + 1
            k: int = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    resultSet.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        for s in resultSet:
            result.append([s[0], s[1], s[2]])
        return result

    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = list()
        nums.sort()

        prev_i: int = -float("inf")
        for i in range(0, len(nums) - 2):
            if prev_i == nums[i]:
                continue
            j: int = i + 1
            k: int = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    prev_j = nums[j]
                    while prev_j == nums[j] and j < k:
                        j += 1

                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            prev_i = nums[i]

        return result


def test_threeSum_case_1():
    # arrange
    nums: list[int] = [-1, 0, 1, 2, -1, -4]
    expected: list[list[int]] = [[-1, -1, 2], [-1, 0, 1]]

    # act
    solution = Solution()
    actual = solution.threeSum(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_threeSum_case_2():
    # arrange
    nums: list[int] = [0, 1, 1]
    expected: list[list[int]] = []

    # act
    solution = Solution()
    actual = solution.threeSum(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_threeSum_case_3():
    # arrange
    nums: list[int] = [0, 0, 0]
    expected: list[list[int]] = [[0, 0, 0]]

    # act
    solution = Solution()
    actual = solution.threeSum(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_threeSum_case_4():
    # arrange
    nums: list[int] = [0, 0, 0, 0]
    expected: list[list[int]] = [[0, 0, 0]]

    # act
    solution = Solution()
    actual = solution.threeSum(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_threeSum_case_5():
    # arrange
    nums: list[int] = [-2, 0, 1, 1, 2]

    expected: list[list[int]] = [[-2, 0, 2], [-2, 1, 1]]

    # act
    solution = Solution()
    actual = solution.threeSum(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
