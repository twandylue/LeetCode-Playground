import sys

sys.path.append("../models")
from binary_tree_node import TreeNode
from typing import Optional
from collections import deque


# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#     def __repr__(self):
#         return 'TreeNode({})'.format(self.val)
def DeserializeFromList(vector: list[Optional[int]]) -> Optional[TreeNode]:
    """Deserialize a list to a binary tree by level order traversal (BFS)."""
    if len(vector) == 0:
        return None
    originalQueue: deque[Optional[TreeNode]] = deque()
    tempQueue: deque[Optional[TreeNode]] = deque()
    for i in range(len(vector)):
        if vector[i] == None:
            originalQueue.append(None)
        else:
            originalQueue.append(TreeNode(vector[i]))

    root: Optional[TreeNode] = originalQueue.popleft()
    tempQueue.append(root)

    while len(tempQueue) > 0:
        n: Optional[TreeNode] = tempQueue.popleft()
        if len(originalQueue) > 0:
            n.left = originalQueue.popleft()
            if n.left != None:
                tempQueue.append(n.left)
        if len(originalQueue) > 0:
            n.right = originalQueue.popleft()
            if n.right != None:
                tempQueue.append(n.right)

    return root


def deserializeFromString(string):
    if string == "{}":
        return None
    nodes = [
        None if val == "null" else TreeNode(int(val))
        for val in string.strip("[]{}").split(",")
    ]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# # NOTE: need to install turtle
# def drawtree(root):
#     def height(root):
#         return 1 + max(height(root.left), height(root.right)) if root else -1
#
#     def jumpto(x, y):
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
#
#     def draw(node, x, y, dx):
#         if node:
#             t.goto(x, y)
#             jumpto(x, y - 20)
#             t.write(node.val, align="center", font=("Arial", 12, "normal"))
#             draw(node.left, x - dx, y - 60, dx / 2)
#             jumpto(x, y - 20)
#             draw(node.right, x + dx, y - 60, dx / 2)
#
#     import turtle
#
#     t = turtle.Turtle()
#     t.speed(0)
#     turtle.delay(0)
#     h = height(root)
#     jumpto(0, 30 * h)
#     draw(root, 0, 30 * h, 40 * h)
#     t.hideturtle()
#     turtle.mainloop()


if __name__ == "__main__":
    arr: list[Optional[int]] = [1, 2, 2, 3, 3, None, None, 4, 4, None, None]
    root = DeserializeFromList(arr)
    if root == None:
        raise Exception("wrong")

    # deserializeFromString("[1,2,3,null,null,4,null,null,5]")
    # drawtree(deserializeFromString('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
