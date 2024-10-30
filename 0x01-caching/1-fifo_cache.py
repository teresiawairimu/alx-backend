#!/usr/bin/python3
"""Class FiFOCache inherits from BaseCaching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Inherits from BaseCaching and implements a basic
    caching system using FIFO to discard an item if
    cache_data is higher than BaseCaching.MAX_ITEMS

    Methods:
        put(key, item):
            Adds an item to the cahce with specified key
            if key or item is None, do nothing
            if number of items in cache_data is higher than
            BaseCaching.MAX_ITEMS then discard first item
            Print DISCARD with the key discarded and a new line
        get(key):
            return the value in cache_data linked to key
            if key is None return None
    """
    def put(self, key, item):
        """adds an item to the cache

        Parameters:
            key: The key associated with the item
            item: the item stored in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """returns the value in cache_data linked to a key

        Parameters:
            key: the keu to look up in the cache.

        Returns:
            the item associated with the key, or none if not found
        """
        if key is not None:
            return self.cache_data.get[key]
        else:
            return None
