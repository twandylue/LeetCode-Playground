import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from list_node import ListNode
from linkedListConverter import convert_to_linked_list
from linkedListConverter import convert_linked_list_to_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """time complexity: O(n), space complexity: O(1)"""
        dummy: ListNode = ListNode()
        dummy.next = head
        slow: Optional[ListNode] = dummy
        fast: Optional[ListNode] = head
        while fast is not None and fast.next is not None and slow is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        """time complexity: O(n), space complexity: O(n)"""
        node_map: dict[ListNode, int] = {}
        curr: Optional[ListNode] = head
        while curr is not None:
            if curr in node_map:
                return True
            node_map[curr] = 1
            curr = curr.next

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


def test_hasCycle_case_4():
    # arrange
    head: list[int] = [1, 2]
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
