#!/usr/bin/python
import sys
from drunken import DrunkyMunky

if len(sys.argv) <= 1:
    drunk = 1
else:
    drunk = sys.argv[1]

DrunkyMunky.isDrunk(drunk)
