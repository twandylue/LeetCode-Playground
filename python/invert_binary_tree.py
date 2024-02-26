"""module to reorder the linked list"""

import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        return self.dfs(root)

    def dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        self.dfs(root.left)
        self.dfs(root.right)
        root.left, root.right = root.right, root.left
        return root


def test_invertTree_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([4, 2, 7, 1, 3, 6, 9])
    if root is None:
        raise Exception("failed")

    expected: Optional[TreeNode] = DeserializeFromList([4, 7, 2, 9, 6, 3, 1])
    if expected is None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.invertTree(root)

    # assert
    assert SerializeBinaryTreeToList(expected) == SerializeBinaryTreeToList(actual)
