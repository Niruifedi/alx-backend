#!/usr/bin/env python3

"""
LIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Lifo cache inherits from the base caching class
    """
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Method adds an item to the cache and pops the last item off the cache
        """
        if key and item:
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.keys[-2]))
            del self.cache_data[self.keys[-2]]
            self.keys.pop(-2)

    def get(self, key):
        """
        get an item in the cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
