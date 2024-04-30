import heapq


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
