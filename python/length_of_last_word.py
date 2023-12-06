class Solution:
    # time complexity: O(n)
    def lengthOfLastWord(self, s: str) -> int:
        r: int = len(s) - 1
        result: int = 0
        while r >= 0:
            if not s[r] == " ":
                l: int = r
                while l >= 0 and not s[l] == " ":
                    result += 1
                    l -= 1
                break
            r -= 1

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
