import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """time complexity: O(n), this problem is to find out the "longest path"""
        #  NOTE: hint
        # |path rooted at node|= height(left)+height(right)
        # height(node)=1+max(height(left), height(right))
        if root is None:
            return 0
        return self.dfs(root.left) + self.dfs(root.right)

    def dfs(self, root: Optional[TreeNode]) -> int:
        """postorder traversal"""
        if root is None:
            return 0
        left: int = self.dfs(root.left)
        right: int = self.dfs(root.right)

        return 1 + max(left, right)


def test_diameterOfBinaryTree_case_1():
    # arrange
    arr: list[int] = [1, 2, 3, 4, 5]
    root: Optional[TreeNode] = DeserializeFromList(arr)
    if root is None:
        raise Exception("failed")
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.diameterOfBinaryTree(root)

    # assert
    assert expected == actual


def test_diameterOfBinaryTree_case_2():
    # arrange
    arr: list[int] = [1, 2]
    root: Optional[TreeNode] = DeserializeFromList(arr)
    if root is None:
        raise Exception("failed")
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.diameterOfBinaryTree(root)

    # assert
    assert expected == actual
