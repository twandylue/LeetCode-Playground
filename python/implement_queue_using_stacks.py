class MyQueue:

    def __init__(self):
        self.stack_1: list[int] = []
        self.stack_2: list[int] = []

    def push(self, x: int) -> None:
        """time complexity: O(1)"""
        self.stack_1.append(x)

    def pop(self) -> int:
        """time complexity: O(n)"""
        if len(self.stack_2) == 0:
            while len(self.stack_1) > 0:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

    def peek(self) -> int:
        """time complexity: O(n)"""
        if len(self.stack_2) == 0:
            while len(self.stack_1) > 0:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2[-1]

    def empty(self) -> bool:
        """time complexity: O(1)"""
        return max(len(self.stack_2), len(self.stack_1)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
def test_MyQueue_case_1():
    obj: MyQueue = MyQueue()
    obj.push(1)
    obj.push(2)
    param_1: int = obj.peek()
    assert 1 == param_1
    param_2: int = obj.pop()
    assert 1 == param_2
    assert not obj.empty()
