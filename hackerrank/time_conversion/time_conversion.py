#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


"""original
def time_conversion(s)
    # Write your code here
    print(s)
    # s = "07:05:45AM" -> "07:05:45"
    # s = "07:05:45PM" -> "19:05:45"
    # s = "12:01:45PM" -> "12:01:45"
    # s = "12:01:45AM" -> "00:01:45"
    hour, minutes, second_and_half = s.split(':')
    seconds = second_and_half[0:2]
    half = second_and_half[2:4]
    morning = True if half.lower() == "am" else False
    if morning and int(hour) == 12:
        hour = "00"
    elif not morning and int(hour) < 12:
        hour = "{}".format(int(hour) + 12)

    return "{}:{}:{}".format(hour, minutes, seconds)
"""
def time_conversion(s):
    """
    Convert 12 hour format to 24 hour format

        * s = "07:05:45AM" -> "07:05:45"
        * s = "07:05:45PM" -> "19:05:45"
        * s = "12:01:45PM" -> "12:01:45"
        * s = "12:01:45AM" -> "00:01:45"
    :param s: 12-hour time string
    :return: 24-hour time string
    """
    hour, minutes, second_and_am_pm = s.split(':')
    seconds = second_and_am_pm[:2]
    am_pm = second_and_am_pm[2:].lower()
    if am_pm == "am":
        if int(hour) == 12:
            hour = "00"
    else: # PM
        if int(hour) < 12:
            hour = int(hour)+ 12

    return f"{hour}:{minutes}:{seconds}"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = time_conversion(s)

    fptr.write(result + '\n')

    fptr.close()
