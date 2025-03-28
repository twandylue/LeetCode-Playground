import heapq
from collections import defaultdict


class Solution:
    def findItinerary2(self, tickets: list[list[str]]) -> list[str]:
        """Time complexity: O(E log E), where E is the number of edges (tickets)."""
        result: list[str] = []
        adj: dict[str, list[str]] = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
        self.dfs2("JFK", adj, result)
        return result[::-1]

    def dfs2(self, src: str, adj: dict[str, list[str]], result: list[str]):
        while len(adj[src]) > 0:
            next_stop: str = heapq.heappop(adj[src])
            self.dfs2(next_stop, adj, result)
        result.append(src)

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj_stops: dict[str, list[str]] = dict()
        result: list[str] = ["JFK"]
        for t in tickets:
            if t[0] in adj_stops:
                adj_stops[t[0]].append(t[1])
            else:
                adj_stops[t[0]] = [t[1]]

        for stops in adj_stops.values():
            stops.sort()

        self.dfs("JFK", adj_stops, tickets, result)

        return result

    def dfs(
        self,
        src: str,
        adj_stops: dict[str, list[str]],
        tickets: list[list[str]],
        result: list[str],
    ) -> bool:
        if len(result) == len(tickets) + 1:
            return True

        if src not in adj_stops:
            return False

        tmpNextStops: list[str] = adj_stops[src].copy()
        for i in range(0, len(tmpNextStops)):
            adj_stops[src].remove(tmpNextStops[i])
            result.append(tmpNextStops[i])
            if self.dfs(tmpNextStops[i], adj_stops, tickets, result):
                return True
            adj_stops[src].insert(i, tmpNextStops[i])
            result.pop()

        return False


def test_findItinerary_case_1():
    # Arrange
    tickets: list[list[str]] = [
        ["MUC", "LHR"],
        ["JFK", "MUC"],
        ["SFO", "SJC"],
        ["LHR", "SFO"],
    ]
    expected: list[str] = ["JFK", "MUC", "LHR", "SFO", "SJC"]

    # Act
    actual = Solution().findItinerary(tickets)

    # Assert
    assert actual == expected


def test_findItinerary_case_2():
    # Arrange
    tickets: list[list[str]] = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"],
    ]
    expected = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]

    # Act
    actual = Solution().findItinerary(tickets)

    # Assert
    assert actual == expected


def test_findItinerary_case_3():
    # Arrange
    tickets: list[list[str]] = [
        ["JFK", "ATL"],
    ]
    expected = ["JFK", "ATL"]

    # Act
    actual = Solution().findItinerary(tickets)

    # Assert
    assert actual == expected


def test_findItinerary_case_4():
    # Arrange
    tickets: list[list[str]] = [
        ["JFK", "KUL"],
        ["JFK", "NRT"],
        ["NRT", "JFK"],
    ]
    expected = ["JFK", "NRT", "JFK", "KUL"]

    # Act
    actual = Solution().findItinerary(tickets)

    # Assert
    assert actual == expected


def test_findItinerary_case_5():
    # Arrange
    tickets: list[list[str]] = [
        ["JFK", "KUL"],
        ["JFK", "NRT"],
        ["NRT", "JFK"],
    ]
    expected = ["JFK", "NRT", "JFK", "KUL"]

    # Act
    actual = Solution().findItinerary2(tickets)

    # Assert
    assert actual == expected
