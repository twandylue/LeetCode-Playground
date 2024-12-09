class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """time complexity: O(n), space complexity: O(1)"""
        l: int = 0
        r: int = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        return []


def test_two_sum_2_case1():
    # arrange
    numbers: list[int] = [2, 7, 11, 15]
    target: int = 9
    expected: list[int] = [1, 2]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    actual.sort()
    expected.sort()
    assert actual == expected


def test_two_sum_2_case2():
    # arrange
    numbers: list[int] = [2, 3, 4]
    target: int = 6
    expected: list[int] = [1, 3]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    actual.sort()
    expected.sort()
    assert actual == expected


def test_two_sum_2_case3():
    # arrange
    numbers: list[int] = [-1, 0]
    target: int = -1
    expected: list[int] = [1, 2]

    # act
    solution = Solution()
    actual = solution.twoSum(numbers, target)

    # assert
    actual.sort()
    expected.sort()
    assert actual == expected
