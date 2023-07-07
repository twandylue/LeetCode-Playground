class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left: int = 1
        right: int = max(piles)

        while left <= right:
            mid: int = (left + right) // 2
            count: int = 0
            for pile in piles:
                count += (pile + mid - 1) // mid

            if count <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left


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