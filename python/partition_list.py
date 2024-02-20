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
        left: Optional[ListNode] = ListNode()
        left_curr: Optional[ListNode] = left
        right: Optional[ListNode] = ListNode()
        right_curr: Optional[ListNode] = right
        curr: Optional[ListNode] = head
        while left_curr is not None and right_curr is not None and curr is not None:
            if curr.val < x:
                left_curr.next = curr
                left_curr = left_curr.next
            else:
                right_curr.next = curr
                right_curr = right_curr.next
            curr = curr.next

        left_curr.next = right.next
        right_curr.next = None

        return left.next


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
