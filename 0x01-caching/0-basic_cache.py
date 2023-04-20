#!/usr/bin/env python3
"""
Basic Dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cacheinherits from the base caching class
    """
    def put(self, key, item):
        """
        put an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        get an item in the cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
