import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from assert_two_tree import isSameTree
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """preorder traversal with time complexity: O(m + n)"""
        if root1 is None and root2 is None:
            return None
        v1: int = root1.val if root1 is not None else 0
        v2: int = root2.val if root2 is not None else 0
        root: TreeNode = TreeNode(v1 + v2)
        root.left = self.mergeTrees(
            root1.left if root1 is not None else None,
            root2.left if root2 is not None else None,
        )
        root.right = self.mergeTrees(
            root1.right if root1 is not None else None,
            root2.right if root2 is not None else None,
        )
        return root


def test_mergeTrees_case_1():
    """This is a test case"""
    # arrange
    root1: list[Optional[int]] = [1, 3, 2, 5]
    root1: Optional[TreeNode] = DeserializeFromList(root1)
    if root1 is None:
        raise Exception("failed")
    root2: list[Optional[int]] = [2, 1, 3, None, 4, None, 7]
    root2: Optional[TreeNode] = DeserializeFromList(root2)
    if root2 is None:
        raise Exception("failed")
    expected: Optional[TreeNode] = DeserializeFromList([3, 4, 5, 5, 4, None, 7])

    # act
    solution = Solution()
    actual = solution.mergeTrees(root1, root2)

    # assert
    assert SerializeBinaryTreeToList(expected) == SerializeBinaryTreeToList(actual)


def test_mergeTrees_case_2():
    """This is a test case"""
    # arrange
    root1: list[Optional[int]] = [1]
    root1: Optional[TreeNode] = DeserializeFromList(root1)
    if root1 is None:
        raise Exception("failed")
    root2: list[Optional[int]] = [1, 2]
    root2: Optional[TreeNode] = DeserializeFromList(root2)
    if root2 is None:
        raise Exception("failed")
    expected: Optional[TreeNode] = DeserializeFromList([2, 2])

    # act
    solution = Solution()
    actual = solution.mergeTrees(root1, root2)

    # assert
    assert SerializeBinaryTreeToList(expected) == SerializeBinaryTreeToList(actual)
