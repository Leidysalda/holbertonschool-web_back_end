#!/usr/bin/python3
"""Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def put(self, key, item):
        """Put method"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gget method"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
