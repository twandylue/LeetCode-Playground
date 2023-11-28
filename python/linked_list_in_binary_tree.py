from collections import deque
from typing import Optional
import sys

sys.path.append("./models")
from list_node import ListNode
from binary_tree_node import TreeNode

sys.path.append("./utils")
from deserialize_to_binary_tree import DeserializeFromList
from linkedListConverter import convert_to_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        queue: deque[tuple[TreeNode, str]] = deque()
        queue.append((root, str(root.val)))
        paths: list[str] = list()

        while len(queue) > 0:
            node, path = queue.popleft()
            if node.left == None and node.right == None:
                paths.append(path)
                continue
            if node.left != None:
                queue.append((node.left, path + "->" + str(node.left.val)))
            if node.right != None:
                queue.append((node.right, path + "->" + str(node.right.val)))

        subpath: str = self.subpath_helper(head)

        for p in paths:
            if subpath in p:
                return True

        return False

    def subpath_helper(self, root: Optional[ListNode]) -> str:
        if root == None:
            return ""
        path: str = str(root.val)
        if root.next:
            path += "->" + self.subpath_helper(root.next)

        return path


def test_isSubPath_case_1():
    # arrange
    head: Optional[ListNode] = convert_to_linked_list([4, 2, 8])
    if head == None:
        raise Exception("failed")

    root: Optional[TreeNode] = DeserializeFromList(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    )
    if root == None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isSubPath(head, root)

    # assert
    assert actual == True


def test_isSubPath_case_2():
    # arrange
    head: Optional[ListNode] = convert_to_linked_list([1, 4, 2, 6])
    if head == None:
        raise Exception("failed")

    root: Optional[TreeNode] = DeserializeFromList(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    )
    if root == None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isSubPath(head, root)

    # assert
    assert actual == True


def test_isSubPath_case_3():
    # arrange
    head: Optional[ListNode] = convert_to_linked_list([1, 4, 2, 6, 8])
    if head == None:
        raise Exception("failed")

    root: Optional[TreeNode] = DeserializeFromList(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    )
    if root == None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isSubPath(head, root)

    # assert
    assert actual == False
