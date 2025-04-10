from typing import Optional


class RingBuffer:
    def __init__(self, size: int):
        self._buffer: list[Optional[int]] = [None] * size
        self._head: int = 0  # For reading
        self._tail: int = 0  # For writing
        self._full: bool = False
        self._size: int = size

    def enqueue(self, value: int) -> bool:
        if self._full:
            self._head = (self._head + 1) % self._size
        self._buffer[self._tail] = value
        self._tail = (self._tail + 1) % self._size
        if self._head == self._tail:
            self._full = True

    def dequeu(self) -> Optional[int]:
        if self.is_empty():
            return None
        result: int = self._buffer[self._head]
        self._buffer[self._head] = None  # Clear the buffer
        self._head = (self._head + 1) % self._size
        self._full = False
        return result

    def is_empty(self) -> bool:
        return not self._full and self._head == self._tail

    def print_ring_buffer(self) -> None:
        for i in range(len(self._buffer)):
            print(f"{self._buffer[i]} ", end="")
        print(f"| head: {self._head}, tail: {self._tail}, is full: {self._full}")


if __name__ == "__main__":
    rb: RingBuffer = RingBuffer(5)
    rb.enqueue(10)
    rb.enqueue(20)
    rb.enqueue(30)
    rb.enqueue(40)
    rb.enqueue(50)

    # Overwrite oldest data
    rb.enqueue(60)

    rb.print_ring_buffer()

    # Dequeue elements
    value: int = rb.dequeu()
    print(f"Dequeued: {value}")
    rb.print_ring_buffer()
    rb.dequeu()
    rb.print_ring_buffer()
    rb.dequeu()
    rb.print_ring_buffer()
    rb.dequeu()
    rb.print_ring_buffer()
    rb.dequeu()
    rb.print_ring_buffer()
    rb.dequeu()
    rb.print_ring_buffer()
