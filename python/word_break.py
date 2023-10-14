class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp: list[bool] = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


def test_wordBreak_case_1():
    # arrange
    s: str = "leetcode"
    wordDict: list[str] = ["leet", "code"]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.wordBreak(s, wordDict)

    # assert
    assert actual == expected


def test_wordBreak_case_2():
    # arrange
    s: str = "applepenapple"
    wordDict: list[str] = ["apple", "pen"]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.wordBreak(s, wordDict)

    # assert
    assert actual == expected


def test_wordBreak_case_3():
    # arrange
    s: str = "catsandog"
    wordDict: list[str] = ["cats", "dog", "sand", "and", "cat"]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.wordBreak(s, wordDict)

    # assert
    assert actual == expected
