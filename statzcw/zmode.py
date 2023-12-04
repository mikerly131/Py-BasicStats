"""
Module to calculate and return a mode.
Supposed to return a float for the function, but declaring it will mean I have to force a value when no mode
-> float is removed for now from method declaration
"""
from statzcw import zcount


def zmode(zlist: list):

    # Turn this into dcs at some point
    num_count = {}
    for num in zlist:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # Sort dictionary by occurrences of keys, setup list of keys and values
    num_sort_count = dict(sorted(num_count.items(), key=lambda x:x[1], reverse=True))
    num_keys = list(num_sort_count.keys())
    num_values = list(num_sort_count.values())
    # Get a count of numbers in zlist
    num_count = zcount.zcount(zlist)

    # WHy won't git hub take my updates
    # Conditional: If all value counts from zlist are equal then no mode,
    if num_count == 1:
        z_mode = num_keys[0]
        return z_mode / 1.0
    elif sum(num_values) / (num_values[0] * num_count) == 1:
        print("There is no mode.")
    # Elif the count of value 0 is not equal to count of value 1, value 0 is the mode
    elif num_values[0] != num_values[1]:
        z_mode = num_keys[0]
        return z_mode / 1.0
    # Else all values with equal count are the mode
    else:
        # Turn this into an lcs at some point
        mode_list = []
        z_mode = num_values[0]
        for key in num_keys:
            test_num = num_sort_count[key]
            if z_mode == test_num:
                mode_list.append(key)
        return mode_list





