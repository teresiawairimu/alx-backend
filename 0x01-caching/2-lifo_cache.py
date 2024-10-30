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
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """Retrieves item associated with a key
        Parameter:
            key: associated with item
        Returns:
            item associated with key, None if key is not found
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
