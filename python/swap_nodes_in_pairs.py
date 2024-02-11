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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """time complexity: O(n)"""
        dummy: ListNode = ListNode()
        dummy.next = head
        prev: Optional[ListNode] = dummy
        curr: Optional[ListNode] = head
        while curr is not None and curr.next is not None:
            next_pairs: Optional[ListNode] = curr.next.next
            next_node: Optional[ListNode] = curr.next
            prev.next = next_node
            next_node.next = curr
            curr.next = next_pairs

            prev = curr
            curr = next_pairs

        return dummy.next


def test_swapPairs_case_1():
    # arrange
    head: list[int] = [1, 2, 3, 4]
    expected: list[int] = [2, 1, 4, 3]

    # act
    solution = Solution()
    actual = solution.swapPairs(convert_to_linked_list(head))

    # assert
    assert expected == convert_linked_list_to_list(actual)


def test_swapPairs_case_2():
    """This is a test case for reorderList"""
    # arrange
    head: list[int] = [1]
    expected: list[int] = [1]

    # act
    solution = Solution()
    actual = solution.swapPairs(convert_to_linked_list(head))

    # assert
    assert expected == convert_linked_list_to_list(actual)


def test_swapPairs_case_3():
    """This is a test case for reorderList"""
    # arrange
    head: list[int] = []
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.swapPairs(convert_to_linked_list(head))

    # assert
    assert expected == convert_linked_list_to_list(actual)
