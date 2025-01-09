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
            while l >= 0 and s[l] != " ":
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


def test_lengthOfLastWord_case_2():
    # arrange
    s: str = "   fly me   to   the moon  "
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.lengthOfLastWord(s)

    # assert
    assert expected == actual


def test_lengthOfLastWord_case_3():
    # arrange
    s: str = "luffy is still joyboy"
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.lengthOfLastWord(s)

    # assert
    assert expected == actual
