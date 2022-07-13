#!/usr/bin/env python3
""" BaseCaching module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """a new class inherited from base class"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """add an item in key-value pair to the cache"""
        if len(self.cache_data) == BaseCaching.MAX_ITEMS\
           and key not in self.cache_data:
            pop_value = self.queue.pop(-1)
            self.cache_data.pop(pop_value)
            print("DISCARD: {}".format(pop_value))
        if key and item:
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """get an item by key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
