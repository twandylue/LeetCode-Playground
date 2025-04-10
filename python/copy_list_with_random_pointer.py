from typing import Optional


class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """time complexity: O(n), space complexity: O(n)"""
        if head is None:
            return None
        old_to_new: dict[Node, Node] = {}
        curr: Optional[Node] = head
        # First, copy all nodes
        while curr is not None:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        # Second, set up next and random
        while curr is not None:
            if curr not in old_to_new:
                continue
            if curr.next is not None:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random is not None:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head]
