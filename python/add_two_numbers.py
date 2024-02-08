from typing import Optional
import sys

sys.path.append("./models")
sys.path.append("./utils")

from list_node import ListNode
from linkedListConverter import convert_to_linked_list
from linkedListConverter import convert_linked_list_to_list


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        dummy: ListNode = ListNode()
        curr: Optional[ListNode] = dummy
        carry: int = 0
        while l1 is not None or l2 is not None or carry > 0:
            accu: int = 0
            if l1 is not None:
                accu += l1.val
                l1 = l1.next
            if l2 is not None:
                accu += l2.val
                l2 = l2.next
            accu += carry
            carry = accu // 10
            new_node: ListNode = ListNode(accu % 10)
            curr.next = new_node
            curr = curr.next

        return dummy.next


def test_addTwoNumbers_case_1():
    # arrange
    l1: list[int] = [2, 4, 3]
    l2: list[int] = [5, 6, 4]
    expected: list[int] = [7, 0, 8]

    # act
    solution = Solution()
    actual = solution.addTwoNumbers(
        convert_to_linked_list(l1), convert_to_linked_list(l2)
    )

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_addTwoNumbers_case_2():
    # arrange
    l1: list[int] = [0]
    l2: list[int] = [0]
    expected: list[int] = [0]

    # act
    solution = Solution()
    actual = solution.addTwoNumbers(
        convert_to_linked_list(l1), convert_to_linked_list(l2)
    )

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_addTwoNumbers_case_3():
    # arrange
    l1: list[int] = [9, 9, 9, 9, 9, 9, 9]
    l2: list[int] = [9, 9, 9, 9]
    expected: list[int] = [8, 9, 9, 9, 0, 0, 0, 1]

    # act
    solution = Solution()
    actual = solution.addTwoNumbers(
        convert_to_linked_list(l1), convert_to_linked_list(l2)
    )

    # assert
    assert expected == convert_linked_list_to_list(actual)
