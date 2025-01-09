class Solution:
    def longestCommonPrefix2(self, strs: list[str]) -> str:
        """time complexity: O(m * n) where m is the length of the shortest string and n is the number of strings"""
        result: str = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return result
            result += strs[0][i]

        return result

    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortestStr: str = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < len(shortestStr):
                shortestStr = strs[i]

        result: str = shortestStr
        for j in range(len(strs)):
            p: str = self.find_prefix(strs[j], shortestStr)
            if len(p) < len(result):
                result = p

        return result

    def find_prefix(self, s: str, base: str) -> str:
        result: str = ""
        r: int = 0
        while r < len(base):
            if base[r] != s[r]:
                break
            result += s[r]
            r += 1

        return result


def test_longestCommonPrefix_case_1():
    # arrange
    strs: list[str] = ["flower", "flow", "flight"]
    expected: str = "fl"

    # act
    solution = Solution()
    actual = solution.longestCommonPrefix(strs)

    # aasert
    assert expected == actual


def test_longestCommonPrefix_case_2():
    # arrange
    strs: list[str] = ["dog", "racecar", "car"]
    expected: str = ""

    # act
    solution = Solution()
    actual = solution.longestCommonPrefix(strs)

    # aasert
    assert expected == actual


def test_longestCommonPrefix_case_3():
    # arrange
    strs: list[str] = ["cir", "car"]
    expected: str = "c"

    # act
    solution = Solution()
    actual = solution.longestCommonPrefix(strs)

    # aasert
    assert expected == actual


def test_longestCommonPrefix_case_4():
    # arrange
    strs: list[str] = ["reflower", "flow", "flight"]
    expected: str = ""

    # act
    solution = Solution()
    actual = solution.longestCommonPrefix(strs)

    # aasert
    assert expected == actual
