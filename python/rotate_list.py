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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy: ListNode = ListNode()
        dummy.next = head
        curr: Optional[ListNode] = head
        length: int = 0
        while curr is not None:
            curr = curr.next
            length += 1

        back_count: int = k % length
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        for _ in range(back_count):
            fast = fast.next
        while fast is not None and fast.next is not None and slow is not None:
            fast = fast.next
            slow = slow.next

        first_node: Optional[ListNode] = dummy.next
        fast.next = first_node
        dummy.next = slow.next
        slow.next = None

        return dummy.next


def test_rotateRight_case_1():
    """This is a test case"""
    # arrange
    head: list[int] = [1, 2, 3, 4, 5]
    k: int = 2
    expected: list[int] = [4, 5, 1, 2, 3]

    # act
    solution = Solution()
    actual = solution.rotateRight(convert_to_linked_list(head), k)

    # assert
    assert expected == convert_linked_list_to_list(actual)


def test_rotateRight_case_2():
    """This is a test case"""
    # arrange
    head: list[int] = [0, 1, 2]
    k: int = 4
    expected: list[int] = [2, 0, 1]

    # act
    solution = Solution()
    actual = solution.rotateRight(convert_to_linked_list(head), k)

    # assert
    assert expected == convert_linked_list_to_list(actual)


def test_rotateRight_case_3():
    """This is a test case"""
    # arrange
    head: list[int] = []
    k: int = 0
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.rotateRight(convert_to_linked_list(head), k)

    # assert
    assert expected == convert_linked_list_to_list(actual)
