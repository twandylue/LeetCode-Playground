import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """time complexity: O(n)"""
        return self.dfs(root)[0]

    def dfs(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        """postorder traversal"""
        if root is None:
            return (True, 0)
        left: tuple[bool, int] = self.dfs(root.left)
        right: tuple[bool, int] = self.dfs(root.right)
        is_balanced: bool = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return (is_balanced, max(left[1], right[1]) + 1)


def test_isBalanced_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 9, 20, None, None, 15, 7])
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isBalanced(root)

    # assert
    assert expected == actual


def test_isBalanced_case_2():
    # arrange
    arr: list[Optional[int]] = [1, 2, 2, 3, 3, None, None, 4, 4]
    root: Optional[TreeNode] = DeserializeFromList(arr)
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isBalanced(root)

    # assert
    assert expected == actual


def test_isBalanced_case_3():
    # arrange
    root: Optional[TreeNode] = None
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isBalanced(root)

    # assert
    assert expected == actual
