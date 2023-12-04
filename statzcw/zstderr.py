"""
Module for calculating the standard error of the sample for a list of numbers
Standard error is standard deviation of sample divided by count of pop
"""
from statzcw import zstdev, zcount
import math


def zstderr(zlist: list) -> float:

    std_dev = zstdev.zstdev(zlist)
    count = zcount.zcount(zlist)

    zerr = std_dev / math.sqrt(count)

    return round(zerr, 5)