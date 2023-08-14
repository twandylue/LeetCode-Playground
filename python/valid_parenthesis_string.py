class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin: int = 0
        leftMax: int = 0
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0


def test_checkValidString_case_1():
    # arrange
    s = "()"
    expected = True

    # act
    actual = Solution().checkValidString(s)

    # assert
    assert actual == expected


def test_checkValidString_case_2():
    # arrange
    s = "(*)"
    expected = True

    # act
    actual = Solution().checkValidString(s)

    # assert
    assert actual == expected


def test_checkValidString_case_3():
    # arrange
    s = "(*))"
    expected = True

    # act
    actual = Solution().checkValidString(s)

    # assert
    assert actual == expected
