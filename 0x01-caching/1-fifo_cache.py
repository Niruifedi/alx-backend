#!/usr/bin/env python3
"""
First in First out Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Fifo cache inherits from the basecaching class
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Mehtod adds an item to the cache and pops the first item off the cache
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(list(self.cache_data.keys())[0]))
            del self.cache_data[list(self.cache_data.keys())[0]]

    def get(self, key):
        """
        get an item in the cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
