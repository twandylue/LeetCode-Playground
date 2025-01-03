from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        """time complexity: O(n)"""
        return self.cal(deque(s.replace(" ", "")))

    def cal(self, queue: deque[str]) -> int:
        stack: list[int] = []
        curr: int = 0
        last_operator: str = "+"
        while len(queue) > 0:
            c: str = queue.popleft()
            if c.isdigit():
                curr = curr * 10 + int(c)
            if c == "(":
                curr = self.cal(queue)
            if c in "+-*/)" or len(queue) == 0:
                if last_operator == "+":
                    stack.append(curr)
                elif last_operator == "-":
                    stack.append(-1 * curr)
                elif last_operator == "*":
                    stack.append(stack.pop() * curr)
                else:
                    stack.append(int(stack.pop() / curr))
                last_operator = c
                curr = 0
            if c == ")":
                break
        return sum(stack)


def test_calculate_case_1():
    # arrange
    s: str = " 1+1 "
    expected: int = 2

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


def test_calculate_case_4():
    # arrange
    s: str = "(2+6* 3+5- (3*14/7+2)*5)+3"
    expected: int = -12

    # act
    actual = Solution().calculate(s)

    # assert
    assert expected == actual


def test_calculate_case_5():
    # arrange
    s: str = "2*(5+5*2)/3+(6/2+8)"
    expected: int = 21

    # act
    actual = Solution().calculate(s)

    # assert
    assert expected == actual
