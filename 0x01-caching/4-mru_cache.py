#!/usr/bin/env python3

"""
MRU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Cache
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_data_list:
                self.cache_data_list.append(key)
            else:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed = self.cache_data_list.pop(-2)
                del self.cache_data[removed]
                print("DISCARD: {}".format(removed))

    def get(self, key):
        """
        Get an item by key
        """
        if key:
            if key in self.cache_data:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
                return self.cache_data[key]
        return None
