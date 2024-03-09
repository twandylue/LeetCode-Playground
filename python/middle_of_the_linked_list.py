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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast: Optional[ListNode] = head
        slow: Optional[ListNode] = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow


def test_middleNode_case_1():
    # arrange
    head: list[int] = [1, 2, 3, 4, 5]
    expected: list[int] = [3, 4, 5]

    # act
    solution = Solution()
    actual = solution.middleNode(convert_to_linked_list(head))

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True


def test_middleNode_case_2():
    # arrange
    head: list[int] = [1, 2, 3, 4, 5, 6]
    expected: list[int] = [4, 5, 6]

    # act
    solution = Solution()
    actual = solution.middleNode(convert_to_linked_list(head))

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True
