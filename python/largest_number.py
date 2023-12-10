import functools


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums.sort(key=functools.cmp_to_key(self.compare))

        return "0" if nums[0] == "0" else "".join(nums)

    def compare(self, n: str, m: str) -> int:
        if n + m > m + n:
            return -1
        elif n + m == m + n:
            return 0
        else:
            return 1


def test_largestNumber_case_1():
    # arrange
    nums: list[int] = [10, 2]
    expected: str = "210"

    # act
    solution = Solution()
    actual = solution.largestNumber(nums)

    # assert
    assert expected == actual


def test_largestNumber_case_2():
    # arrange
    nums: list[int] = [3, 30, 34, 5, 9]
    expected: str = "9534330"

    # act
    solution = Solution()
    actual = solution.largestNumber(nums)

    # assert
    assert expected == actual
