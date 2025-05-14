class Solution:
    def numDecodings(self, s: str) -> int:
        dp: dict[int, int] = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i + 1 < len(s) and (
                s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")
            ):
                dp[i] += dp[i + 2]

        return dp[0]

    def numDecodings_dfs(self, s: str) -> int:
        """time complexity: O(n)"""
        dp: dict[int, int] = {len(s): 1}
        return self.dfs(0, s, dp)

    def dfs(self, i: int, s: str, dp: dict[int, int]) -> int:
        if i in dp:
            return dp[i]
        if i >= len(s):
            return 0
        if s[i] == "0":
            return 0

        result: int = 0
        result += self.dfs(i + 1, s, dp)
        if s[i] == "1" or (i + 1 < len(s) and (s[i] == "2" and s[i + 1] in "0123456")):
            result += self.dfs(i + 2, s, dp)

        dp[i] = result
        return result


def test_numDecodings_case_1():
    # arrange
    s: str = "1"
    expected: int = 1

    # act
    solution = Solution()
    actual: int = solution.numDecodings(s)

    # assert
    assert expected == actual


def test_numDecodings_case_2():
    # arrange
    s: str = "06"
    expected: int = 0

    # act
    solution = Solution()
    actual: int = solution.numDecodings(s)

    # assert
    assert expected == actual


def test_numDecodings_case_3():
    # arrange
    s: str = "226"
    expected: int = 3

    # act
    solution = Solution()
    actual: int = solution.numDecodings(s)

    # assert
    assert expected == actual


def test_numDecodings_case_4():
    # arrange
    s: str = "12"
    expected: int = 2

    # act
    solution = Solution()
    actual: int = solution.numDecodings(s)

    # assert
    assert expected == actual


def test_numDecodings_case_5():
    # arrange
    s: str = "1"
    expected: int = 1

    # act
    solution = Solution()
    actual: int = solution.numDecodings_dfs(s)

    # assert
    assert expected == actual


def test_numDecodings_case_6():
    # arrange
    s: str = "06"
    expected: int = 0

    # act
    solution = Solution()
    actual: int = solution.numDecodings_dfs(s)

    # assert
    assert expected == actual


def test_numDecodings_case_7():
    # arrange
    s: str = "226"
    expected: int = 3

    # act
    solution = Solution()
    actual: int = solution.numDecodings_dfs(s)

    # assert
    assert expected == actual


def test_numDecodings_case_8():
    # arrange
    s: str = "12"
    expected: int = 2

    # act
    solution = Solution()
    actual: int = solution.numDecodings_dfs(s)

    # assert
    assert expected == actual
