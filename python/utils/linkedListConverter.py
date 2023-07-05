import sys

sys.path.append("../models")

from typing import Optional
from list_node import ListNode


def convert_to_linked_list(arr: list[int]) -> Optional[ListNode]:
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    curr = head

    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next

    return head


def convert_linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    arr = []

    while head:
        arr.append(head.val)
        head = head.next

    return arr
