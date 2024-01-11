class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack: list[str] = list()
        for i in range(len(operations)):
            if operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                num: int = int(stack[-1])
                stack.append(str(num * 2))
            elif operations[i] == "+":
                num1: int = int(stack.pop())
                num2: int = int(stack.pop())
                total: int = num1 + num2
                stack.append(str(num2))
                stack.append(str(num1))
                stack.append(str(total))
            else:
                stack.append(operations[i])

        result: int = 0
        for i in range(len(stack)):
            result += int(stack[i])

        return result


def test_calPoints_case_1():
    # arrange
    ops: list[int] = ["5", "2", "C", "D", "+"]
    expected: int = 30

    # act
    solution = Solution()
    actual = solution.calPoints(ops)

    # assert
    assert expected == actual


def test_calPoints_case_2():
    # arrange
    ops: list[int] = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    expected: int = 27

    # act
    solution = Solution()
    actual = solution.calPoints(ops)

    # assert
    assert expected == actual


def test_calPoints_case_3():
    # arrange
    ops: list[int] = ["1", "C"]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.calPoints(ops)

    # assert
    assert expected == actual
