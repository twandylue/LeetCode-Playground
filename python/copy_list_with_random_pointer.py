from typing import Optional


class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


# NOTE: time complexity: O(n), space complexity: O(n)
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        node_map: dict[Optional[Node], Optional[Node]] = {}
        curr: Optional[Node] = head
        new_head: Node = Node(0)
        new_curr: Optional[Node] = new_head
        while curr is not None and new_curr is not None:
            new_node: Node = Node(curr.val)
            new_curr.next = new_node
            new_curr = new_node
            node_map[curr] = new_node
            curr = curr.next

        pointer: Optional[Node] = head
        while pointer is not None:
            if pointer.random is not None:
                node_map[pointer].random = node_map[pointer.random]
            pointer = pointer.next

        return new_head.next
