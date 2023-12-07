class Solution:
    def longestPrefix(self, s: str) -> str:
        prevLSP: int = 0
        i: int = 1
        lps: list[int] = [0] * len(s)
        while i < len(s):
            if s[prevLSP] == s[i]:
                prevLSP += 1
                lps[i] = prevLSP
                i += 1
            elif prevLSP == 0:
                lps[i] = 0
                i += 1
            else:
                prevLSP = lps[prevLSP - 1]

        return "" if lps[-1] == 0 else s[len(s) - lps[-1] :]


def test_longestPrefix_case_1():
    # arrange
    s: str = "bba"
    expected: str = ""

    # act
    solution = Solution()
    actual = solution.longestPrefix(s)

    # assert
    assert expected == actual


def test_longestPrefix_case_2():
    # arrange
    s: str = "level"
    expected: str = "l"

    # act
    solution = Solution()
    actual = solution.longestPrefix(s)

    # assert
    assert expected == actual


def test_longestPrefix_case_3():
    # arrange
    s: str = "ababab"
    expected: str = "abab"

    # act
    solution = Solution()
    actual = solution.longestPrefix(s)

    # assert
    assert expected == actual
