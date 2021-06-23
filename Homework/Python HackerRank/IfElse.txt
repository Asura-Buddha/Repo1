#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n > 20 or (n > 1 and n < 6):
        print("Not Weird")
    else:
        print("Weird")
