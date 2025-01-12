class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """time complexity: O(n), space complexity: O(n)"""
        if len(tokens) < 3:
            return int(tokens[0])

        stack: list[int] = []
        for t in tokens:
            if t == "+":
                arg1 = stack.pop()
                arg2 = stack.pop()
                stack.append(arg2 + arg1)
            elif t == "-":
                arg1 = stack.pop()
                arg2 = stack.pop()
                stack.append(arg2 - arg1)
            elif t == "*":
                arg1 = stack.pop()
                arg2 = stack.pop()
                stack.append(arg2 * arg1)
            elif t == "/":
                arg1 = stack.pop()
                arg2 = stack.pop()
                stack.append(int(arg2 / arg1))
            else:
                stack.append(int(t))

        return stack[-1]


def test_evalRPN_case_1():
    # arrange
    tokens: list[str] = ["2", "1", "+", "3", "*"]
    expected: int = 9

    # act
    solution = Solution()
    actual = solution.evalRPN(tokens)

    # assert
    assert actual == expected


def test_evalRPN_case_2():
    # arrange
    tokens: list[str] = ["4", "13", "5", "/", "+"]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.evalRPN(tokens)

    # assert
    assert actual == expected


def test_evalRPN_case_3():
    # arrange
    tokens: list[str] = [
        "10",
        "6",
        "9",
        "3",
        "+",
        "-11",
        "*",
        "/",
        "*",
        "17",
        "+",
        "5",
        "+",
    ]
    expected: int = 22

    # act
    solution = Solution()
    actual = solution.evalRPN(tokens)

    # assert
    assert actual == expected
