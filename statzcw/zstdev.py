"""
Module for calculating the standard deviation of the sample for a list of numbers
Standard Deviation is square root of variance of sample
"""
from statzcw import zvariance
import math


def zstdev(zlist: list) -> float:
    zvar = zvariance.zvariance(zlist)
    zstdev = math.sqrt(zvar)

    # Returning it rounded to 5 places because displays better and thats what I want
    return round(zstdev, 5)