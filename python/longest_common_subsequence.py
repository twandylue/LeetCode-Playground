class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """time complexity: O(n*m) where n is the length of text1 and m is the length of text2"""
        dp: list[list[int]] = [
            [0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)
        ]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]


def test_longestCommonSubsequence_case_1():
    # arrange
    text1: str = "abcde"
    text2: str = "ace"
    expected: int = 3

    # act
    actual = Solution().longestCommonSubsequence(text1, text2)

    # aasert
    assert expected == actual


def test_longestCommonSubsequence_case_2():
    # arrange
    text1: str = "abc"
    text2: str = "abc"
    expected: int = 3

    # act
    actual = Solution().longestCommonSubsequence(text1, text2)

    # aasert
    assert expected == actual


def test_longestCommonSubsequence_case_3():
    # arrange
    text1: str = "abc"
    text2: str = "def"
    expected: int = 0

    # act
    actual = Solution().longestCommonSubsequence(text1, text2)

    # aasert
    assert expected == actual
