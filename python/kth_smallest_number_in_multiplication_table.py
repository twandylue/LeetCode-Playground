class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # NOTE: Time complexity: O(m * log(m * n))
        l: int = 1
        r: int = m * n
        while l < r:
            mid: int = l + (r - l) // 2
            if self.feasible(mid, m, n, k):
                r = mid
            else:
                l = mid + 1
        return l

    def feasible(self, val: int, m: int, n: int, k: int) -> bool:
        count: int = 0
        for i in range(1, m + 1):
            count += min(val // i, n)
            if val // i == 0:
                break
        return count >= k


def test_findKthNumber_1():
    # arrange
    m: int = 3
    n: int = 3
    k: int = 5
    expected: int = 3

    # act
    actual = Solution().findKthNumber(m, n, k)

    # assert
    assert expected == actual


def test_findKthNumber_2():
    # arrange
    m: int = 2
    n: int = 3
    k: int = 6
    expected: int = 6

    # act
    actual = Solution().findKthNumber(m, n, k)

    # assert
    assert expected == actual
