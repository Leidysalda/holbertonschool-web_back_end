#!/usr/bin/ptrhon3
"""Hypermedia pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Index range"""
    return (page - 1) * page_size, page * page_size


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

    def get_page(self, page: int=1, page_size: int=10) -> List[List]:
        """get page"""
        for pag in [page, page_size]:
            assert isinstance(pag, int) and page > 0
        self.dataset()
        r_pag = index_range(page=page, page_size=page_size)
        return self.__dataset[r_pag[0]:r_pag[1]]

    def get_hyper(self, page: int=1, page_size: int=10) -> dict:
        """takes the same arguments and returns a dictionary"""

        total_pag = len(self.dataset()) / page_size

        total_pages = math.ceil (total_pag)
        
        return {
            'page_size': page_size,
            'page': page,
            'data':  self.get_page(page, page_size),
            'next_page': page + 1 if (page + 1) <= total_pages else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': total_pages
}
