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
        self._size: int = 0
        self._capacity: int = k
        self._head: Node = Node()
        self._tail: Node = Node()
        self._head.next = self._tail
        self._tail.prev = self._head

    def enQueue(self, value: int) -> bool:
        if self._size >= self._capacity:
            return False
        new_node: Node = Node(value)
        last_node: Optional[Node] = self._tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self._tail
        self._tail.prev = new_node
        self._size += 1
        return True

    def deQueue(self) -> bool:
        if self._size == 0 or self._head.next == self._tail:
            return False
        first_node: Optional[Node] = self._head.next
        second_node: Optional[Node] = first_node.next
        self._head.next = second_node
        second_node.prev = self._head
        self._size -= 1
        return True

    def Front(self) -> int:
        if self._size == 0 or self._head.next == self._tail:
            return -1
        first_node: Optional[Node] = self._head.next
        return first_node.val

    def Rear(self) -> int:
        if self._size == 0 or self._tail.prev == self._head:
            return -1
        last_node: Optional[Node] = self._tail.prev
        return last_node.val

    def isEmpty(self) -> bool:
        if self._size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self._size == self._capacity:
            return True
        return False


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

    assert actual_1 == True
    assert actual_2 == True
    assert actual_3 == True
    assert actual_4 == False
    assert actual_5 == 3
    assert actual_6 == True
    assert actual_7 == True
    assert actual_8 == True
    assert actual_9 == 4
