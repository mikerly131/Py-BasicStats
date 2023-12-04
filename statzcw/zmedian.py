"""
Module for calculating the median number from a list of numbers
"""
from statzcw import zcount


def zmedian(zlist: list) -> float:

    # Get list length, need to know if odd or even
    list_len = zcount.zcount(zlist)
    l = int(list_len)

    # Sort so we can find the middle value number of the list of numbers
    sort_list = sorted(zlist, reverse=False)
    print(list_len)
    print(sort_list)

    # If the list is an odd number of elements long, get the middle of it
    # / division as int will give index to middle of list
    if l % 2 == 1:
        middle = int((l / 2))
        zmedian = zlist[middle]
    else:
        # get the middle two numbers of the list, add together and divide by 2
        mid_1 = int((l / 2))
        mid_2 = int((l / 2) - 1)
        zmedian = (zlist[mid_1] + zlist[mid_2]) / 2.0

    return zmedian


