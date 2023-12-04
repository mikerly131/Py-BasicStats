"""
Module to calculate the sample variance of numbers in a list of numbers
Variance measures hor far data is spread out, which is the average of the squared differences from the mean
"""
from statzcw import zcount
import math


def zvariance(zlist: list) -> float:

    count = zcount.zcount(zlist)

    # Don't subtract one yet, the mean for variance is still based on pop count, had to look that up
    v_mean = sum(zlist) / count

    # Get deviations by subtracting each number from the v_mean just calculated, store in list
    deviations = []
    for num in zlist:
        sq_diff = abs(num - v_mean) ** 2
        deviations.append(sq_diff)

    # For variance, look at SAMPLE not POPULATION, so we subtract 1 from pop count (just the rules)
    v_count = count - 1
    # Now to get variance we find the average (mean) of deviations for the SAMPLE
    zvar_sq = sum(deviations) / v_count
    # zvar = math.sqrt(zvar_sq)

    return zvar_sq
