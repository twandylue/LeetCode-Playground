class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """time complexity: O(n * log m) where n is the number of piles and m is the maximum number of bananas in a pile, space complexity: O(1)"""
        l: int = 1
        r: int = max(piles)
        result: int = r
        while l <= r:
            mid: int = (l + r) // 2
            total_time: int = 0
            for pile in piles:
                if pile % mid == 0:
                    total_time += pile / mid
                else:
                    total_time += pile // mid + 1
            if total_time <= h:
                result = min(result, mid)
                r = mid - 1
            else:
                l = mid + 1
        return result

    def minEatingSpeed2(self, piles: list[int], h: int) -> int:
        l: int = 1
        r: int = max(piles)
        while l < r:
            mid: int = l + (r - l) // 2
            if self.feasible(mid, piles, h):
                r = mid
            else:
                l = mid + 1
        return l

    def feasible(self, n: int, piles: list[int], h: int) -> bool:
        total_hours: int = 0
        for pile in piles:
            total_hours += pile // n if pile % n == 0 else pile // n + 1
        return total_hours <= h


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


def test_minEatingSpeed_case_4():
    # arrange
    piles = [30, 11, 23, 4, 20]
    h = 6
    expected = 23

    # act
    solution = Solution()
    actual = solution.minEatingSpeed2(piles, h)

    # assert
    assert expected == actual
