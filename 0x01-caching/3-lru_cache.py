#!/usr/bin/env python3
"""class LRUCache inherits from BaseCaching"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Inherits from BaseCaching

    Methods:
        put(key, item):
            adds an item to the cache_data dictionary
            if number of items in cache_data is higher than MAX.ITEMS
            discard least recently used item(LRU algorithm)
            Print DISCARD: with the key discarded,
            followed by new line
        get(key):
            return the value linked to a key
            If key is None return None
    """
    def __init__(self):
        """initiaizes the cache with OrderedDict
        to maintain access order"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds item to cache_data dictionary
        Parameter:
            key: associated with item in cache_data
            item: value to be added into cache_data
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieves value associated with key
        Parameter:
            key: associated with item
        Returns:
            Item associated with key,
            Or None if key is None
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
