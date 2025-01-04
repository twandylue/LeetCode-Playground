class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """time complexity: O(n)"""
        if len(s) == len(goal) and len(s) != 0 and len(goal) != 0:
            return self.is_substring(s + s, goal)
        return False

    def is_substring(self, s: str, t: str) -> bool:
        """time complexity: O(n)"""
        return s.find(t) != -1


def test_rotateString_case_1():
    # arrange
    s: str = "abcde"
    goal: str = "cdeab"
    expected: bool = True

    # act
    actual = Solution().rotateString(s, goal)

    # assert
    assert expected == actual


def test_rotateString_case_2():
    # arrange
    s: str = "abcde"
    goal: str = "abced"
    expected: bool = False

    # act
    actual = Solution().rotateString(s, goal)

    # assert
    assert expected == actual
