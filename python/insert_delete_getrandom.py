import random


class RandomizedSet:
    def __init__(self):
        self.map: dict[int, int] = dict()
        self.values: list[int] = list()

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.values.append(val)
        self.map[val] = len(self.values) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        # lastIndex: int = len(self.values) - 1
        index = self.map.get(val)
        lastValue: int = self.values[-1]
        self.values[-1] = val
        self.values[index] = lastValue
        self.map[lastValue] = index
        self.values.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


def test_RandomizedSet_case_1():
    randomizedSet: RandomizedSet = RandomizedSet()
    assert randomizedSet.insert(1)
    assert randomizedSet.remove(2) == False
    assert randomizedSet.insert(2)
    randomizedSet.getRandom()
    assert randomizedSet.remove(1)
    assert randomizedSet.insert(2) == False
    randomizedSet.getRandom()
