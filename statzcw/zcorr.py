"""
Module for calculating correlation between two lists of numbers
Correlation is the covriance between the two lists / stdev of each list multiplied together
"""
from statzcw import zmean, zcount, zstdev


def zcorr(xlist: list, ylist: list) -> float:

    # Determine covariance, and std dev for each list
    co_var = cov(xlist, ylist)
    std_dev_x = zstdev.zstdev(xlist)
    std_dev_y = zstdev.zstdev(ylist)

    # Correlation is covariance / (std dev x * std dev y)
    correlation = co_var / (std_dev_x * std_dev_y)
    return round(correlation, 5)


def cov(x: list, y: list):

    # Lists must be equal length for covraiance to apply
    if len(x) != len(y):
        return

    # Get the mean of each list
    x_mean = zmean.zmean(x)
    y_mean = zmean.zmean(y)

    # Set sum to 0, and count to number of items in a list
    sum = 0
    count = int(zcount.zcount(x))

    # Loop: for each item in the list, calculate the difference from mean multiplied together, add to sum
    for i in range(0, count):
        sum += ((x[i] - x_mean) * (y[i] - y_mean))

    # Divide the sum by count - 1
    return sum/(count-1)
