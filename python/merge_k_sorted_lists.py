from typing import Optional
import sys

sys.path.append("./models")
from list_node import ListNode

sys.path.append("./utils")
from linkedListConverter import convert_to_linked_list
from linkedListConverter import convert_linked_list_to_list


# NOTE: time complexity: nlogk, where k: number of lists and n: totle elements in lists
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists: list[ListNode] = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))

            lists = mergedLists

        return lists[0]

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def test_mergeKLists_case_1():
    # arrange
    lists: list[ListNode] = [
        convert_to_linked_list([1, 4, 5]),
        convert_to_linked_list([1, 3, 4]),
        convert_to_linked_list([2, 6]),
    ]
    expected: list[int] = [1, 1, 2, 3, 4, 4, 5, 6]

    # act
    solution = Solution()
    actual = solution.mergeKLists(lists)

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_mergeKLists_case_2():
    # arrange
    lists: list[ListNode] = []
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.mergeKLists(lists)

    # assert
    assert convert_linked_list_to_list(actual) == expected


def test_mergeKLists_case_3():
    # arrange
    lists: list[ListNode] = [convert_linked_list_to_list([])]
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.mergeKLists(lists)

    # assert
    assert convert_linked_list_to_list(actual) == expected
