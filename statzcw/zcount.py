"""
Module to count the numbers in a list of numbers
"""


def zcount(zlist: list) -> float:
    zcounter = 0.0
    for number in zlist:
        zcounter += 1
    return zcounter