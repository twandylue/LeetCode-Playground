import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        """time complexity: O(n)"""
        """dfs in preorder traversal"""
        if root is None:
            return None
        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


def test_trimBST_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 0, 2])
    low: int = 1
    high: int = 2
    expected: Optional[TreeNode] = DeserializeFromList([1, None, 2])

    # act
    actual: int = Solution().trimBST(root, low, high)

    # assert
    assert SerializeBinaryTreeToList(expected) == SerializeBinaryTreeToList(actual)


def test_trimBST_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 0, 4, None, 2, None, None, 1])
    low: int = 1
    high: int = 3
    expected: Optional[TreeNode] = DeserializeFromList([3, 2, None, 1])

    # act
    actual: int = Solution().trimBST(root, low, high)

    # assert
    assert SerializeBinaryTreeToList(expected) == SerializeBinaryTreeToList(actual)
