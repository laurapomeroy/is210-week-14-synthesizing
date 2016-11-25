#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Returns a list comprehension"""

import task_01


def fibo(count):
    """Counts the total number of Fibonacci

    Args:
        count(int): The total number of Fibonacci numbers to return.

    Returns: a list comprehension.

    Examples:

        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [num for num in task_01.xfibo(count)]
