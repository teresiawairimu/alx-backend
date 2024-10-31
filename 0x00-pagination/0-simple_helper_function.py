#!/usr/bin/env python3
"""Takes two integer arguments and returns a tuple of size two"""


def index_range(page, page_size):
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
