class Solution:
    # AAABAAAA
    # AAAA
    # 0123
    # NOTE: O(m+n)
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        lps: list[int] = [0] * len(needle)
        i: int = 1
        preLPS: int = 0
        while i < len(needle):
            if needle[preLPS] == needle[i]:
                preLPS += 1
                lps[i] = preLPS
                i += 1
            elif preLPS == 0:
                lps[i] = 0
                i += 1
            else:
                preLPS = lps[preLPS - 1]

        m: int = 0
        n: int = 0
        while m < len(haystack):
            if haystack[m] == needle[n]:
                m += 1
                n += 1
            else:
                if n == 0:
                    m += 1
                else:
                    n = lps[n - 1]

            if n == len(needle):
                return m - n

        return -1


def test_strStr_case_1():
    # arrange
    haystack: str = "sadbutsad"
    needle: str = "sad"
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.strStr(haystack, needle)

    # assert
    assert expected == actual


def test_strStr_case_2():
    # arrange
    haystack: str = "leetcode"
    needle: str = "leeto"
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.strStr(haystack, needle)

    # assert
    assert expected == actual


def test_strStr_case_3():
    # arrange
    haystack: str = "mississippi"
    needle: str = "issip"
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.strStr(haystack, needle)

    # assert
    assert expected == actual
