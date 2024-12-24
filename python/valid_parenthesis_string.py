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

    def checkValidString2(self, s: str) -> bool:
        """time complexity: O(n), space complexity: O(n)"""
        left_stack: list[int] = []
        star_stack: list[int] = []
        for i, c in enumerate(s):
            if c == "(":
                left_stack.append(i)
            elif c == "*":
                star_stack.append(i)
            else:
                if len(left_stack) == 0 and len(star_stack) == 0:
                    return False
                if len(left_stack) > 0:
                    left_stack.pop()
                else:
                    star_stack.pop()
        while len(left_stack) > 0 and len(star_stack) > 0:
            if left_stack.pop() > star_stack.pop():
                return False
        return len(left_stack) == 0


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
