#!/usr/bin/env python3
"""class LIFOCache inherits from BaseCaching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from Basecaching and is a caching system
    Methods:
        put(key, item):
            Adds the item to the cache_data dictionary
        get(key):
            Retrieves item from cache_data dictionary
    """
    def put(self, key, item):
        """Adds item to dictionary
        Parameters:
            key: associated with item
            item: added to the cache_data dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_item = self.cache_data.popitem()
                print(last_item[0])

    def get(self, key):
        """Retrieves item associated with a key
        Parameter:
            key: associated with item
        Returns:
            item associated with key, None if key is not found
        """
        if key is not None:
            self.cache_data[key]
