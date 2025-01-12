class MinStack:

    def __init__(self):
        self._stack: list[int] = []
        self._min_stack: list[int] = []

    def push(self, val: int) -> None:
        """time complexity: O(1), space complexity: O(n)"""
        self._stack.append(val)
        if len(self._min_stack) > 0 and val > self._min_stack[-1]:
            self._min_stack.append(self._min_stack[-1])
        else:
            self._min_stack.append(val)

    def pop(self) -> None:
        """time complexity: O(1), space complexity: O(n)"""
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        """time complexity: O(1)"""
        return self._stack[-1]

    def getMin(self) -> int:
        """time complexity: O(1)"""
        return self._min_stack[-1]


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


def test_min_stack_case_3():
    # arrange
    obj = MinStack()
    expected1 = -3
    expected2 = -3

    # act
    obj.push(-2)
    obj.push(-2)
    obj.push(-3)
    obj.push(-3)
    # [-2, -2, -3, -3]
    actual1: int = obj.getMin()
    obj.pop()
    actual2: int = obj.getMin()

    # assert
    assert actual1 == expected1
    assert actual2 == expected2
