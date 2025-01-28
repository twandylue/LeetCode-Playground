class UnionFind:
    def __init__(self, n: int):
        self._parents: list[int] = [i for i in range(n)]
        self._ranks: list[int] = [1] * n

    def find(self, x: int) -> int:
        curr: int = x
        while curr != self._parents[curr]:
            parent = self._parents[curr]
            self._parents[curr] = self._parents[self._parents[curr]]
            curr = parent
        return curr

    def find2(self, node: int) -> int:
        if node != self._parents[node]:
            node = self.find(self._parents[node])
        return node

    def union(self, x1: int, x2: int) -> bool:
        p1: int = self.find(x1)
        p2: int = self.find(x2)
        if p1 == p2:
            return False
        if self._ranks[p1] < self._ranks[p2]:
            p1, p2 = p2, p1
        self._ranks[p1] += self._ranks[p2]
        self._parents[p2] = p1
        return True
