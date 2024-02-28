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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """time complexity: O(n)"""
        return self.dfs(p, q)

    def dfs(self, p: Optional[TreeNode], q: list[Optional[TreeNode]]) -> bool:
        """preorder traversal"""
        if p is None and q is None:
            return True

        if p is None and q is not None:
            return False

        if p is not None and q is None:
            return False

        if p.val != q.val:
            return False

        return self.dfs(p.right, q.right) and self.dfs(p.left, q.left)


def test_isSameTree_case_1():
    # arrange
    p: Optional[TreeNode] = DeserializeFromList([1, 2, 3])
    if p is None:
        raise Exception("failed")

    q: Optional[TreeNode] = DeserializeFromList([1, 2, 3])
    if q is None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isSameTree(p, q)

    # assert
    assert actual == True


def test_isSameTree_case_2():
    # arrange
    p: Optional[TreeNode] = DeserializeFromList([0])
    if p is None:
        raise Exception("failed")

    q: Optional[TreeNode] = DeserializeFromList([1])
    if q is None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isSameTree(p, q)

    # assert
    assert actual == False
