class Solution:
    def intervalIntersection(
        self, firstlist: list[list[int]], secondlist: list[list[int]]
    ) -> list[list[int]]:
        """time complexity: O(n)"""
        i: int = 0
        j: int = 0
        result: list[int] = []
        while i < len(firstlist) and j < len(secondlist):
            a_s, a_e = firstlist[i]
            b_s, b_e = secondlist[j]
            if a_s <= b_e and a_e >= b_s:
                result.append([max(a_s, b_s), min(a_e, b_e)])
            if a_e <= b_e:
                i += 1
            else:
                j += 1
        return result


def test_intervalIntersection_case_1():
    # arrange
    firstList: list[list[int]] = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList: list[list[int]] = [[1, 5], [8, 12], [15, 24], [25, 26]]
    expected: list[int] = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    # act
    actual = Solution().intervalIntersection(firstList, secondList)

    # assert
    assert expected == actual


def test_intervalIntersection_case_2():
    # arrange
    firstList: list[list[int]] = [[1, 3], [5, 9]]
    secondList: list[list[int]] = []
    expected: list[int] = []

    # act
    actual = Solution().intervalIntersection(firstList, secondList)

    # assert
    assert expected == actual
