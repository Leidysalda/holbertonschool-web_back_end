#!/usr/bin/python3
"""Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class inherits from BaseCaching
    use self.cache_data - dictionary from the parent class
    BaseCaching
    """

    def put(self, key, item):
        """put"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
