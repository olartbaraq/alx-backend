#!/usr/bin/env python3
""" BaseCaching module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """a new class inherited from base class"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """add an item in key-value pair to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                pop_value = self.queue.pop(0)
                self.cache_data.pop(pop_value)
                print("DISCARD: {}".format(pop_value))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """get an item by key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data[key]
        if item is not None:
            self.mv_last_list(key)
        return item

    def mv_last_list(self, item):
        """ Moves element to last idx of list """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def get_first_list(array):
        """ Get first element of list or None """
        if array:
            return array[0]
        return None
