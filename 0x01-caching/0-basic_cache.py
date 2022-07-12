#!/usr/bin/env python3
""" BaseCaching module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a new class inherited from base class"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """add an item in key-value pair to the cache"""
        if key or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """get an item by key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
