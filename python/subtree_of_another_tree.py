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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """time complexity: O(n)"""
        if root is None:
            return False
        if subRoot is None or self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """preorder traversal"""
        if p is None and q is None:
            return True
        if p is not None and q is None:
            return False
        if p is None and q is not None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


def test_isSubtree_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 4, 5, 1, 2])
    if root is None:
        raise Exception("failed")

    subRoot: Optional[TreeNode] = DeserializeFromList([4, 1, 2])
    if subRoot is None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isSubtree(root, subRoot)

    # assert
    assert actual
