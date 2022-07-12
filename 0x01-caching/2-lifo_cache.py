#!/usr/bin/env python3
""" BaseCaching module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """a new class inherited from base class"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """add an item in key-value pair to the cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            pop_value = list(self.cache_data)[3]
            self.cache_data.pop(pop_value)
            print("DISCARD: {}".format(pop_value))

    def get(self, key):
        """get an item by key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
