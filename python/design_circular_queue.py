from typing import Optional


class Node:
    def __init__(
        self,
        value: int = 0,
        prev: Optional["Node"] = None,
        next_node: Optional["Node"] = None,
    ) -> "Node":
        self.val: int = value
        self.prev: Optional["Node"] = prev
        self.next: Optional["Node"] = next_node


class MyCircularQueue:

    def __init__(self, k: int):
        self._space: int = k
        self._left: Node = Node()
        self._right: Node = Node()
        self._left.next = self._right
        self._right.prev = self._left

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node: Node = Node(value)
        last_node: Optional[Node] = self._right.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self._right
        self._right.prev = new_node
        self._space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        first_node: Optional[Node] = self._left.next
        second_node: Optional[Node] = first_node.next
        self._left.next = second_node
        second_node.prev = self._left
        self._space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._right.prev.val

    def isEmpty(self) -> bool:
        return self._left.next == self._right

    def isFull(self) -> bool:
        return self._space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
def test_circular_queue_case_1():
    que = MyCircularQueue(3)
    actual_1 = que.enQueue(1)
    actual_2 = que.enQueue(2)
    actual_3 = que.enQueue(3)
    actual_4 = que.enQueue(4)
    actual_5 = que.Rear()
    actual_6 = que.isFull()
    actual_7 = que.deQueue()
    actual_8 = que.enQueue(4)
    actual_9 = que.Rear()

    assert actual_1 is True
    assert actual_2 is True
    assert actual_3 is True
    assert actual_4 is False
    assert actual_5 == 3
    assert actual_6 is True
    assert actual_7 is True
    assert actual_8 is True
    assert actual_9 == 4
