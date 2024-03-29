# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

    def __init__(self, val: int = 0) -> "TreeNode":
        self.val = val
