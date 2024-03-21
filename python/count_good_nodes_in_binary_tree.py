import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """time complexity: O(n)"""
        return self.dfs(root.val, root)

    def dfs(self, max_val: int, node: Optional[TreeNode]) -> int:
        """dfs in preorder traversal"""
        if node is None:
            return 0
        count: int = 0
        if node.val >= max_val:
            count += 1
        max_val = max(max_val, node.val)
        count += self.dfs(max_val, node.left) + self.dfs(max_val, node.right)
        return count


def test_goodNodes_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 1, 4, 3, None, 1, 5])
    expected: int = 4

    # act
    actual: int = Solution().goodNodes(root)

    # assert
    assert actual == expected


def test_goodNodes_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1])
    expected: int = 1

    # act
    actual: int = Solution().goodNodes(root)

    # assert
    assert actual == expected


def test_goodNodes_case_3():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 3, None, 4, 2])
    expected: int = 3

    # act
    actual: int = Solution().goodNodes(root)

    # assert
    assert actual == expected
