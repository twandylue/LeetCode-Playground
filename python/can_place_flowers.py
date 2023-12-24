class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if i > 0:
                    flowerbed[i - 1] = -1
                if i < len(flowerbed) - 1:
                    flowerbed[i + 1] = -1
        i: int = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                n -= 1
                if n == 0:
                    return True
                i += 2
                continue
            i += 1

        return False


def test_canPlaceFlowers_case_1():
    # arrange
    flowerbed: list[int] = [1, 0, 0, 0, 1]
    n: int = 1
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.canPlaceFlowers(flowerbed, n)

    # assert
    assert expected == actual


def test_canPlaceFlowers_case_2():
    # arrange
    flowerbed: list[int] = [1, 0, 1, 0, 1, 0, 1]
    n: int = 0
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.canPlaceFlowers(flowerbed, n)

    # assert
    assert expected == actual
