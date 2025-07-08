class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result: list[int] = []
        p1: int = 0
        p2: int = n
        while p1 < n:
            result.append(nums[p1])
            result.append(nums[p2])
            p1 += 1
            p2 += 1
        return result


def test_shuffle_case_1():
    # arrange
    nums: list[int] = [2, 5, 1, 3, 4, 7]
    n: int = 3
    expected: list[int] = [2, 3, 5, 4, 1, 7]

    # act
    actual = Solution().shuffle(nums, n)

    # assert
    assert expected == actual


def test_shuffle_case_2():
    # arrange
    nums: list[int] = [1, 2, 3, 4, 4, 3, 2, 1]
    n: int = 4
    expected: list[int] = [1, 4, 2, 3, 3, 2, 4, 1]

    # act
    actual = Solution().shuffle(nums, n)

    # assert
    assert expected == actual
