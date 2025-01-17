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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """time complexity: O(h) where h is the height of the tree."""
        if p.val > q.val:
            p, q = q, p
        return self.dfs(root, p, q)

    def dfs(
        self, node: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        if node is None or node == p or node == q:
            return node
        if node.val > p.val and node.val < q.val:
            return node
        if node.val > q.val:
            return self.dfs(node.left, p, q)
        return self.dfs(node.right, p, q)


def test_lowestCommonAncestor_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList(
        [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    )
    if root is None:
        raise Exception("failed")
    p: TreeNode = TreeNode(2)
    q: TreeNode = TreeNode(8)
    expected: TreeNode = TreeNode(6)

    # act
    solution = Solution()
    actual = solution.lowestCommonAncestor(root, p, q)

    # assert
    assert expected.val == actual.val


def test_lowestCommonAncestor_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList(
        [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    )
    if root is None:
        raise Exception("failed")
    p: TreeNode = TreeNode(2)
    q: TreeNode = TreeNode(4)
    expected: TreeNode = TreeNode(2)

    # act
    solution = Solution()
    actual = solution.lowestCommonAncestor(root, p, q)

    # assert
    assert expected.val == actual.val


def test_lowestCommonAncestor_case_3():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([2, 1])
    if root is None:
        raise Exception("failed")
    p: TreeNode = TreeNode(2)
    q: TreeNode = TreeNode(1)
    expected: TreeNode = TreeNode(2)

    # act
    solution = Solution()
    actual = solution.lowestCommonAncestor(root, p, q)

    # assert
    assert expected.val == actual.val
