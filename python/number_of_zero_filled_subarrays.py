class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        comb: int = 0
        count: int = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                comb += self.cal_helper(count)
                count = 0

        comb += self.cal_helper(count)

        return comb

    def cal_helper(self, count: int) -> int:
        result: int = 0

        for i in range(1, count + 1):
            result += i

        return result


def test_zeroFilledSubarray_case_1():
    # arrange
    nums: list[int] = [1, 3, 0, 0, 2, 0, 0, 4]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.zeroFilledSubarray(nums)

    # assert
    assert expected == actual


def test_zeroFilledSubarray_case_2():
    # arrange
    nums: list[int] = [0, 0, 0, 2, 0, 0]
    expected: int = 9

    # act
    solution = Solution()
    actual = solution.zeroFilledSubarray(nums)

    # assert
    assert expected == actual
