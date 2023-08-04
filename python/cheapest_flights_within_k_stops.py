class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        prices: list[float] = [float("inf")] * n
        prices[src] = 0
        for _ in range(0, k + 1):
            tmpPrices = prices.copy()
            for flight in flights:
                s: int = flight[0]
                d: int = flight[1]
                p: int = flight[2]

                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]


def test_findCheapestPrice_case_1():
    # arrange
    n: int = 4
    flights: list[list[int]] = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100],
        [1, 3, 600],
        [2, 3, 200],
    ]
    src: int = 0
    dst: int = 3
    k: int = 1
    expected: int = 700

    # act
    solution = Solution()
    actual: int = solution.findCheapestPrice(n, flights, src, dst, k)

    # assert
    assert expected == actual


def test_findCheapestPrice_case_2():
    # arrange
    n: int = 3
    flights: list[list[int]] = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src: int = 0
    dst: int = 2
    k: int = 1
    expected: int = 200

    # act
    solution = Solution()
    actual: int = solution.findCheapestPrice(n, flights, src, dst, k)

    # assert
    assert expected == actual


def test_findCheapestPrice_case_3():
    # arrange
    n: int = 3
    flights: list[list[int]] = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src: int = 0
    dst: int = 2
    k: int = 0
    expected: int = 500

    # act
    solution = Solution()
    actual: int = solution.findCheapestPrice(n, flights, src, dst, k)

    # assert
    assert expected == actual
