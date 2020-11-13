#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
from pip._vendor.distlib.compat import raw_input


def solve(s):
    s = list(s)
    for i in range(len(s) - 1):
        if s[0].islower():
            s[i] = s[i].upper()

        if s[i].isspace():
            if s[i + 1].islower():
                s[i + 1] = s[i+1].upper()

    s = ''.join(s)
    print(s)
    return s


if __name__ == '__main__':
    s = raw_input()

    result = solve(s)
