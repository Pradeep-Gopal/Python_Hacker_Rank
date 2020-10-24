#!/bin/python

import math
import os
import random
import re
import sys

from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input().strip())

    if n % 2 == 1:
        print("Weird")
    if n % 2 != 1 and n in range(2, 5):
        print("Not Weird")
    if n % 2 != 1 and n in range(6, 21):
        print("Weird")
    if n % 2 != 1 and n > 20:
        print("Not Weird")
