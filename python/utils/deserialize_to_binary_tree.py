# ref: https://leetcode.com/problems/recover-binary-search-tree/solutions/32539/Tree-Deserializer-and-Visualizer-for-Python
import sys

sys.path.append("../models")
from binary_tree_node import TreeNode
from typing import Optional
from collections import deque


def DeserializeFromList(vector: list[Optional[int]]) -> Optional[TreeNode]:
    if len(vector) == 0:
        return None
    nodes: list[Optional[TreeNode]] = []
    for i in range(len(vector)):
        if vector[i] == None:
            nodes.append(None)
        else:
            nodes.append(TreeNode(vector[i]))

    index: int = 0
    deq: deque[Optional[TreeNode]] = deque()
    root: Optional[TreeNode] = nodes[index]
    index += 1
    deq.append(root)
    while len(deq) > 0 and index < len(nodes):
        n: Optional[TreeNode] = deq.popleft()
        if n == None:
            raise Exception("Node in deque is None")

        if nodes[index] == None:
            n.left = None
            break
        else:
            n.left = nodes[index]
            index += 1

        if nodes[index] == None:
            n.right = None
            break
        else:
            n.right = nodes[index]
            index += 1

        if n.left != None:
            deq.append(n.left)

        if n.right != None:
            deq.append(n.right)

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


# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#     def __repr__(self):
#         return 'TreeNode({})'.format(self.val)

## NOTE: need to install turtle
# def drawtree(root):
#     def height(root):
#         return 1 + max(height(root.left), height(root.right)) if root else -1
#     def jumpto(x, y):
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
#     def draw(node, x, y, dx):
#         if node:
#             t.goto(x, y)
#             jumpto(x, y-20)
#             t.write(node.val, align='center', font=('Arial', 12, 'normal'))
#             draw(node.left, x-dx, y-60, dx/2)
#             jumpto(x, y-20)
#             draw(node.right, x+dx, y-60, dx/2)
#     import turtle
#     t = turtle.Turtle()
#     t.speed(0); turtle.delay(0)
#     h = height(root)
#     jumpto(0, 30*h)
#     draw(root, 0, 30*h, 40*h)
#     t.hideturtle()
#     turtle.mainloop()

if __name__ == "__main__":
    root = DeserializeFromList([4, 2, 7, 1, 3, 6, 9])
    if root == None:
        raise Exception("wrong")

    # deserializeFromString("[1,2,3,null,null,4,null,null,5]")
    # drawtree(deserializeFromString('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
