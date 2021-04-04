#!/usr/bin/env python3
"""Chad Tricks!!"""
######clear screen from chad
from subprocess import call
from os import name as osname
#####print 1by1 dependencies
import sys, time

def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print

def clear():
    # check and make call for specific operating system
    call('clear' if osname =='posix' else 'cls')
