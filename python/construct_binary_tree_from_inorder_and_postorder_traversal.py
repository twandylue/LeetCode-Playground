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
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        """time complexity: O(n)"""
        inorder_map: dict[int, int] = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        return self.build_helper(0, len(inorder) - 1, inorder, postorder, inorder_map)

    def build_helper(
        self,
        l: int,
        r: int,
        inorder: list[int],
        postorder: list[int],
        inorder_map: dict[int, int],
    ) -> Optional[TreeNode]:
        """helper function for buildTree. It's not a dfs, just a recursive function."""
        if l > r:
            return None
        root = TreeNode(postorder.pop())
        idx: int = inorder_map[root.val]
        root.right = self.build_helper(idx + 1, r, inorder, postorder, inorder_map)
        root.left = self.build_helper(l, idx - 1, inorder, postorder, inorder_map)
        return root


def test_buildTree_case_1():
    """This is a test case"""
    # arrange
    inorder: list[int] = [9, 3, 15, 20, 7]
    postorder: list[int] = [9, 15, 7, 20, 3]
    expected: Optional[TreeNode] = DeserializeFromList([3, 9, 20, None, None, 15, 7])

    # act
    solution = Solution()
    actual = solution.buildTree(inorder, postorder)

    # assert
    assert SerializeBinaryTreeToList(expected) == SerializeBinaryTreeToList(actual)
