class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result: int = max(nums)
        maxNum: int = 1
        minNum: int = 1
        for n in nums:
            if n == 0:
                maxNum, minNum = 1, 1

            tmp: int = n * maxNum
            maxNum = max(n * maxNum, n * minNum, n)
            minNum = min(tmp, n * minNum, n)
            result = max(result, maxNum)

        return result


def test_maxProduct_case_1():
    # arrange
    nums: list[int] = [2, 3, -2, 4]
    expected: int = 6

    # act
    solution = Solution()
    actual: int = solution.maxProduct(nums)

    # assert
    assert actual == expected


def test_maxProduct_case_2():
    # arrange
    nums: list[int] = [-2, 0, -1]
    expected: int = 0

    # act
    solution = Solution()
    actual: int = solution.maxProduct(nums)

    # assert
    assert actual == expected


def test_maxProduct_case_3():
    # arrange
    nums: list[int] = [-4, -3, -2]
    expected: int = 12

    # act
    solution = Solution()
    actual: int = solution.maxProduct(nums)

    # assert
    assert actual == expected
