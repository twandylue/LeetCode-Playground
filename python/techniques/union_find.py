class UnionFind:
    def __init__(self, n: int):
        self._parents: list[int] = [i for i in range(n)]
        self._ranks: list[int] = [1] * n
        self._indep: int = n  # number of independent components

    def find(self, x: int) -> int:
        curr: int = x
        while curr != self._parents[curr]:
            parent = self._parents[curr]
            self._parents[curr] = self._parents[self._parents[curr]]
            curr = parent
        return curr

    def find2(self, node: int) -> int:
        if node != self._parents[node]:
            node = self._parents[node]
        return node

    def union(self, u: int, v: int) -> bool:
        pu: int = self.find2(u)
        pv: int = self.find2(v)
        if pu == pv:
            return False
        if self._ranks[pu] < self._ranks[pv]:
            pu, pv = pv, pu
        self._ranks[pu] += self._ranks[pv]
        self._parents[pv] = pu
        self._indep -= 1  # reduce the number of independent components
        return True

    def get_indep(self) -> int:
        """
        Get the number of independent components
        """
        return self._indep
