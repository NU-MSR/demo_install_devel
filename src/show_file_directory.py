#!/usr/bin/env python
import os

def main():
    # all we want to do in here is show the location of the executable:
    print "Path of the executable itself is = ", os.path.abspath(__file__)
    return

if __name__ == '__main__':
    main()
