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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast: Optional[ListNode] = head
        slow: Optional[ListNode] = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        curr: Optional[ListNode] = slow
        prev: Optional[ListNode] = None
        while curr != None:
            next: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = next

        left: Optional[ListNode] = head
        right: Optional[ListNode] = prev
        while right != None and left != None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


def test_isPalindrome_case_1():
    # arrange
    head: list[int] = [1, 2, 2, 1]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isPalindrome(convert_to_linked_list(head))

    # assert
    assert expected == actual


def test_isPalindrome_case_2():
    # arrange
    head: list[int] = [1, 2]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isPalindrome(convert_to_linked_list(head))

    # assert
    assert expected == actual
