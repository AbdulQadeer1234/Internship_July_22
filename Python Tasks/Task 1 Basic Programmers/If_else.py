#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2!=0):
        print("Weird")
    if n in range(2,6) and (n%2==0):
        print("Not Weird") 
    if n in range(6,21) and (n%2==0):
        print("Weird")
    if (n%2==0) and (n>20):
        print("Not Weird")
