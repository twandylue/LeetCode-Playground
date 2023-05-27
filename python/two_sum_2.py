class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        s = 0
        e = len(numbers) - 1

        while s < e:
            if numbers[s] + numbers[e] < target:
                s += 1
                continue
            elif numbers[s] + numbers[e] > target:
                e -= 1
                continue
            else:
                return [s + 1, e + 1]

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
    assert actual == expected
