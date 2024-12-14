import sys

sys.path.append("./models")
sys.path.append("./utils")

from collections import deque
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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """time complexity: O(n)"""
        preorder_queue: deque[int] = deque(preorder)
        inorder_map: dict[int, int] = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        return self.build_helper(
            0, len(inorder) - 1, preorder_queue, inorder, inorder_map
        )

    def build_helper(
        self,
        l: int,
        r: int,
        preorder_queue: deque[int],
        inorder: list[int],
        inorder_map: dict[int, int],
    ) -> Optional[TreeNode]:
        if l > r:
            return None
        root: TreeNode = TreeNode(preorder_queue.popleft())
        inorder_idx: int = inorder_map[root.val]
        root.left = self.build_helper(
            l, inorder_idx - 1, preorder_queue, inorder, inorder_map
        )
        root.right = self.build_helper(
            inorder_idx + 1, r, preorder_queue, inorder, inorder_map
        )
        return root


def test_buildTree_case_1():
    """This is a test case"""
    # arrange
    preorder: list[int] = [3, 9, 20, 15, 7]
    inorder: list[int] = [9, 3, 15, 20, 7]
    expected: Optional[TreeNode] = DeserializeFromList([3, 9, 20, None, None, 15, 7])

    # act
    solution = Solution()
    actual = solution.buildTree(preorder, inorder)

    # assert
    assert SerializeBinaryTreeToList(expected) == SerializeBinaryTreeToList(actual)


def test_buildTree_case_2():
    """This is a test case"""
    # arrange
    preorder: list[int] = [-1]
    inorder: list[int] = [-1]
    expected: Optional[TreeNode] = DeserializeFromList([-1])

    # act
    solution = Solution()
    actual = solution.buildTree(preorder, inorder)

    # assert
    assert SerializeBinaryTreeToList(expected) == SerializeBinaryTreeToList(actual)
