import sys

sys.path.append("../models")

from typing import Optional
from list_node import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def assert_two_linked_list(
    head1: Optional[ListNode], head2: Optional[ListNode]
) -> bool:
    while head1 != None and head2 != None:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    if head1 != None or head2 != None:
        return False

    return True
