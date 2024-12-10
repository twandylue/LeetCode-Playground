"""module to reorder the linked list"""

import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from list_node import ListNode
from linkedListConverter import convert_to_linked_list
from assert_two_linked_list import assert_two_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """class to reorder the linked list"""

    # NOTE: time complexity: O(n)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Split the list
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second part of list
        curr: Optional[ListNode] = slow.next
        slow.next = None
        prev: Optional[ListNode] = None
        while curr is not None:
            next_node: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Merge two list
        list1: Optional[ListNode] = head
        list2: Optional[ListNode] = prev
        while list1 is not None and list2 is not None:
            list1_next: Optional[ListNode] = list1.next
            list2_next: Optional[ListNode] = list2.next
            list1.next = list2
            list2.next = list1_next
            list1 = list1_next
            list2 = list2_next


def test_reorderList_case_1():
    """This is a test case for reorderList"""
    # arrange
    head: list[int] = [1, 2, 3, 4]
    expected: list[int] = [1, 4, 2, 3]

    # act
    orig_list: Optional[ListNode] = convert_to_linked_list(head)
    solution = Solution()
    solution.reorderList(orig_list)

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), orig_list) is True


def test_reorderList_case_2():
    """This is a test case for reorderList"""
    # arrange
    head: list[int] = [1, 2, 3, 4, 5]
    expected: list[int] = [1, 5, 2, 4, 3]

    # act
    orig_list: Optional[ListNode] = convert_to_linked_list(head)
    solution = Solution()
    solution.reorderList(orig_list)

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), orig_list) is True
