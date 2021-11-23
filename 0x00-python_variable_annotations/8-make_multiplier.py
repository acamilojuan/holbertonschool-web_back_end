#!/usr/bin/env python3
""" Basic annotations - Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function make_multiplier that takes a float multiplier """
    def multiplication(numb):
        return numb * multiplier
    return multiplication
