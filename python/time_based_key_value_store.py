from typing import Tuple


class TimeMap:
    def __init__(self):
        self.store: dict[str, list[tuple[str, int]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        pos: int = self.binarySearch(self.store[key], timestamp)
        if pos == -1:
            return ""

        return self.store[key][pos][0]

    def binarySearch(self, times: list[tuple[str, int]], time: int) -> int:
        l: int = 0
        r: int = len(times) - 1
        result: int = -1
        while l <= r:
            mid: int = (l + r) // 2
            if times[mid][1] == time:
                return mid
            if times[mid][1] < time:
                l = mid + 1
                result = mid
            else:
                r = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
def test_TimeMap_case_1():
    timeMap: TimeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    assert timeMap.get("foo", 1) == "bar"
    assert timeMap.get("foo", 3) == "bar"
    timeMap.set("foo", "bar2", 4)
    assert timeMap.get("foo", 4) == "bar2"
    assert timeMap.get("foo", 5) == "bar2"
