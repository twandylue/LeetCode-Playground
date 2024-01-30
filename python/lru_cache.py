class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: ListNode
        self.next: ListNode


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.head: ListNode = ListNode(0, 0)
        self.tail: ListNode = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodeMap: dict[int, ListNode] = dict()

    def insert_after_head(self, node: ListNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def pop_node(self, node: ListNode) -> ListNode:
        node.next.prev = node.prev
        node.prev.next = node.next
        return node

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            node: ListNode = self.nodeMap[key]
            isoNode: ListNode = self.pop_node(node)
            self.insert_after_head(isoNode)
            return isoNode.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node: ListNode = self.nodeMap[key]
            isoNode: ListNode = self.pop_node(node)
            isoNode.value = value
            self.insert_after_head(isoNode)
        else:
            if self.capacity <= len(self.nodeMap):
                lastNode: ListNode = self.tail.prev
                isoNode: ListNode = self.pop_node(lastNode)
                del self.nodeMap[isoNode.key]

            newNode: ListNode = ListNode(key, value)
            self.nodeMap[key] = newNode
            self.insert_after_head(newNode)


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
