import sys

sys.path.append("../models")
from binary_tree_node import TreeNode
from typing import Optional
from deserialize_to_binary_tree import DeserializeFromList
from collections import deque


def SerializeBinaryTreeToList(root: Optional[TreeNode]) -> list[Optional[int]]:
    output: list[Optional[int]] = []
    if root is None:
        return output
    queue: deque[Optional[TreeNode]] = deque()
    queue.append(root)
    while len(queue) > 0:
        node: Optional[TreeNode] = queue.popleft()
        if node is None:
            output.append(None)
        else:
            output.append(node.val)
            if node.left is None and node.right is None:
                continue
            queue.append(node.left)
            queue.append(node.right)
    return output


if __name__ == "__main__":
    vec: list[Optional[int]] = [4, 2, 7, 1, 3, 6, 9]
    root = DeserializeFromList(vec)
    if root == None:
        raise Exception("wrong")

    actual: list[Optional[int]] = SerializeBinaryTreeToList(root)
    print(f"actual: {actual}")

    assert vec == actual
