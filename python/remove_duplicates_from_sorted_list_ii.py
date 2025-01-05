"""Import necessary modules"""

import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from linkedListConverter import convert_to_linked_list
from assert_two_linked_list import assert_two_linked_list
from list_node import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """time complexity: O(n)"""
        dummy: ListNode = ListNode()
        dummy.next = head
        prev: ListNode = dummy
        curr: Optional[ListNode] = head
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                while (
                    curr is not None
                    and curr.next is not None
                    and curr.val == curr.next.val
                ):
                    curr.next = curr.next.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next


def test_deleteDuplicates_case_1():
    # arrange
    head: list[int] = [1, 2, 3, 3, 4, 4, 5]
    expected: list[int] = [1, 2, 5]

    # act
    actual = Solution().deleteDuplicates(convert_to_linked_list(head))

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True


def test_deleteDuplicates_case_2():
    # arrange
    head: list[int] = [1, 1, 1, 2, 3]
    expected: list[int] = [2, 3]

    # act
    actual = Solution().deleteDuplicates(convert_to_linked_list(head))

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True
