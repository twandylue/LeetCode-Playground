class Solution:
    def longestPalindrome(self, s: str) -> str:
        result: str = ""
        resultLen: int = 0
        for i in range(len(s)):
            l: int = i
            r: int = i
            while r < len(s) and s[l] == s[r]:
                if r - l + 1 > resultLen:
                    resultLen = r - l + 1
                    result = s[l : r + 1]
                if l > 0:
                    l -= 1
                    r += 1
                else:
                    break

            l: int = i
            r: int = i + 1
            while r < len(s) and s[l] == s[r]:
                if r - l + 1 > resultLen:
                    resultLen = r - l + 1
                    result = s[l : r + 1]
                if l > 0:
                    l -= 1
                    r += 1
                else:
                    break

        return result


def test_longestPalindrome_case_1():
    # arrange
    s: str = "babad"
    expected: str = "bab"

    # act
    solution = Solution()
    actual = solution.longestPalindrome(s)

    # assert
    assert expected == actual


def test_longestPalindrome_case_2():
    # arrange
    s: str = "cbbd"
    expected: str = "bb"

    # act
    solution = Solution()
    actual = solution.longestPalindrome(s)

    # assert
    assert expected == actual
