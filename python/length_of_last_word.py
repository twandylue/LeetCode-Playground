class Solution:
    # time complexity: O(n)
    def lengthOfLastWord(self, s: str) -> int:
        """time complexity: O(n)"""
        r: int = len(s) - 1
        result: int = 0
        while r >= 0:
            if s[r] == " ":
                r -= 1
                continue
            l: int = r
            while s >= 0 and s[l] != " ":
                l -= 1
                result += 1
            break
        return result


def test_lengthOfLastWord_case_1():
    # arrange
    s: str = "Hello World"
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.lengthOfLastWord(s)

    # assert
    assert expected == actual
