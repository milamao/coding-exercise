class Node:
    def __init__(self, k):
        self.prev = None
        self.next = None
        self.key = k

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key => (value, freq, node)
        self.freqs = {}  # freq => (head, tail)
        self.min_freq = float('INF')

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # remove
        value, freq, node = self.remove(key)
        # add
        self.add(key, value, freq + 1, node)
        # update min frequency
        if self.min_freq not in self.freqs:
            self.min_freq += 1

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.cache:
            if len(self.cache) == self.capacity:
                head, tail = self.freqs[self.min_freq]
                lfu_key = head.next.key
                self.remove(lfu_key)
            self.add(key, value, 1, Node(key))
            self.min_freq = 1
        else:
            old_value, freq, node = self.remove(key)
            self.add(key, value, freq + 1, node)
            if self.min_freq not in self.freqs:
                self.min_freq += 1

    def remove(self, key):
        value, freq, node = self.cache.get(key)
        self.cache.pop(key)

        head, tail = self.freqs[freq]

        if node.next:
            node.next.prev = node.prev
            node.prev.next = node.next
        else:
            tail = node.prev
            node.prev.next = None
        node.prev = None
        node.next = None

        if head == tail:
            self.freqs.pop(freq)
        else:
            self.freqs[freq] = (head, tail)

        return value, freq, node

    def add(self, key, value, freq, node):
        if freq in self.freqs:
            head, tail = self.freqs[freq]
            tail.next = node
            node.prev = tail
            tail = tail.next
        else:
            head = Node(None)
            head.next = node
            node.prev = head
            tail = node
        self.freqs[freq] = (head, tail)

        self.cache[key] = (value, freq, node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)