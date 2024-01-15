class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l: int = 1
        r: int = max(piles)
        while l <= r:
            mid: int = (l + r) // 2
            count: int = 0
            for p in piles:
                if p % mid > 0:
                    count += p // mid + 1
                else:
                    count += p // mid
            if count > h:
                l = mid + 1
            else:
                r = mid - 1

        return l


def test_minEatingSpeed_case_1():
    # arrange
    piles = [3, 6, 7, 11]
    h = 8
    expected = 4

    # act
    solution = Solution()
    actual = solution.minEatingSpeed(piles, h)

    # assert
    assert expected == actual


def test_minEatingSpeed_case_2():
    # arrange
    piles = [30, 11, 23, 4, 20]
    h = 5
    expected = 30

    # act
    solution = Solution()
    actual = solution.minEatingSpeed(piles, h)

    # assert
    assert expected == actual


def test_minEatingSpeed_case_3():
    # arrange
    piles = [30, 11, 23, 4, 20]
    h = 6
    expected = 23

    # act
    solution = Solution()
    actual = solution.minEatingSpeed(piles, h)

    # assert
    assert expected == actual
