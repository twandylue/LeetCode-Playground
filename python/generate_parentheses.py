class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack: list[str] = []
        result: list[str] = []
        self.back_tracking(n, stack, result, 0, 0)

        return result

    def back_tracking(
        self, n: int, stack: list[str], result: list[str], openPara: int, closePara: int
    ):
        if openPara == closePara == n:
            result.append("".join(stack))
            return
        if openPara < n:
            stack.append("(")
            self.back_tracking(n, stack, result, openPara + 1, closePara)
            stack.pop()
        if closePara < openPara:
            stack.append(")")
            self.back_tracking(n, stack, result, openPara, closePara + 1)
            stack.pop()


def test_generateParentheses_case_1():
    # arrange
    n: int = 3
    expected: list[str] = ["((()))", "(()())", "(())()", "()(())", "()()()"]

    # act
    solution = Solution()
    actual = solution.generateParenthesis(n)

    # assert
    assert actual == expected


def test_generateParentheses_case_2():
    # arrange
    n: int = 1
    expected: list[str] = ["()"]

    # act
    solution = Solution()
    actual = solution.generateParenthesis(n)

    # assert
    assert actual == expected
