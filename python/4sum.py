class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []
        nums.sort()
        prevI = -float("inf")
        for i in range(0, len(nums) - 3):
            if prevI == nums[i]:
                continue
            prevJ: int = -float("inf")
            for j in range(i + 1, len(nums) - 2):
                if prevJ == nums[j]:
                    continue
                k: int = j + 1
                e: int = len(nums) - 1
                while k < e:
                    if nums[i] + nums[j] + nums[k] + nums[e] == target:
                        result.append([nums[i], nums[j], nums[k], nums[e]])
                        prev: int = nums[k]
                        while prev == nums[k] and k < e:
                            k += 1
                    elif nums[i] + nums[j] + nums[k] + nums[e] > target:
                        e -= 1
                    else:
                        k += 1

                prevJ = nums[j]
            prevI = nums[i]

        return result

    ## NOTE: Time Limit Exceeded
    # def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
    #     result: list[list[int]] = []
    #     subset: list[int] = []
    #
    #     nums.sort()
    #     self.dfs(0, nums, target, 0, subset, result)
    #
    #     return result
    #
    # def dfs(
    #     self,
    #     pos: int,
    #     nums: list[int],
    #     target: int,
    #     accu: int,
    #     subset: list[int],
    #     result: list[list[int]],
    # ):
    #     if accu == target and len(subset) == 4:
    #         result.append(subset[::])
    #     if pos > len(nums) - 1 or len(subset) > 4:
    #         return
    #
    #     prev: int = -float("inf")
    #     for i in range(pos, len(nums)):
    #         if nums[i] == prev:
    #             continue
    #         subset.append(nums[i])
    #         self.dfs(i + 1, nums, target, accu + nums[i], subset, result)
    #         subset.pop()
    #         prev = nums[i]


def test_fourSum_case_1():
    # arrange
    nums: list[int] = [1, 0, -1, 0, -2, 2]
    target: int = 0
    expected: list[list[int]] = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    # act
    solution = Solution()
    actual = solution.fourSum(nums, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_fourSum_case_2():
    # arrange
    nums: list[int] = [2, 2, 2, 2, 2]
    target: int = 8
    expected: list[list[int]] = [[2, 2, 2, 2]]

    # act
    solution = Solution()
    actual = solution.fourSum(nums, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_fourSum_case_3():
    # arrange
    nums: list[int] = [2, 2, 2, 2, 2, 2, 2, 2]
    target: int = 8
    expected: list[list[int]] = [[2, 2, 2, 2]]

    # act
    solution = Solution()
    actual = solution.fourSum(nums, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_fourSum_case_4():
    # arrange
    nums: list[int] = [-1, 0, 1, 2, -1, -4]
    target: int = -1
    expected: list[list[int]] = [[-4, 0, 1, 2], [-1, -1, 0, 1]]

    # act
    solution = Solution()
    actual = solution.fourSum(nums, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_fourSum_case_5():
    # arrange
    nums: list[int] = [0]
    target: int = 0
    expected: list[list[int]] = []

    # act
    solution = Solution()
    actual = solution.fourSum(nums, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
