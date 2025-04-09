class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """time complexity: O(4^n / sqrt(n)), space complexity: O(n)"""
        stack: list[str] = []
        result: list[str] = []
        self.backtrack(0, 0, n, stack, result)
        return result

    def backtrack(
        self, open_n: int, close_n: int, n: int, stack: list[str], result: list[str]
    ) -> None:
        if open_n == n and close_n == n:
            result.append("".join(stack))
            return
        if open_n < n:
            stack.append("(")
            self.backtrack(open_n + 1, close_n, n, stack, result)
            stack.pop()
        if close_n < open_n:
            stack.append(")")
            self.backtrack(open_n, close_n + 1, n, stack, result)
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
