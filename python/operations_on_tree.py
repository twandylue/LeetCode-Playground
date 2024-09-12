from typing import Optional
from collections import deque


class LockingTree:

    def __init__(self, parent: list[int]):
        self._parent: list[int] = parent
        self._locked: list[Optional[int]] = [None] * len(parent)
        self._child: dict[int, list[int]] = {i: [] for i in range(len(parent))}
        for i in range(1, len(parent)):
            self._child[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        """time complexity: O(1)"""
        if self._locked[num] is not None:
            return False
        self._locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        """time complexity: O(1)"""
        if self._locked[num] != user:
            return False
        self._locked[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        """time complexity: O(n)"""
        i: int = num
        while i != -1:
            if self._locked[i] is not None:
                return False
            i = self._parent[i]
        lockedCount: int = 0
        queue: deque[int] = deque([num])
        while len(queue) > 0:
            n: int = queue.popleft()
            if self._locked[n] is not None:
                self._locked[n] = None
                lockedCount += 1
            queue.extend(self._child[n])
        if lockedCount > 0:
            self._locked[num] = user
        return lockedCount > 0


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
def test_BSTIterator_case_1():
    """This is a test case"""
    lockingTree: LockingTree = LockingTree([-1, 0, 0, 1, 1, 2, 2])
    assert lockingTree.lock(2, 2)  # return true because node 2 is unlocked.
    # Node 2 will now be locked by user 2.
    assert not lockingTree.unlock(
        2, 3
    )  # return false because user 3 cannot unlock a node locked by user 2.
    assert lockingTree.unlock(
        2, 2
    )  # return true because node 2 was previously locked by user 2.
    # Node 2 will now be unlocked.
    assert lockingTree.lock(4, 5)
    # return true because node 4 is unlocked.
    # Node 4 will now be locked by user 5.
    assert lockingTree.upgrade(0, 1)
    # return true because node 0 is unlocked and has at least one locked descendant (node 4).
    # Node 0 will now be locked by user 1 and node 4 will now be unlocked.
    assert not lockingTree.lock(0, 1)
    # return false because node 0 is already locked.
