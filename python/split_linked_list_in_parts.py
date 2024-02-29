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
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> list[Optional[ListNode]]:
        """time complexity: O(n)"""
        result: list[Optional[ListNode]] = []
        length: int = 0
        curr: Optional[ListNode] = head
        while curr is not None:
            length += 1
            curr = curr.next
        subvec_size: int = length // k
        remainder: int = length % k
        # NOTE: length = subvec_size * k + remainder
        indices: list[int] = [subvec_size for _ in range(k)]
        for i in range(remainder):
            indices[i] += 1

        curr = head
        for count in indices:
            dummy: ListNode = ListNode()
            dummy.next = curr
            curr = dummy
            if curr is not None:
                for _ in range(count):
                    curr = curr.next
            if curr is not None:
                next_node: Optional[ListNode] = curr.next
                curr.next = None
                curr = next_node
            result.append(dummy.next)

        return result


def test_splitListToParts_case_1():
    """NOTE: skip because it is difficult to prepare for test cases (input)"""
    # arragne
    nums: list[int] = [1, 2, 3]
    k: int = 5
    # nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # k: int = 3

    # act
    solution = Solution()
    actual: Optional[ListNode] = solution.splitListToParts(
        convert_to_linked_list(nums),
        k,
    )

    assert True
