#!/bin/python

import math
import os
import random
import re
import sys

from pip._vendor.distlib.compat import raw_input
from pip._vendor.msgpack.fallback import xrange


x, y = list(map(int, input().split()))
rows = [input() for i in range(x)]

text = "".join([row[i] for i in range(y) for row in rows])

text = re.sub('([\w])[^\w]+([\w])', r'\1 \2', text)

text = re.sub('  ', ' ', text)
print(text)
