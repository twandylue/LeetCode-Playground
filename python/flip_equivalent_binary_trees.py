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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """time complexity: O(n). dfs in preorder traversal."""
        if root1 is None or root2 is None:
            return root1 is None and root2 is None
        if root1.val != root2.val:
            return False
        first: bool = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(
            root1.right, root2.right
        )
        second: bool = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(
            root1.right, root2.left
        )
        return first or second


def test_flipEquiv_case_1():
    """This is a test case"""
    # arrange
    root1: Optional[TreeNode] = DeserializeFromList(
        [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
    )
    root2: Optional[TreeNode] = DeserializeFromList(
        [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]
    )
    expected: bool = True

    # act
    actual: int = Solution().flipEquiv(root1, root2)

    # assert
    assert expected == actual


def test_flipEquiv_case_2():
    """This is a test case"""
    # arrange
    root1: Optional[TreeNode] = DeserializeFromList([])
    root2: Optional[TreeNode] = DeserializeFromList([])
    expected: bool = True

    # act
    actual: int = Solution().flipEquiv(root1, root2)

    # assert
    assert expected == actual


def test_flipEquiv_case_3():
    """This is a test case"""
    # arrange
    root1: Optional[TreeNode] = DeserializeFromList([])
    root2: Optional[TreeNode] = DeserializeFromList([1])
    expected: bool = False

    # act
    actual: int = Solution().flipEquiv(root1, root2)

    # assert
    assert expected == actual
