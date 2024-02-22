"""module to reorder the linked list"""

import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from list_node import ListNode
from linkedListConverter import convert_to_linked_list
from assert_two_linked_list import assert_two_linked_list
from linkedListConverter import convert_linked_list_to_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """time complexity: O(n)"""
        dummy: ListNode = ListNode()
        dummy.next = head
        prev_left: Optional[ListNode] = dummy
        curr: Optional[ListNode] = head
        for _ in range(left - 1):
            curr = curr.next
            prev_left = prev_left.next

        prev: Optional[ListNode] = None
        p_left: Optional[ListNode] = curr
        for _ in range(right - left + 1):
            next_node: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        prev_left.next = prev
        p_left.next = curr

        return dummy.next


def test_reverseBetween_case_1():
    """This is a test case"""
    # arrange
    head: list[int] = [1, 2, 3, 4, 5]
    left: int = 2
    right: int = 4
    expected: list[int] = [1, 4, 3, 2, 5]

    # act
    solution = Solution()
    actual = solution.reverseBetween(convert_to_linked_list(head), left, right)

    # assert
    assert expected == convert_linked_list_to_list(actual)


def test_reverseBetween_case_2():
    """This is a test case"""
    # arrange
    head: list[int] = [1, 2, 3, 4]
    left: int = 1
    right: int = 4
    expected: list[int] = [4, 3, 2, 1]

    # act
    solution = Solution()
    actual = solution.reverseBetween(convert_to_linked_list(head), left, right)

    # assert
    assert expected == convert_linked_list_to_list(actual)
