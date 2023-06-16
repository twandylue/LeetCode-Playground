import collections
import sys

sys.path.append("../models")
from binary_tree_node import TreeNode
from typing import Deque, Optional
from deserialize_to_binary_tree import DeserializeFromList


def SerializeBinaryTreeToList(root: Optional[TreeNode]) -> list[Optional[int]]:
    output: list[Optional[int]] = []
    stack: Deque[Optional[TreeNode]] = collections.deque()
    stack.append(root)
    while len(stack) > 0:
        node = stack.popleft()
        if node == None:
            continue
        else:
            output.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

    return output


if __name__ == "__main__":
    vec: list[Optional[int]] = [4, 2, 7, 1, 3, 6, 9]
    root = DeserializeFromList(vec)
    if root == None:
        raise Exception("wrong")

    actual: list[Optional[int]] = SerializeBinaryTreeToList(root)
    print(f"actual: {actual}")

    assert vec == actual
