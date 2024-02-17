"""for Optional"""

from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        prev: Optional["Node"] = None,
        next_node: Optional["Node"] = None,
    ):
        self.val: int = val
        self.next: Optional["Node"] = next_node
        self.prev: Optional["Node"] = prev


class MyLinkedList:
    """MyLinkedList Class"""

    def __init__(self):
        self.head: Node = Node()
        self.tail: Node = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """time complexity: O(n)"""
        curr: Node = self.head.next
        idx: int = 0
        while idx < index and curr is not None:
            curr = curr.next
            idx += 1
        if idx == index and curr is not None and curr != self.tail:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        """time complexity: O(1)"""
        new_node: Node = Node(val)
        first_node: Optional[Node] = self.head.next
        new_node.next = first_node
        first_node.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:
        """time complexity: O(1)"""
        new_node: Node = Node(val)
        last_node: Optional[Node] = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        self.tail.prev = new_node
        new_node.next = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        """time complexity: O(n)"""
        curr: Node = self.head.next
        idx: int = 0
        new_node: Node = Node(val)
        while idx < index and curr is not None:
            idx += 1
            curr = curr.next
        if idx == index and curr is not None:
            prev_node: Optional[Node] = curr.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = curr
            curr.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        """time complexity: O(n)"""
        curr: Optional[Node] = self.head.next
        idx: int = 0
        while curr is not None and idx < index:
            curr = curr.next
            idx += 1
        if idx == index and curr is not None and curr != self.tail:
            next_node: Optional[Node] = curr.next
            prev_node: Optional[Node] = curr.prev
            prev_node.next = next_node
            next_node.prev = prev_node


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
def test_my_linked_list_case_1():
    """test case"""
    my_linked_list: MyLinkedList = MyLinkedList()
    my_linked_list.addAtHead(1)
    my_linked_list.addAtTail(3)
    my_linked_list.addAtIndex(1, 2)
    # linked list becomes 1->2->3
    actual1: int = my_linked_list.get(1)
    # return 2
    my_linked_list.deleteAtIndex(1)
    # now the linked list is 1->3
    actual2: int = my_linked_list.get(1)
    # return 3

    assert actual2 == 3
    assert actual1 == 2


def test_my_linked_list_case_2():
    """test case"""
    my_linked_list: MyLinkedList = MyLinkedList()
    my_linked_list.addAtHead(1)
    my_linked_list.deleteAtIndex(0)
