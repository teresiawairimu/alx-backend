#!/usr/bin/python3
"""Class that inherits from BaseCaching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system
    without size limits.

    Methods:
        put(key, item):
            Adds an item to the cache with the specified key.
            If key or item is None, it does nothing.
        get(key):
            Retrieves an item from the cache by key. Returns None if the key
            is None pr if the key is not found in the cache.
    """
    def put(self, key, item):
        """Adds an item to the cache with the specified key.
        If either key or item is None, this method does not perform any
        action.
        Parameters:
            key: The key to associate with the item.
            item: the item to be stored in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache by key
        if the key is None, or not found, returns None.
        Parameters:
            key: THe key to look up in the cache.
        Returns:
            The item associated with the key, or None if the key is not found
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
