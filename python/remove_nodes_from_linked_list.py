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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """time complexity: O(n)"""
        stack: list[ListNode] = []
        curr: ListNode = head
        while curr is not None:
            while len(stack) > 0 and curr.val > stack[-1].val:
                stack.pop()
            if len(stack) > 0:
                stack[-1].next = curr
            stack.append(curr)
            curr = curr.next
        return stack[0]


def test_removeNodes_case_1():
    # arrange
    head: list[int] = [5, 2, 13, 3, 8]
    expected: list[int] = [13, 8]

    # act
    solution = Solution()
    actual = solution.removeNodes(convert_to_linked_list(head))

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual)


def test_removeNodes_case_2():
    # arrange
    head: list[int] = [1, 1, 1, 1]
    expected: list[int] = [1, 1, 1, 1]

    # act
    solution = Solution()
    actual = solution.removeNodes(convert_to_linked_list(head))

    # assert
    assert assert_two_linked_list(convert_to_linked_list(expected), actual)
