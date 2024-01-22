class Solution:
    # NOTE: time complexity: O(mlogm + nlogm)
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        result: list[int] = list()
        potions.sort()

        for s in spells:
            n: int = self.findLowerPos(s, potions, success)
            result.append(len(potions) - n)

        return result

    def findLowerPos(self, s: int, potions: list[int], success: int) -> int:
        l: int = 0
        r: int = len(potions) - 1
        idx: int = len(potions)
        while l <= r:
            mid: int = (l + r) // 2
            if s * potions[mid] >= success:
                r = mid - 1
                idx = mid
            else:
                l = mid + 1

        return idx

    # NOTE: Also works
    # def successfulPairs(
    #     self, spells: list[int], potions: list[int], success: int
    # ) -> list[int]:
    #     result: list[int] = list()
    #     potions.sort()
    #     for s in spells:
    #         number: int = success // s + 1 if success % s > 0 else success // s
    #         index: int = self.findMostLeftLarge(potions, number)
    #         if index == -1:
    #             result.append(0)
    #         else:
    #             result.append(len(potions) - index)
    #
    #     return result
    #
    # def findMostLeftLarge(self, potions: list[int], target: int) -> int:
    #     l: int = 0
    #     r: int = len(potions) - 1
    #     result: int = -1
    #     while l <= r:
    #         mid: int = (l + r) // 2
    #         if potions[mid] == target:
    #             result = mid
    #             r = mid - 1
    #         elif potions[mid] > target:
    #             result = mid
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    #
    #     return result


def test_successfulPairs_case_1():
    # arrange
    spells: list[int] = [5, 1, 3]
    potions: list[int] = [1, 2, 3, 4, 5]
    success: int = 7
    expected: list[int] = [4, 0, 3]

    # act
    solution = Solution()
    actual = solution.successfulPairs(spells, potions, success)

    # assert
    assert expected == actual


def test_successfulPairs_case_2():
    # arrange
    spells: list[int] = [3, 1, 2]
    potions: list[int] = [8, 5, 8]
    success: int = 16
    expected: list[int] = [2, 0, 2]

    # act
    solution = Solution()
    actual = solution.successfulPairs(spells, potions, success)

    # assert
    assert expected == actual


def test_successfulPairs_case_3():
    # arrange
    spells: list[int] = [15, 8, 19]
    potions: list[int] = [38, 36, 23]
    success: int = 328
    expected: list[int] = [3, 0, 3]

    # act
    solution = Solution()
    actual = solution.successfulPairs(spells, potions, success)

    # assert
    assert expected == actual
