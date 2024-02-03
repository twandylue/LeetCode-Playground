from typing import Optional
import sys

sys.path.append("./models")
from list_node import ListNode


# NOTE: time complexity: O(n)
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr: Optional[ListNode] = head
    prev: Optional[ListNode] = None
    while curr != None:
        next: Optional[ListNode] = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
