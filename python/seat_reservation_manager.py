import heapq


class SeatManager:

    def __init__(self, n: int):
        """time complexity: O(n), space complexity: O(n)"""
        self._min_heap: list[int] = [i for i in range(1, n + 1)]
        self._reversed_seats: set[int] = set()
        heapq.heapify(self._min_heap)

    def reserve(self) -> int:
        """time complexity: O(logn)"""
        if len(self._min_heap) > 0:
            seat_number: int = heapq.heappop(self._min_heap)
            self._reversed_seats.add(seat_number)
            return seat_number
        return 0

    def unreserve(self, seatNumber: int) -> None:
        """time complexity: O(logn)"""
        if seatNumber not in self._reversed_seats:
            return
        heapq.heappush(self._min_heap, seatNumber)
        self._reversed_seats.remove(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
def test_SeatManager_case_1():
    """This is a test case for SeatManager"""
    seatManager: SeatManager = SeatManager(5)  # Initializes a SeatManager with 5 seats.
    assert (
        1 == seatManager.reserve()
    )  # All seats are available, so return the lowest numbered seat, which is 1.
    assert (
        2 == seatManager.reserve()
    )  # The available seats are [2,3,4,5], so return the lowest of them, which is 2.
    seatManager.unreserve(
        2
    )  # Unreserve seat 2, so now the available seats are [2,3,4,5].
    assert (
        2 == seatManager.reserve()
    )  # The available seats are [2,3,4,5], so return the lowest of them, which is 2.
    assert (
        3 == seatManager.reserve()
    )  # The available seats are [3,4,5], so return the lowest of them, which is 3.
    assert (
        4 == seatManager.reserve()
    )  # The available seats are [4,5], so return the lowest of them, which is 4.
    assert 5 == seatManager.reserve()  # The only available seat is seat 5, so return 5.
    seatManager.unreserve(5)  # Unreserve seat 5, so now the available seats are [5].
