import heapq


class Solution:
    def shortestPath(self, n: int, m: int, edges: list[list[int]]) -> list[int]:
        """
        NOTE:
        - The graph is directed and acyclic with weight.
        - time complexity: O((|V|+|E|)log|V|), where |V| is the number of vertices and |E| is the number of edges. Space complexity: O(|V|)
        - ref: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
        """
        result: list[int] = [float("inf")] * n
        src: int = 0
        graph: dict[int, list[tuple[int, int]]] = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [(edge[1], edge[2])]
            else:
                graph[edge[0]].append((edge[1], edge[2]))
        visited: set[int] = set()
        min_heap: list[tuple[int, int]] = [(0, src)]
        while len(min_heap) > 0:
            accu_dis, node = heapq.heappop(min_heap)
            result[node] = min(result[node], accu_dis)
            if node not in graph or node in visited:
                continue
            visited.add(node)
            for next_node, weight in graph[node]:
                heapq.heappush(min_heap, (accu_dis + weight, next_node))
        return [-1 if x == float("inf") else x for x in result]


def test_shortestPath_case_1():
    # arrange
    n: int = 4
    m: int = 2
    edges: list[list[int]] = [[0, 1, 2], [0, 2, 1]]
    expected: list[list[int]] = [0, 2, 1, -1]

    # act
    solution = Solution()
    actual = solution.shortestPath(n, m, edges)

    # assert
    assert expected == actual


def test_shortestPath_case_2():
    # arrange
    n: int = 6
    m: int = 7
    edges: list[list[int]] = [
        [0, 1, 2],
        [0, 4, 1],
        [4, 5, 4],
        [4, 2, 2],
        [1, 2, 3],
        [2, 3, 6],
        [5, 3, 1],
    ]
    expected: list[list[int]] = [0, 2, 3, 6, 1, 5]

    # act
    solution = Solution()
    actual = solution.shortestPath(n, m, edges)

    # assert
    assert expected == actual


def test_shortestPath_case_3():
    # arrange
    n: int = 10
    m: int = 24
    edges: list[list[int]] = [
        [0, 2, 6],
        [0, 3, 7],
        [0, 4, 9],
        [0, 6, 8],
        [0, 7, 6],
        [1, 2, 6],
        [1, 3, 7],
        [1, 5, 10],
        [1, 6, 1],
        [1, 7, 4],
        [2, 3, 3],
        [2, 6, 10],
        [2, 8, 8],
        [2, 9, 10],
        [3, 5, 3],
        [3, 6, 10],
        [3, 7, 5],
        [5, 6, 9],
        [5, 7, 7],
        [6, 7, 7],
        [6, 8, 8],
        [6, 9, 8],
        [7, 9, 1],
        [8, 9, 6],
    ]
    expected: list[list[int]] = [0, -1, 6, 7, 9, 10, 8, 6, 14, 7]

    # act
    solution = Solution()
    actual = solution.shortestPath(n, m, edges)

    # assert
    assert expected == actual
