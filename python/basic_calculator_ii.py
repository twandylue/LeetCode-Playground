class Solution:
    def calculate(self, s: str) -> int:
        """time complexity: O(n)"""
        curr: int = 0
        last_operator: str = "+"
        stack: list[int] = []
        for i, c in enumerate(s):
            if c.isdigit():
                curr = curr * 10 + int(c)
            if c in "+-*/" or i == len(s) - 1:
                if last_operator == "+":
                    stack.append(curr)
                elif last_operator == "-":
                    stack.append(-1 * curr)
                elif last_operator == "*" and len(stack) > 0:
                    stack.append(stack.pop() * curr)
                elif last_operator == "/" and len(stack) > 0:
                    stack.append(int(stack.pop() / curr))
                last_operator = c
                curr = 0
        return sum(stack)


def test_calculate_case_1():
    # arrange
    s: str = "3+2*2"
    expected: int = 7

    # act
    actual = Solution().calculate(s)

    # assert
    assert expected == actual


def test_calculate_case_2():
    # arrange
    s: str = " 3/2 "
    expected: int = 1

    # act
    actual = Solution().calculate(s)

    # assert
    assert expected == actual


def test_calculate_case_3():
    # arrange
    s: str = " 3+5 / 2 "
    expected: int = 5

    # act
    actual = Solution().calculate(s)

    # assert
    assert expected == actual
