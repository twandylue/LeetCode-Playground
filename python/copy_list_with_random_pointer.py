from typing import Optional
import sys

sys.path.append("./models")

sys.path.append("./utils")
from linkedListConverter import convert_to_linked_list
from linkedListConverter import convert_linked_list_to_list


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
        dic: dict[Node, Node] = dict()
        pointer: Optional[Node] = head
        newHead: Node = Node(0)
        newPointer: Optional[Node] = newHead
        while pointer is not None:
            node: Node = Node(pointer.val, pointer.next, None)
            dic[pointer] = node
            pointer = pointer.next

            newPointer.next = node
            newPointer = newPointer.next

        pointer = head
        while pointer is not None:
            if pointer.random is not None:
                dic[pointer].random = dic[pointer.random]
            pointer = pointer.next

        return newHead.next
