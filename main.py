##
# WOLF CU SD-Card Data Reader
# Description:
# Author: David Rozenbeek

import sys, getopt, os
from numpy import *

file = "Test_Data/D_00032"

def read_data():
    f = open(file, "rb")
    st = os.stat(file)
    block = f.read(st.st_size)
    print(block)
    str = ""
    count = 8
    for ch in block:
        str += hex(ch)[2:].zfill(2).upper()
        count = count - 1
        if count == 0:
            str += '\n'
            count = 8
    print(str)


def count_packages():
    pass


def present_results():
    pass


def main():

    print("------------ WOLF CU SD-CARD Data reader ------------")

    # TODO: Import files and store data
    read_data()

    # TODO: Count packets
    count_packages()

    # TODO: Present results
    present_results()


main()
