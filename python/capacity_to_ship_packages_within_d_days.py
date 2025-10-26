class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """time complexity: O(n)"""
        l: int = sum(weights) // days
        r: int = sum(weights)
        while l <= r:
            mid: int = (l + r) // 2
            if self.can_ship(mid, weights, days):
                r = mid - 1
            else:
                l = mid + 1
        return l

    def can_ship(self, cap: int, weights: list[int], days: int) -> bool:
        accu_days: int = 0
        accu: int = 0
        for w in weights:
            if w > cap:
                return False
            accu += w
            if accu > cap:
                accu_days += 1
                accu = w
        if accu > 0:
            accu_days += 1
        return accu_days <= days

    def shipWithinDays2(self, weights: list[int], days: int) -> int:
        l: int = max(weights)
        r: int = sum(weights)
        while l < r:
            mid: int = l + (r - l) // 2
            if self.feasible(mid, weights, days):
                r = mid
            else:
                l = mid + 1
        return l

    def feasible(self, n: int, weights: list[int], days: int) -> bool:
        total_days: int = 1
        accu: int = 0
        for weight in weights:
            accu += weight
            if accu > n:
                total_days += 1
                accu = weight
        return total_days <= days


def test_shipWithinDays_case_1():
    # arrange
    weights: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days: int = 5
    expected: int = 15

    # act
    solution = Solution()
    actual = solution.shipWithinDays(weights, days)

    # assert
    assert expected == actual


def test_shipWithinDays_case_2():
    # arrange
    weights: list[int] = [3, 2, 2, 4, 1, 4]
    days: int = 3
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.shipWithinDays(weights, days)

    # assert
    assert expected == actual


def test_shipWithinDays_case_3():
    # arrange
    weights: list[int] = [1, 2, 3, 1, 1]
    days: int = 4
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.shipWithinDays(weights, days)

    # assert
    assert expected == actual


def test_shipWithinDays_case_4():
    # arrange
    weights: list[int] = [1, 2, 3, 1, 1]
    days: int = 4
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.shipWithinDays2(weights, days)

    # assert
    assert expected == actual
