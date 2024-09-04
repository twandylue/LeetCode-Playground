class Solution:
    def makeGood(self, s: str) -> str:
        """time complexity: O(n)"""
        result: list[str] = []
        i: int = 0
        while i < len(s):
            if (
                len(result) > 0
                and result[-1].lower() == s[i].lower()
                and result[-1] != s[i]
            ):
                result.pop()
            else:
                result.append(s[i])
            i += 1
        return "".join(result)


def test_makeGood_case_1():
    # arrange
    s: str = "leEeetcode"
    expected: str = "leetcode"

    # act
    actual = Solution().makeGood(s)

    # assert
    assert expected == actual


def test_makeGood_case_2():
    # arrange
    s: str = "abBAcC"
    expected: str = ""

    # act
    actual = Solution().makeGood(s)

    # assert
    assert expected == actual
