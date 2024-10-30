#!/usr/bin/env python3
"""Inherits from BaseCaching"""

from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Inherits from BaseCaching and implements an LFU caching system.
    Methods:
        put(key, item):
            Adds an item to cache_data
            Discards least frequency used item
        get(key):
            retrieves item associacted with key
    """
    def __init__(self):
        """Initialize the cache_data"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = {}
        self.lru_order = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache using LFU strategy.

        Parameters:
            key: The key associated with the item.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.lru_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                least_frequent_keys = []
                for k, freq in self.frequency.items():
                    if freq == min_freq:
                        least_frequent_keys.append(k)
                lru_key = None
                for k in self.lru_order:
                    if k in least_frequent_keys:
                        lru_key = k
                        break
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.lru_order[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.lru_order[key] = True

    def get(self, key):
        """Retrieve an item associated with a key.

        Parameters:
            key: The key to look up in the cache.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.lru_order.move_to_end(key)
        return self.cache_data[key]
