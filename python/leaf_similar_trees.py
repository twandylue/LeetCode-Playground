import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """time complexity: O(m + n) where m is the nodes of root1 and n is the nodes of root2"""
        array1: list[int] = []
        array2: list[int] = []
        self.dfs(root1, array1)
        self.dfs(root2, array2)
        return array1 == array2

    def dfs(self, root: Optional[TreeNode], arr: list[int]):
        if root is None:
            return
        if root.left is None and root.right is None:
            arr.append(root.val)
            return
        self.dfs(root.left, arr)
        self.dfs(root.right, arr)


def test_leafSimilar_case_1():
    # arrange
    root1: Optional[TreeNode] = DeserializeFromList(
        [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    )
    root2: Optional[TreeNode] = DeserializeFromList(
        [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    )
    expected: bool = True

    # act
    actual: bool = Solution().leafSimilar(root1, root2)

    # assert
    assert expected == actual


def test_leafSimilar_case_2():
    # arrange
    root1: Optional[TreeNode] = DeserializeFromList([1, 2, 3])
    root2: Optional[TreeNode] = DeserializeFromList([1, 3, 2])
    expected: bool = False

    # act
    actual: bool = Solution().leafSimilar(root1, root2)

    # assert
    assert expected == actual
