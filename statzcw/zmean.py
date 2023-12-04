"""
Module to calculate the mean of a list of numbers
"""
from statzcw import zcount


def zmean(zlist: list) -> float:
    z_count = zcount.zcount(zlist)
    zsum = sum(zlist)
    zmean = zsum / z_count
    return zmean
