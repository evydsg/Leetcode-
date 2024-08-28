class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    # Remove node from the list
    def remove(self, node):
        prev, next_node = node.prev, node.next
        prev.next, next_node.prev = next_node, prev

    # Insert node at the right (most recent position)
    def insert(self, node):
        prev, next_node = self.right.prev, self.right
        prev.next = node
        node.prev, node.next = prev, next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove from the list and delete the LRU from the hashmap
            least_recent_used = self.left.next
            self.remove(least_recent_used)
            del self.cache[least_recent_used.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)