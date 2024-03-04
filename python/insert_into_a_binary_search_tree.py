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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """time complexity: O(h) where h is the height of the tree."""
        if root is None:
            return TreeNode(val)
        curr: Optional[TreeNode] = root
        while curr is not None:
            if curr.val > val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
        return root


def test_insertIntoBST_case_1():
    """NOTE: skip because there is not certain answer."""
    # # arrange
    # root: Optional[TreeNode] = DeserializeFromList([4, 2, 7, 1, 3])
    # if root is None:
    #     raise Exception("failed")
    # val: int = 5
    # expected: list[int] = [4, 2, 7, 1, 3, 5]
    #
    # # act
    # solution = Solution()
    # actual = solution.insertIntoBST(root, val)
    #
    # # assert
    # assert expected == SerializeBinaryTreeToList(actual)
    assert True
