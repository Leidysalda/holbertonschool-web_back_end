#!/usr/bin/env python3
"""Complex types - functions

"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function make_multiplier that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier.
    """

    def new_func(fn: float) -> float:
        """
        New argument for multiply by multiplier
        """
        return float(fn * multiplier)

    return new_func
