from collections import defaultdict


class TimeMap:
    def __init__(self):
        self._store: dict[str, list[tuple[str, int]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """time complexity: O(1)"""
        self._store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        """time complexity: O(lon g)"""
        data: list[tuple[str, int]] = self._store.get(key, [])
        l: int = 0
        r: int = len(data) - 1
        result: str = ""
        while l <= r:
            mid: int = (l + r) // 2
            if data[mid][1] <= timestamp:
                result = data[mid][0]
                l = mid + 1
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
