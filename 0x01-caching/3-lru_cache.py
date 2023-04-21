#!/usr/bin/env python3

"""
LRU Caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        add an item to the cache
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_data_list:
                self.cache_data_list.append(key)
            else:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removed = self.cache_data_list.pop(0)
            del self.cache_data[removed]
            print("DISCARD: {}".format(removed))

    def get(self, key):
        """
        get an item in the cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
