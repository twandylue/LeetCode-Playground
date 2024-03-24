import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """time complexity: O(n)"""
        que: deque[TreeNode] = deque()
        que.append(root)
        result: int = 0
        while len(que) > 0:
            level_size: int = len(que)
            if que[0] is not None:
                result = que[0].val
            for _ in range(level_size):
                node: TreeNode = que.popleft()
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
        return result


def test_findBottomLeftValue_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([2, 1, 3])
    expected: int = 1

    # act
    actual: int = Solution().findBottomLeftValue(root)

    # assert
    assert actual == expected


def test_findBottomLeftValue_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList(
        [1, 2, 3, 4, None, 5, 6, None, None, 7]
    )
    expected: int = 7

    # act
    actual: int = Solution().findBottomLeftValue(root)

    # assert
    assert actual == expected
