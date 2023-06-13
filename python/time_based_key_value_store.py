from typing import Tuple


class TimeMap:
    def __init__(self):
        self.store: dict[str, list[Tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        result: str = ""
        if key in self.store:
            l: int = 0
            r: int = len(self.store[key]) - 1
            arr: list[Tuple[str, int]] = self.store[key]
            while l <= r:
                mid: int = (l + r) // 2
                if timestamp == arr[mid][1]:
                    return arr[mid][0]
                elif timestamp > arr[mid][1]:
                    result = arr[mid][0]
                    l = mid + 1
                else:
                    if mid > 0:
                        r = mid - 1
                    else:
                        break

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
