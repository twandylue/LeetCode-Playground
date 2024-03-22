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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """time complexity: O(n)"""
        return self.dfs(root, -float("inf"), float("inf"))

    def dfs(self, node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
        """dfs in preorder traversal"""
        if node is None:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return self.dfs(node.left, min_val, node.val) and self.dfs(
            node.right, node.val, max_val
        )


def test_isValidBST_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([2, 1, 3])
    if root == None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isValidBST(root)

    # assert
    assert actual == True


def test_isValidBST_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([5, 1, 4, None, None, 3, 6])
    if root == None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isValidBST(root)

    # assert
    assert actual == False
