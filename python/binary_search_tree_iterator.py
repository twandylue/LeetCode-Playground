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
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        """time complexity: O(n)"""
        self._arr: list[int] = []
        self.dfs(root, self._arr)
        self._p: int = 0

    def dfs(self, node: Optional[TreeNode], arr: list[int]) -> None:
        if node is None:
            return
        self.dfs(node.left, arr)
        arr.append(node.val)
        self.dfs(node.right, arr)

    def next(self) -> int:
        if self._p >= len(self._arr):
            return 0
        result: int = self._arr[self._p]
        self._p += 1
        return result

    def hasNext(self) -> bool:
        if self._p < len(self._arr):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
def test_BSTIterator_case_1():
    """This is a test case"""
    bSTIterator: BSTIterator = BSTIterator(
        DeserializeFromList([7, 3, 15, None, None, 9, 20])
    )
    assert bSTIterator.next() == 3  ## return 3
    assert bSTIterator.next() == 7  ## return 7
    assert bSTIterator.hasNext()  ## return True
    assert bSTIterator.next() == 9  ## return 9
    assert bSTIterator.hasNext()  ## return True
    assert bSTIterator.next() == 15  ## return 15
    assert bSTIterator.hasNext()  ## return True
    assert bSTIterator.next() == 20  ## return 20
    assert not bSTIterator.hasNext()  ## return False
