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
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """DFS, time complexity: O(n)"""
        if root.left == None or root.right == None:
            return root.val == 1
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        return 0

    def evaluateTree2(self, root: Optional[TreeNode]) -> bool:
        """BFS, time complexity: O(n)"""
        stack: list[TreeNode] = [root]
        value: dict[TreeNode, bool] = {}
        while len(stack) > 0:
            node: TreeNode = stack.pop()
            if node.left == None or node.right == None:
                value[node] = node.val == 1
            else:
                if node.left in value and node.right in value:
                    if node.val == 2:
                        value[node] = value[node.left] or value[node.right]
                    if node.val == 3:
                        value[node] = value[node.left] and value[node.right]
                else:
                    stack.extend([node, node.left, node.right])
        return value[root]


def test_evaluateTree_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([2, 1, 3, None, None, 0, 1])
    expected: bool = True

    # act
    actual = Solution().evaluateTree(root)

    # assert
    assert expected == actual


def test_evaluateTree_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([0])
    expected: bool = False

    # act
    actual = Solution().evaluateTree(root)

    # assert
    assert expected == actual


def test_evaluateTree_case_3():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([0])
    expected: bool = False

    # act
    actual = Solution().evaluateTree2(root)

    # assert
    assert expected == actual


def test_evaluateTree_case_4():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([2, 1, 3, None, None, 0, 1])
    expected: bool = True

    # act
    actual = Solution().evaluateTree2(root)

    # assert
    assert expected == actual
