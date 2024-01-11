class StockSpanner:
    def __init__(self):
        self.stack: list[tuple[int, int]] = list()

    def next(self, price: int) -> int:
        span: int = 1
        while len(self.stack) > 0 and price >= self.stack[-1][0]:
            _, s = self.stack.pop()
            span += s

        self.stack.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
def test_stock_spanner_case_1():
    stockSpanner: StockSpanner = StockSpanner()
    assert stockSpanner.next(100) == 1
    assert stockSpanner.next(80) == 1
    assert stockSpanner.next(60) == 1
    assert stockSpanner.next(70) == 2
    assert stockSpanner.next(60) == 1
    assert stockSpanner.next(75) == 4
    assert stockSpanner.next(85) == 6


def test_stock_spanner_case_2():
    stockSpanner: StockSpanner = StockSpanner()
    assert stockSpanner.next(28) == 1
    assert stockSpanner.next(14) == 1
    assert stockSpanner.next(28) == 3
    assert stockSpanner.next(35) == 4
    assert stockSpanner.next(46) == 5
