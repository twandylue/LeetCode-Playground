class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s: list[str] = []
        for c in s:
            if c == "#":
                if len(stack_s) > 0:
                    stack_s.pop()
            else:
                stack_s.append(c)
        stack_t: list[str] = []
        for c in t:
            if c == "#":
                if len(stack_t) > 0:
                    stack_t.pop()
            else:
                stack_t.append(c)
        return "".join(stack_s) == "".join(stack_t)


def test_backspaceCompare_case_1():
    # arrange
    s: str = "y#fo##f"
    t: str = "y#f#o##f"
    expected: int = True

    # act
    actual = Solution().backspaceCompare(s, t)

    # assert
    assert expected == actual


def test_backspaceCompare_case_2():
    # arrange
    s: str = "a#c"
    t: str = "b"
    expected: int = False

    # act
    actual = Solution().backspaceCompare(s, t)

    # assert
    assert expected == actual


def test_backspaceCompare_case_3():
    # arrange
    s: str = "ab##"
    t: str = "c#d#"
    expected: int = True

    # act
    actual = Solution().backspaceCompare(s, t)

    # assert
    assert expected == actual
