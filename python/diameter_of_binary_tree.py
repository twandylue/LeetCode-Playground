from typing import Optional
import sys

sys.path.append("./models")
from binary_tree_node import TreeNode

sys.path.append("./utils")
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


class Solution:
    maxDis: int

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDis: int = 0
        self.helper(root, self.maxDis)
        return self.maxDis

    def helper(self, root: Optional[TreeNode], maxDis: int) -> int:
        if root == None:
            return 0
        left = self.helper(root.left, maxDis)
        right = self.helper(root.right, maxDis)
        self.maxDis = max(left + right, maxDis)

        return max(left, right) + 1


def test_diameterOfBinaryTree_case_1():
    # arrange
    arr: list[int] = [1, 2, 3, 4, 5]
    root: Optional[TreeNode] = DeserializeFromList(arr)
    if root == None:
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
    if root == None:
        raise Exception("failed")
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.diameterOfBinaryTree(root)

    # assert
    assert expected == actual
