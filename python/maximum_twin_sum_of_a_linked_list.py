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
    # NOTE: time complexity: O(n)
    def pairSum(self, head: Optional[ListNode]) -> int:
        result: int = 0
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head.next
        while fast is not None and fast.next is not None and slow is not None:
            slow = slow.next
            fast = fast.next.next

        curr: Optional[ListNode] = slow.next
        slow.next = None
        prev: Optional[ListNode] = None
        while curr is not None:
            next_node: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first: Optional[ListNode] = head
        second: Optional[ListNode] = prev
        while first is not None and second is not None:
            result = max(result, first.val + second.val)
            first = first.next
            second = second.next

        return result


def test_pairSum_case_1():
    """This is a test case for reorderList"""
    # arrange
    head: list[int] = [5, 4, 2, 1]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.pairSum(convert_to_linked_list(head))

    # assert
    assert expected == actual


def test_pairSum_case_2():
    """This is a test case for reorderList"""
    # arrange
    head: list[int] = [4, 2, 2, 3]
    expected: int = 7

    # act
    solution = Solution()
    actual = solution.pairSum(convert_to_linked_list(head))

    # assert
    assert expected == actual
