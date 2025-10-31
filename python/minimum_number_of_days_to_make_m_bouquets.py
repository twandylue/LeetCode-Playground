class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        l: int = 1
        r: int = max(bloomDay)
        while l < r:
            mid: int = l + (r - l) // 2
            if self.feasible(mid, bloomDay, m, k):
                r = mid
            else:
                l = mid + 1
        return l

    def feasible(self, day: int, bloomDay: list[int], m: int, k: int) -> bool:
        flowers: int = 0
        bouquets: int = 0
        for bloom in bloomDay:
            if bloom > day:
                flowers = 0
            else:
                bouquets += (flowers + 1) // k
                flowers = (flowers + 1) % k
        return bouquets >= m


def test_minDays_1():
    # arrange
    bloomDay: list[int] = [1, 10, 3, 10, 2]
    m: int = 3
    k: int = 1
    expected: int = 3

    # act
    actual = Solution().minDays(bloomDay, m, k)

    # assert
    assert expected == actual


def test_minDays_2():
    # arrange
    bloomDay: list[int] = [1, 10, 3, 10, 2]
    m: int = 3
    k: int = 2
    expected: int = -1

    # act
    actual = Solution().minDays(bloomDay, m, k)

    # assert
    assert expected == actual


def test_minDays_3():
    # arrange
    bloomDay: list[int] = [7, 7, 7, 7, 12, 7, 7]
    m: int = 2
    k: int = 3
    expected: int = 12

    # act
    actual = Solution().minDays(bloomDay, m, k)

    # assert
    assert expected == actual
