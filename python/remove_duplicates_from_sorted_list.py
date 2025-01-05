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
    # NOTE: time complexity: O(n)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy: ListNode = ListNode()
        dummy.next = head
        curr: Optional[ListNode] = head
        while curr is not None:
            while curr.next is not None and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next

        return dummy.next


def test_deleteDuplicates_case_1():
    # arrange
    head: list[int] = [1, 1, 2]
    expected: list[int] = [1, 2]

    # act
    solution = Solution()
    actual = solution.deleteDuplicates(convert_to_linked_list(head))

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True


def test_deleteDuplicates_case_2():
    # arrange
    head: list[int] = [1, 1, 2, 3, 3]
    expected: list[int] = [1, 2, 3]

    # act
    solution = Solution()
    actual = solution.deleteDuplicates(convert_to_linked_list(head))

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True
