import sys

from typing import Optional

sys.path.append("./models")
from list_node import ListNode

sys.path.append("./utils")
from linkedListConverter import convert_to_linked_list
from assert_two_linked_list import assert_two_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        """time complexity: O(n)"""
        dummy: ListNode = ListNode()
        dummy.next = list1
        first_pointer: ListNode = list1
        for _ in range(a - 1):
            first_pointer = first_pointer.next
        second_pointer: ListNode = list1
        for _ in range(b):
            second_pointer = second_pointer.next
        first_pointer.next = list2
        third_pointer: ListNode = list2
        while third_pointer.next is not None:
            third_pointer = third_pointer.next
        third_pointer.next = second_pointer.next
        return dummy.next


def test_mergeInBetween_case_1():
    # arrange
    list1: Optional[ListNode] = convert_to_linked_list([10, 1, 13, 6, 9, 5])
    a: int = 3
    b: int = 4
    list2: Optional[ListNode] = convert_to_linked_list([1000000, 1000001, 1000002])
    expected: list[int] = [10, 1, 13, 1000000, 1000001, 1000002, 5]

    # act
    solution = Solution()
    actual = solution.mergeInBetween(list1, a, b, list2)

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True


def test_mergeInBetween_case_2():
    # arrange
    list1: Optional[ListNode] = convert_to_linked_list([0, 1, 2, 3, 4, 5, 6])
    a: int = 2
    b: int = 5
    list2: Optional[ListNode] = convert_to_linked_list(
        [1000000, 1000001, 1000002, 1000003, 1000004]
    )
    expected: list[int] = [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]

    # act
    solution = Solution()
    actual = solution.mergeInBetween(list1, a, b, list2)

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True
