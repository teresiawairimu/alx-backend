#!/usr/bin/env python3

import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size two containing a start index and
    end index corresponding to the range of indexes to return in
    a list for those particular pagination parameters

    Parameters:
        page (int):
            The page number
        page_size (int):
            THe number of items that should appear on each page
    Returns:
        A tuple of size two.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments
        return the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index >= len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """Returns a dictionary containing key-value pairs
        Returns:
            page_size: the length of returned dataset page
            page: current page number
            data: dataset page
            next_page: number of the next page, None if no next page
            prev_page: number of previous page, None if no previous page
            total_pages: the total number of pages in the dataset
        """
        data = self.get_page(page, page_size)
        page_size = len(data)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }