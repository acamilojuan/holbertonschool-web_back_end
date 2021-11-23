#!/usr/bin/env python3
""" Basic annotations - Complex types - string and int/float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function to create a tuple"""
    return (k, v ** 2)
