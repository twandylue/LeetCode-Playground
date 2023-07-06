from typing import Optional
import sys

sys.path.append("./models")
from list_node import ListNode

sys.path.append("./utils")
from linkedListConverter import convert_to_linked_list
from linkedListConverter import convert_linked_list_to_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d: dict[ListNode, int] = dict()
        node = head
        while node != None:
            if node.next in d:
                return True
            d[node] = 1
            node = node.next

        return False


def test_hasCycle_case_1():
    # arrange
    head: list[int] = [3, 2, 0, -4]
    pos: int = 1
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.hasCycle(prepare_linked_list(convert_to_linked_list(head), pos))

    # assert
    assert actual == expected


def test_hasCycle_case_2():
    # arrange
    head: list[int] = [1, 2]
    pos: int = 0
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.hasCycle(prepare_linked_list(convert_to_linked_list(head), pos))

    # assert
    assert actual == expected


def test_hasCycle_case_3():
    # arrange
    head: list[int] = [1]
    pos: int = -1
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.hasCycle(prepare_linked_list(convert_to_linked_list(head), pos))

    # assert
    assert actual == expected


def prepare_linked_list(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
    if pos == -1:
        return head

    node: Optional[ListNode] = head
    for i in range(pos):
        node = node.next

    tail: Optional[ListNode] = node
    while tail.next != None:
        tail = tail.next

    tail.next = node

    return head
