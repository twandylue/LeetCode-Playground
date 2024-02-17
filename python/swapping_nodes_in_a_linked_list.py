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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # NOTE: time complexity: O(n)
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy: ListNode = ListNode()
        dummy.next = head
        left: Optional[ListNode] = head
        for _ in range(k - 1):
            left = left.next
        fast: Optional[ListNode] = left
        right: Optional[ListNode] = head
        while fast is not None and fast.next is not None and right is not None:
            fast = fast.next
            right = right.next

        left.val, right.val = right.val, left.val

        return dummy.next


def test_swapNodes_case_1():
    # arrange
    head: list[int] = [1, 2, 3, 4, 5]
    k: int = 2
    expected: list[int] = [1, 4, 3, 2, 5]

    # act
    solution = Solution()
    actual: Optional[ListNode] = solution.swapNodes(convert_to_linked_list(head), k)

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_swapNodes_case_2():
    # arrange
    head: list[int] = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
    k: int = 5
    expected: list[int] = [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]

    # act
    solution = Solution()
    actual: Optional[ListNode] = solution.swapNodes(convert_to_linked_list(head), k)

    # assert
    assert convert_linked_list_to_list(actual) == expected
