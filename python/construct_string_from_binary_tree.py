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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """time complexity: O(n)"""
        return self.dfs(root)

    def dfs(self, root: Optional[TreeNode]) -> str:
        """postorder traversal"""
        if root is None:
            return ""
        left: str = self.dfs(root.left)
        right: str = self.dfs(root.right)
        if left == "" and right == "":
            return str(root.val)
        if left != "" and right == "":
            return str(root.val) + "(" + left + ")"
        if left == "" and right != "":
            return str(root.val) + "()" + "(" + right + ")"
        return str(root.val) + "(" + left + ")" + "(" + right + ")"


def test_tree2str_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 2, 3, 4])
    if root is None:
        raise Exception("failed")
    expected: str = "1(2(4))(3)"

    # act
    solution = Solution()
    actual = solution.tree2str(root)

    # assert
    assert expected == actual


def test_tree2str_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 2, 3, None, 4])
    if root is None:
        raise Exception("failed")
    expected: str = "1(2()(4))(3)"

    # act
    solution = Solution()
    actual = solution.tree2str(root)

    # assert
    assert expected == actual
