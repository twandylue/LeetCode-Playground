from typing import Optional
import sys

sys.path.append("./models")
from binary_tree_node import TreeNode

sys.path.append("./utils")
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True

        pResult: list[Optional[TreeNode]] = self.dfs(p, list())
        qResult: list[Optional[TreeNode]] = self.dfs(q, list())

        if len(qResult) != len(pResult):
            return False
        for i in range(0, len(qResult)):
            if qResult[i] is None and pResult[i] is None:
                continue
            if (qResult[i] is None and pResult[i] is not None) or (
                qResult[i] is not None and pResult[i] is None
            ):
                return False
            if qResult[i].val != pResult[i].val:
                return False
        return True

    def dfs(
        self, n: Optional[TreeNode], v: list[Optional[TreeNode]]
    ) -> list[Optional[TreeNode]]:
        if n is None:
            v.append(None)
            return v

        v.append(n)
        self.dfs(n.left, v)
        self.dfs(n.right, v)

        return v


def test_isSameTree_case_1():
    # arrange
    p: Optional[TreeNode] = DeserializeFromList([1, 2, 3])
    if p == None:
        raise Exception("failed")

    q: Optional[TreeNode] = DeserializeFromList([1, 2, 3])
    if q == None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isSameTree(p, q)

    # assert
    assert actual == True


def test_isSameTree_case_2():
    # arrange
    p: Optional[TreeNode] = DeserializeFromList([0])
    if p == None:
        raise Exception("failed")

    q: Optional[TreeNode] = DeserializeFromList([1])
    if q == None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isSameTree(p, q)

    # assert
    assert actual == False
