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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """time complexity: O(nlogn)"""
        if head is None or head.next is None:
            return head
        fast: Optional[ListNode] = head.next
        slow: Optional[ListNode] = head
        while fast is not None and fast.next is not None and slow is not None:
            fast = fast.next.next
            slow = slow.next

        mid: Optional[ListNode] = slow.next
        slow.next = None
        left: Optional[ListNode] = self.sortList(head)
        right: Optional[ListNode] = self.sortList(mid)

        return self.merge(left, right)

    def merge(
        self, left: Optional[ListNode], right: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Dummy head is important"""
        dummy: ListNode = ListNode()
        curr: Optional[ListNode] = dummy
        while left is not None and right is not None and curr is not None:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left is None and curr is not None:
            curr.next = right
        if right is None and curr is not None:
            curr.next = left

        return dummy.next


def test_sortList_case_1():
    """This is a test case"""
    # arrange
    head: list[int] = [4, 2, 1, 3]
    expected: list[int] = [1, 2, 3, 4]

    # act
    solution = Solution()
    actual = solution.sortList(convert_to_linked_list(head))

    # assert
    assert expected == convert_linked_list_to_list(actual)


def test_sortList_case_2():
    """This is a test case"""
    # arrange
    head: list[int] = [-1, 5, 3, 4, 0]
    expected: list[int] = [-1, 0, 3, 4, 5]

    # act
    solution = Solution()
    actual = solution.sortList(convert_to_linked_list(head))

    # assert
    assert expected == convert_linked_list_to_list(actual)


def test_sortList_case_3():
    """This is a test case"""
    # arrange
    head: list[int] = []
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.sortList(convert_to_linked_list(head))

    # assert
    assert expected == convert_linked_list_to_list(actual)
