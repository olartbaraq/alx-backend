#!/usr/bin/env python3

"""Simple pagination implementation"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    """
    end_index = page * page_size

    start_index = end_index - page_size

    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
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
        """paginating the datasets"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        self.dataset()

        if self.__dataset is None:
            return []

        indx_range = index_range(page, page_size)
        data = self.__dataset[indx_range[0]:indx_range[1]]
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """provides the datasets in key-value pair"""
        data_set = self.__dataset
        len_set = len(data_set) if data_set else 0
        total_pages = math.ceil(len_set / page_size) if data_set else 0

        if not self.get_page(page, page_size):
            page_size = 0
        else:
            page_size = len(self.get_page(page, page_size))

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        dict_file = {}
        dict_file['page_size'] = page_size
        dict_file['page'] = page
        dict_file['data'] = self.get_page(page, page_size)
        dict_file['next_page'] = next_page
        dict_file['prev_page'] = prev_page
        dict_file['total_pages'] = total_pages

        return dict_file
