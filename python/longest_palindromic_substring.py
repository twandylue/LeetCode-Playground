class Solution:
    def longestPalindrome(self, s: str) -> str:
        """time complexity: O(n^2)"""
        idx: int = 0
        length: int = 0
        for i in range(len(s)):
            # for odd
            l: int = i
            r: int = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > length:
                    length = r - l + 1
                    idx = l
                l -= 1
                r += 1
            # for even
            l: int = i
            r: int = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > length:
                    length = r - l + 1
                    idx = l
                l -= 1
                r += 1
        return s[idx : idx + length]

    def longestPalindrome2(self, s: str) -> str:
        """time complexity: O(n^2)"""
        n: int = len(s)
        dp: list[list[bool]] = [[False] * n for _ in range(n)]
        idx: int = 0
        length: int = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if length < (j - i + 1):
                        length = j - i + 1
                        idx = i
        return s[idx : idx + length]


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
