from typing import Optional
import sys

sys.path.append("./models")
from list_node import ListNode

sys.path.append("./utils")
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy: Optional[ListNode] = ListNode()
        dummy.next = head
        curr: Optional[ListNode] = head
        prev: Optional[ListNode] = dummy

        while curr != None:
            if curr.val == val:
                while curr != None and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next


def test_removeElements_case_1():
    # arrange
    head: list[int] = [1, 2, 6, 3, 4, 5, 6]
    val: int = 6
    expected: list[int] = [1, 2, 3, 4, 5]

    # act
    solution = Solution()
    actual = solution.removeElements(convert_to_linked_list(head), val)

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True


def test_removeElements_case_2():
    # arrange
    head: list[int] = []
    val: int = 1
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.removeElements(convert_to_linked_list(head), val)

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True


def test_removeElements_case_3():
    # arrange
    head: list[int] = [7, 7, 7, 7]
    val: int = 7
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.removeElements(convert_to_linked_list(head), val)

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual) == True
