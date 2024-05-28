class UnionFind:
    def __init__(self, n: int):
        self._parents: list[int] = [i for i in range(n)]
        self._ranks: list[int] = [1] * n

    def find(self, x: int) -> int:
        while x != self._parents[x]:
            tmp: int = self._parents[x]
            self._parents[x] = self._parents[self._parents[x]]
            x = tmp
        return x

    def union(self, x1: int, x2: int) -> bool:
        p1: int = self.find(x1)
        p2: int = self.find(x2)
        if p1 == p2:
            return False
        if self._ranks[p1] > self._ranks[p2]:
            self._ranks[p1] += self._ranks[p2]
            self._parents[p2] = p1
        else:
            self._ranks[p2] += self._ranks[p2]
            self._parents[p1] = p2
        return True
