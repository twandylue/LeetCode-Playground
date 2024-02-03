from typing import Optional
import sys

sys.path.append("./models")
from list_node import ListNode

sys.path.append("./utils")
from linkedListConverter import convert_to_linked_list
from linkedListConverter import convert_linked_list_to_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # NOTE: time complexity: O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr: Optional[ListNode] = head
        prev: Optional[ListNode] = None
        while curr != None:
            next: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


def test_reverseList_case_1():
    # arrange
    head: list[int] = [1, 2, 3, 4, 5]
    expected: list[int] = [5, 4, 3, 2, 1]

    # act
    solution = Solution()
    actual = solution.reverseList(convert_to_linked_list(head))

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_reverseList_case_2():
    # arrange
    head: list[int] = [1, 2]
    expected: list[int] = [2, 1]

    # act
    solution = Solution()
    actual = solution.reverseList(convert_to_linked_list(head))

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_reverseList_case_3():
    # arrange
    head: list[int] = []
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.reverseList(convert_to_linked_list(head))

    # assert
    assert convert_linked_list_to_list(actual) == expected
