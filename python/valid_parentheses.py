class Solution:
    def isValid(self, s: str) -> bool:
        """time complexity: O(n)"""
        stack: list[str] = []
        close_to_open: dict[str, str] = {")": "(", "]": "[", "}": "{"}
        for r in range(len(s)):
            if (
                s[r] in close_to_open
                and len(stack) > 0
                and stack[-1] == close_to_open[s[r]]
            ):
                stack.pop()
            else:
                stack.append(s[r])
        return len(stack) == 0


def test_isValid_case_1():
    # arrange
    s = "()"
    expected = True

    # act
    actual = Solution().isValid(s)

    # assert
    assert actual == expected


def test_isValid_case_2():
    # arrange
    s = "()[]{}"
    expected = True

    # act
    actual = Solution().isValid(s)

    # assert
    assert actual == expected


def test_isValid_case_3():
    # arrange
    s = "(]"
    expected = False

    # act
    actual = Solution().isValid(s)

    # assert
    assert actual == expected


def test_isValid_case_4():
    # arrange
    s = "([])"
    expected = True

    # act
    actual = Solution().isValid(s)

    # assert
    assert actual == expected
