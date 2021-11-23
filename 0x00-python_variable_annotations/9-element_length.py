#!/usr/bin/env python3
""" Basic annotations - duck type an iterable object """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function that return values with types """
    return [(i, len(i)) for i in lst]
