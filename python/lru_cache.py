class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: ListNode
        self.next: ListNode


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.map: dict[int, ListNode] = {}
        self.head: ListNode = ListNode(0, 0)
        self.tail: ListNode = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            result = node.value
            node.prev.next = node.next
            node.next.prev = node.prev

            self.head.next.prev = node
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head

            return result
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            self.head.next = node
        else:
            if len(self.map) >= self.capacity:
                del_node = self.tail.prev
                del_node.prev.next = self.tail
                self.tail.prev = del_node.prev
                del self.map[del_node.key]

            new_node = ListNode(key, value)
            self.map[new_node.key] = new_node
            self.head.next.prev = new_node
            new_node.next = self.head.next
            self.head.next = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
actual1 = lRUCache.get(1)  # return 1
lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
actual2 = lRUCache.get(2)  # returns -1 (not found)
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
actual3 = lRUCache.get(1)  # return -1 (not found)
actual4 = lRUCache.get(3)  # return 3
actual5 = lRUCache.get(4)  # return 4


def test_case1():
    assert actual1 == 1
    assert actual2 == -1
    assert actual3 == -1
    assert actual4 == 3
    assert actual5 == 4
