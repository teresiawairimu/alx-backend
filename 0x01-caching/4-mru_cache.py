#!/usr/bin/env python3
"""Inherits from BaseCaching and is a caching system"""

from collections import OrderedDict
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """Inherits from BaseCaching and uses MRU algorithm
    Methods:
        put(key, item):
            Adds an item to the cache_data
            most recently used item is discarded 
            when cache_data's length exceeds MAX_ITEMS
        get(key):
            Retrieves the value associated with the key
    """
    def __init__(self):
        """Initializes the cache using OrderedDict
        to maintain access to the order"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds item to the cache_data dictionary
        Parameters:
            key: associated with item
            item: value to be added
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                most_recent = next(reversed(self.cache_data))
                del self.cache_data[most_recent]
                print(f"DISCARD: {most_recent}")

    def get(self, key):
        """Retrieves item from cache_data dictionary
        Parameters:
            key: associated with the value
        Returns:
            the values associated with the key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
