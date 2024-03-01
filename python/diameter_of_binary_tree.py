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
        # NOTE: This is a skill to use a list to pass by reference
        max_diameter: list[int] = [0]
        self.dfs(root, max_diameter)
        return max_diameter[0]

    def dfs(self, root: Optional[TreeNode], max_diameter: list[int]) -> int:
        """postorder traversal"""
        if root is None:
            return 0
        left: int = self.dfs(root.left, max_diameter)
        right: int = self.dfs(root.right, max_diameter)
        max_diameter[0] = max(max_diameter[0], left + right)
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


def test_diameterOfBinaryTree_case_3():
    # arrange
    arr: list[int] = [
        4,
        -7,
        -3,
        None,
        None,
        -9,
        -3,
        9,
        -7,
        -4,
        None,
        6,
        None,
        -6,
        -6,
        None,
        None,
        0,
        6,
        5,
        None,
        9,
        None,
        None,
        -1,
        -4,
        None,
        None,
        None,
        -2,
    ]
    root: Optional[TreeNode] = DeserializeFromList(arr)
    if root is None:
        raise Exception("failed")
    expected: int = 8

    # act
    solution = Solution()
    actual = solution.diameterOfBinaryTree(root)

    # assert
    assert expected == actual
