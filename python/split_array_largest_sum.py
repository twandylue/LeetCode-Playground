class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # NOTE: Time Complexity: O(nlogn)
        l: int = max(nums)
        r: int = sum(nums)
        while l < r:
            mid: int = l + (r - l) // 2
            if self.feasible(mid, nums, k):
                r = mid
            else:
                l = mid + 1
        return l

    def feasible(self, n: int, nums: list[int], k: int) -> bool:
        accu: int = 0
        total: int = 1
        for num in nums:
            accu += num
            if accu > n:
                accu = num
                total += 1
        return total <= k


def test_splitArray_case_1():
    # arrange
    nums: list[int] = [7, 2, 5, 10, 8]
    k: int = 2
    expected: int = 18

    # act
    actual = Solution().splitArray(nums, k)

    # assert
    assert expected == actual


def test_splitArray_case_2():
    # arrange
    nums: list[int] = [1, 2, 3, 4, 5]
    k: int = 2
    expected: int = 9

    # act
    actual = Solution().splitArray(nums, k)

    # assert
    assert expected == actual
