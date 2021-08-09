#!/usr/bin/pyhton3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class inherited from BaseCaching"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.new_dic{}

    def put(self, key, item):
        """put"""
        if key is None and item is None:
            return

            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f"DISCARD:{}\n", key)

    def get(self, key):
        """get"""
        if key is None:
            return None
        return self.cache_data.get(key)
