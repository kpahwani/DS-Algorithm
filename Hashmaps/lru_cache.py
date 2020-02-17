"""
    The task is to design and implement methods of an LRU cache. The class has two methods get and set which are
    defined as follows. get(x)   : Gets the value of the key x if the key exists in the cache otherwise returns -1
    set(x,y) : inserts the value if the key x is not already present. If the cache reaches its capacity it should
    invalidate the least recently used item before inserting the new item. In the constructor of the class the size of
    the cache should be intitialized.
"""
from collections import deque


class LruCache:
    def __init__(self, size):
        self.map = {}
        self.deque = deque(maxlen=size)

    def set(self, key, value):
        if key in self.deque:
            self.deque.remove(key)
        self.deque.append(key)
        self.map[key] = value

    def get(self, key):
        if key in self.deque:
            self.deque.append(self.deque.pop())
            return self.map[key]

        return -1


cache = LruCache(2)
cache.set(1, 2)
cache.set(2, 3)
cache.set(1, 5)
cache.set(4, 5)
cache.set(6, 7)
print(cache.get(4))
print(cache.get(1))



