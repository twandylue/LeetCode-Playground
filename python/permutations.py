class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []

        if len(nums) == 1:
            return [nums[:]]

        for _ in range(len(nums)):
            n: int = nums.pop(0)
            perms: list[list[int]] = self.permute(nums)
            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result


def test_permute_case_1():
    # arrange
    nums: list[int] = [1, 2, 3]
    expected: list[list[int]] = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]

    # act
    solution = Solution()
    actual = solution.permute(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_permute_case_2():
    # arrange
    nums: list[int] = [0, 1]
    expected: list[list[int]] = [[0, 1], [1, 0]]

    # act
    solution = Solution()
    actual = solution.permute(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_permute_case_3():
    # arrange
    nums: list[int] = [1]
    expected: list[list[int]] = [[1]]

    # act
    solution = Solution()
    actual = solution.permute(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
