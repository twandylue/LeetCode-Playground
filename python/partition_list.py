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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """time complexity: O(n)"""
        before_head: ListNode = ListNode(0)
        after_head: ListNode = ListNode(0)
        before: ListNode = before_head
        after: ListNode = after_head
        while head is not None:
            if head.val < x:
                before.next = head
                before = head
            else:
                after.next = head
                after = head
            head = head.next
        after.next = None
        before.next = after_head.next
        return before_head.next


def test_partition_case_1():
    """This is a test case"""
    # arrange
    head: list[int] = [1, 4, 3, 2, 5, 2]
    x: int = 3
    expected: list[int] = [1, 2, 2, 4, 3, 5]

    # act
    solution = Solution()
    actual = solution.partition(convert_to_linked_list(head), x)

    # assert
    assert expected == convert_linked_list_to_list(actual)


def test_partition_case_2():
    """This is a test case"""
    # arrange
    head: list[int] = [2, 1]
    x: int = 2
    expected: list[int] = [1, 2]

    # act
    solution = Solution()
    actual = solution.partition(convert_to_linked_list(head), x)

    # assert
    assert expected == convert_linked_list_to_list(actual)
