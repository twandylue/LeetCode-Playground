from typing import Optional


class ListNode:
    def __init__(
        self,
        key: int = 0,
        value: int = 0,
        next_node: Optional["ListNode"] = None,
        prev: Optional["ListNode"] = None,
    ):
        self.key: int = key
        self.value: int = value
        self.next: Optional[ListNode] = next_node
        self.prev: Optional[ListNode] = prev


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity: int = capacity
        self._head: Optional[ListNode] = ListNode()
        self._tail: Optional[ListNode] = ListNode()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._node_map: dict[int, ListNode] = {}

    def _insert_after_head(self, node: ListNode) -> None:
        """time complexity: O(1)"""
        next_node: ListNode = self._head.next
        next_node.prev = node
        self._head.next = node
        node.prev = self._head
        node.next = next_node

    def _pop_node(self, node: ListNode) -> Optional[ListNode]:
        """time complexity: O(1)"""
        next_node: ListNode = node.next
        prev_node: ListNode = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        return node

    def get(self, key: int) -> int:
        """time complexity: O(1)"""
        if key not in self._node_map:
            return -1
        node: ListNode = self._node_map[key]
        iso_node: Optional[ListNode] = self._pop_node(node)
        self._insert_after_head(iso_node)
        return iso_node.value

    def put(self, key: int, value: int) -> None:
        """time complexity: O(1)"""
        if key not in self._node_map:
            if len(self._node_map) >= self._capacity:
                least_node: ListNode = self._tail.prev
                iso_least_node: ListNode = self._pop_node(least_node)
                del self._node_map[iso_least_node.key]
            new_node: ListNode = ListNode(key, value)
            self._node_map[key] = new_node
            self._insert_after_head(new_node)
            return
        node: ListNode = self._node_map[key]
        iso_node: ListNode = self._pop_node(node)
        iso_node.value = value
        self._insert_after_head(iso_node)


def test_lru_case1():
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    lruCache = LRUCache(2)
    lruCache.put(1, 1)  # cache is {1=1}
    lruCache.put(2, 2)  # cache is {1=1, 2=2}
    actual1 = lruCache.get(1)  # return 1
    lruCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    actual2 = lruCache.get(2)  # returns -1 (not found)
    lruCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    actual3 = lruCache.get(1)  # return -1 (not found)
    actual4 = lruCache.get(3)  # return 3
    actual5 = lruCache.get(4)  # return 4

    assert actual1 == 1
    assert actual2 == -1
    assert actual3 == -1
    assert actual4 == 3
    assert actual5 == 4
