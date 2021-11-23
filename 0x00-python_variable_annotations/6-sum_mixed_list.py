#!/usr/bin/env python3
""" Basic annotations - Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Function sum_mixed_list which takes a list """
    return sum(mxd_lst)
