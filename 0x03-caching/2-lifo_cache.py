#!/usr/bin/pyhton3
"""FIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class inherits from BaseCaching
    use self.cache_data - dictionary from the parent class
    BaseCaching
    """

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.list_name = []

    def put(self, key, item):
        """put method"""
        if key is None and item is None:
            return

        self.cache_data[key] = item

        if key not in self.list_name:
            self.list_name.append(key)
        else:
            if self.list_name[-1] != key:
                self.list_name.remove(key)
                self.list_name.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.list_name[-2]
            print(f"DISCARD:{discard}")
            del self.cache_data[discard]
            self.list_name.pop(-2)

    def get(self, key):
        """get method"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
