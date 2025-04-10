from typing import Optional
import sys

sys.path.append("./models")
from list_node import ListNode

sys.path.append("./utils")
from linkedListConverter import convert_to_linked_list
from linkedListConverter import convert_linked_list_to_list


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeTwoLists2(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy: Optional[ListNode] = ListNode()
        curr: Optional[ListNode] = dummy
        curr1: Optional[ListNode] = list1
        curr2: Optiaonl[ListNode] = list2
        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        if curr1 is not None:
            curr.next = curr1
        if curr2 is not None:
            curr.next = curr2
        return dummy.next


def test_addTwoNumbers_case_1():
    # arrange
    list1: list[int] = [1, 2, 4]
    list2: list[int] = [1, 3, 4]
    expected: list[int] = [1, 1, 2, 3, 4, 4]

    # act
    solution = Solution()
    actual = solution.mergeTwoLists(
        convert_to_linked_list(list1), convert_to_linked_list(list2)
    )

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_addTwoNumbers_case_2():
    # arrange
    list1: list[int] = []
    list2: list[int] = []
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.mergeTwoLists(
        convert_to_linked_list(list1), convert_to_linked_list(list2)
    )

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_addTwoNumbers_case_3():
    # arrange
    list1: list[int] = []
    list2: list[int] = [0]
    expected: list[int] = [0]

    # act
    solution = Solution()
    actual = solution.mergeTwoLists(
        convert_to_linked_list(list1), convert_to_linked_list(list2)
    )

    # assert
    assert convert_linked_list_to_list(actual) == expected
