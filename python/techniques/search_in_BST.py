import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


# NOTE:
# time complexity: O(logn)
# ref: search_in_a_binary_search_tree.py
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    curr: Optional[TreeNode] = root
    while curr is not None:
        if curr.val == val:
            return curr
        if curr.val > val:
            curr = curr.left
        else:
            curr = curr.right
    return None
