from collections import deque


class AnimalShelf:

    def __init__(self):
        self._queues: tuple[deque[int], deque[int]] = (
            deque(),
            deque(),
        )

    def enqueue(self, animal: list[int]) -> None:
        """time complexity: O(1)"""
        n, t = animal
        self._queues[t].append(n)

    def dequeueAny(self) -> list[int]:
        """time complexity: O(1)"""
        if len(self._queues[0]) == 0:
            return self.dequeueDog()
        if len(self._queues[1]) == 0:
            return self.dequeueCat()
        if self._queues[0][0] < self._queues[1][0]:
            return self.dequeueCat()
        return self.dequeueDog()

    def dequeueDog(self) -> list[int]:
        """time complexity: O(1)"""
        return [-1, -1] if len(self._queues[1]) == 0 else [self._queues[1].popleft(), 1]

    def dequeueCat(self) -> list[int]:
        """time complexity: O(1)"""
        return [-1, -1] if len(self._queues[0]) == 0 else [self._queues[0].popleft(), 0]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()


def test_animalshelf_case_1():
    animalShelf = AnimalShelf()
    animalShelf.enqueue([0, 0])
    animalShelf.enqueue([1, 0])
    actual1 = animalShelf.dequeueCat()
    actual2 = animalShelf.dequeueDog()
    actual3 = animalShelf.dequeueAny()

    assert actual1 == [0, 0]
    assert actual2 == [-1, -1]
    assert actual3 == [1, 0]


def test_animalshelf_case_2():
    animalShelf = AnimalShelf()
    animalShelf.enqueue([0, 0])
    animalShelf.enqueue([1, 0])
    animalShelf.enqueue([2, 1])
    actual1 = animalShelf.dequeueDog()
    actual2 = animalShelf.dequeueCat()
    actual3 = animalShelf.dequeueAny()

    assert actual1 == [2, 1]
    assert actual2 == [0, 0]
    assert actual3 == [1, 0]
