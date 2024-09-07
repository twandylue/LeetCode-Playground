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
    def modifiedList(
        self, nums: list[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """time complexity: O(n + m) where n is the size of nums and m is the size of linked list"""
        dummy: Optional[ListNode] = ListNode()
        dummy.next = head
        prev = dummy
        nums_set: Set[int] = set(nums)
        while prev.next is not None:
            if prev.next.val in nums_set:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next


def test_modifiedList_case_1():
    # arrange
    nums: list[int] = [1]
    head: Optional[ListNode] = convert_to_linked_list([1, 2, 1, 2, 1, 2])
    expected: list[int] = [2, 2, 2]

    # act
    solution = Solution()
    actual: Optional[ListNode] = Solution().modifiedList(nums, head)

    # assert
    assert expected == convert_linked_list_to_list(actual)


def test_modifiedList_case_2():
    # arrange
    nums: list[int] = [1, 2, 3]
    head: Optional[ListNode] = convert_to_linked_list([1, 2, 3, 4, 5])
    expected: list[int] = [4, 5]

    # act
    solution = Solution()
    actual: Optional[ListNode] = Solution().modifiedList(nums, head)

    # assert
    assert expected == convert_linked_list_to_list(actual)


def test_modifiedList_case_3():
    # arrange
    nums: list[int] = [5]
    head: Optional[ListNode] = convert_to_linked_list([1, 2, 3, 4])
    expected: list[int] = [1, 2, 3, 4]

    # act
    solution = Solution()
    actual: Optional[ListNode] = Solution().modifiedList(nums, head)

    # assert
    assert expected == convert_linked_list_to_list(actual)
