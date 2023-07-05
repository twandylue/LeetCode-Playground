from typing import Optional
import sys

sys.path.append("./models")
from list_node import ListNode

sys.path.append("./utils")
from linkedListConverter import convert_to_linked_list
from linkedListConverter import convert_linked_list_to_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head != None:
            dummy = ListNode(0, head)
            fast = dummy
            slow = dummy
            while fast.next != None:
                if n <= 0:
                    slow = slow.next
                fast = fast.next
                n -= 1
            slow.next = slow.next.next

            return dummy.next

        return None


def test_removeNthFromEnd_case_1():
    # arrange
    head: list[int] = [1, 2, 3, 4, 5]
    n: int = 2
    expected: list[int] = [1, 2, 3, 5]

    # act
    solution = Solution()
    actual = solution.removeNthFromEnd(convert_to_linked_list(head), n)

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_removeNthFromEnd_case_2():
    # arrange
    head: list[int] = [1]
    n: int = 1
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.removeNthFromEnd(convert_to_linked_list(head), n)

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_removeNthFromEnd_case_3():
    # arrange
    head: list[int] = [1, 2]
    n: int = 1
    expected: list[int] = [1]

    # act
    solution = Solution()
    actual = solution.removeNthFromEnd(convert_to_linked_list(head), n)

    # assert
    assert convert_linked_list_to_list(actual) == expected
