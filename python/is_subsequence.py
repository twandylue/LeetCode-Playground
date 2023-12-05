class Solution:
    # time complexity: O(n)
    def isSubsequence(self, s: str, t: str) -> bool:
        i: int = 0
        j: int = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


def test_isSubsequence_case_1():
    # arrange
    s: str = "abc"
    t: str = "ahbgdc"
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isSubsequence(s, t)

    # assert
    assert expected == actual
