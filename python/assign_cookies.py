class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        """time complexity: O(nlogn + mlogm)"""
        g.sort()
        s.sort()
        i: int = 0
        j: int = 0
        while i < len(g):
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j == len(s):
                break
            i += 1
            j += 1
        return i


def test_findContentChildren_case_1():
    # arrange
    g: list[int] = [1, 2, 3]
    s: list[int] = [1, 1]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.findContentChildren(g, s)

    # assert
    assert expected == actual


def test_findContentChildren_case_2():
    # arrange
    g: list[int] = [1, 2]
    s: list[int] = [1, 2, 3]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.findContentChildren(g, s)

    # assert
    assert expected == actual
