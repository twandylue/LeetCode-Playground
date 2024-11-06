class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """time complexity: O(n^2) where n is the length of s"""
        return self.longestCommonSubsequence(s, s[::-1])

    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        """time complexity: O(n*m) where n is the length of text1 and m is the length of text2"""
        dp: list[list[int]] = [
            [0 for _ in range(len(t2) + 1)] for _ in range(len(t1) + 1)
        ]
        for i in range(len(t1) - 1, -1, -1):
            for j in range(len(t2) - 1, -1, -1):
                if t1[i] == t2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]


def test_longestPalindromeSubseq_case_1():
    # arrange
    s: str = "bbbab"
    expected: int = 4

    # act
    actual = Solution().longestPalindromeSubseq(s)

    # aasert
    assert expected == actual


def test_longestPalindromeSubseq_case_2():
    # arrange
    s: str = "cbbd"
    expected: int = 2

    # act
    actual = Solution().longestPalindromeSubseq(s)

    # aasert
    assert expected == actual
