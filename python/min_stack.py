class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

        return None

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def test_min_stack_case_1():
    # arrange
    obj = MinStack()
    expected1 = -3
    expected2 = 0
    expected3 = -2

    # act
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    actual1: int = obj.getMin()
    obj.pop()
    actual2: int = obj.top()
    actual3: int = obj.getMin()

    # assert
    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3


def test_min_stack_case_2():
    # arrange
    obj = MinStack()
    expected1 = -2
    expected2 = -1
    expected3 = -2

    # act
    obj.push(-2)
    obj.push(0)
    obj.push(-1)
    actual1: int = obj.getMin()
    actual2: int = obj.top()
    obj.pop()
    actual3: int = obj.getMin()

    # assert
    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3
