#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""New Fibonacci sequence generator"""


def xfibo(count):
    """Produces number of Fibonacci numbers as specified.

    Args:
        count(int): The number of Fibonacci numbers to return.

    Returns: A Fibonacci sequence starting with 0.

    Examples:

        >>> for i in xfibo(5):
                print i
        0
        1
        1
        2
        3
    """
    iteration = 0
    lastnum, curnum = 0, 1
    while iteration < count:
        yield lastnum
        lastnum, curnum = curnum, lastnum + curnum
        iteration += 1
