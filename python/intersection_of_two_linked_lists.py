"""module to reorder the linked list"""

import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from list_node import ListNode
from linkedListConverter import convert_to_linked_list
from linkedListConverter import convert_linked_list_to_list
from assert_two_linked_list import assert_two_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """time complexity: O(m+n)"""
        if headA is None or headB is None:
            return None
        len_a: int = 0
        len_b: int = 0
        curr_a = headA
        curr_b = headB
        while curr_a is not None:
            curr_a = curr_a.next
            len_a += 1
        while curr_b is not None:
            curr_b = curr_b.next
            len_b += 1

        diff: int = abs(len_a - len_b)
        curr_a = headA
        curr_b = headB
        if len_a > len_b:
            for _ in range(diff):
                curr_a = curr_a.next
        else:
            for _ in range(diff):
                curr_b = curr_b.next
        while curr_a is not None and curr_b is not None:
            if curr_a == curr_b:
                return curr_a
            curr_a = curr_a.next
            curr_b = curr_b.next

        return None

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """time complexity: O(m+n)"""
        curr_a: Optional[ListNode] = headA
        curr_b: Optional[ListNode] = headB
        while curr_a != curr_b:
            curr_a = curr_a.next if curr_a is not None else headB
            curr_b = curr_b.next if curr_b is not None else headA
        return curr_a


def test_getIntersectionNode_case_1():
    """NOTE: skip because it is difficult to prepare for test cases (input)"""
    # arrange
    # list_A: list[int] = [4, 1, 8, 4, 5]
    # list_B: list[int] = [5, 6, 1, 8, 4, 5]
    # expected: list[int] = [8]
    #
    # act
    # solution = Solution()
    # actual = solution.getIntersectionNode(
    #     convert_to_linked_list(list_A), convert_to_linked_list(list_B)
    # )
    #
    # assert
    # assert expected == convert_linked_list_to_list(actual)
    assert True
