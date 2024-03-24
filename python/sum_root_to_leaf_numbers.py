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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result: list[int] = [0]
        self.dfs(root, [], result)
        return result[0]

    def dfs(self, node: Optional[TreeNode], accu: list[str], result: list[int]) -> None:
        """dfs in preorder"""
        if node is None:
            return
        accu.append(str(node.val))
        if node.left is None and node.right is None:
            s: str = "".join(accu)
            result[0] += int(s)
        self.dfs(node.left, accu, result)
        self.dfs(node.right, accu, result)
        accu.pop()

    # NOTE: it also works
    # def sumNumbers(self, root: Optional[TreeNode]) -> int:
    #     """time complexity: O(n)"""
    #     return self.dfs(root, 0)
    #
    # def dfs(self, node: Optional[TreeNode], accu: int) -> int:
    #     """dfs in preorder"""
    #     if node is None:
    #         return 0
    #     accu = accu * 10 + node.val
    #     if node.left is None and node.right is None:
    #         return accu
    #     return self.dfs(node.left, accu) + self.dfs(node.right, accu)


def test_sumNumbers_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 2, 3])
    expected: int = 25

    # act
    actual: int = Solution().sumNumbers(root)

    # assert
    assert actual == expected


def test_sumNumbers_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([4, 9, 0, 5, 1])
    expected: int = 1026

    # act
    actual: int = Solution().sumNumbers(root)

    # assert
    assert actual == expected
