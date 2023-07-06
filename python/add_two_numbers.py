from typing import Optional
import sys

sys.path.append("./models")
from list_node import ListNode

sys.path.append("./utils")
from linkedListConverter import convert_to_linked_list
from linkedListConverter import convert_linked_list_to_list


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 == None or l2 == None:
            return None

        head: ListNode = ListNode()
        dummy_head: ListNode = head
        carry: int = 0

        while l1 != None or l2 != None or carry > 0:
            sumNum: int = 0
            if l1 != None:
                sumNum += l1.val
                l1 = l1.next
            if l2 != None:
                sumNum += l2.val
                l2 = l2.next
            sumNum += carry
            carry = sumNum // 10
            head.next = ListNode(sumNum % 10)
            head = head.next

        return dummy_head.next


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
    assert convert_linked_list_to_list(actual) == expected
