##
# WOLF CU SD-Card Data Reader
# Description:
# Author: David Rozenbeek

import sys, getopt, os
from numpy import *

debug = True

#Constants
PACKET_SIZE = 8                                                     #Length of each packets in bytes

file = "Test_Data/D_00032"
packetList = []


def read_data():
    if debug:
        print('Start reading in data')
        print('Opening File:', file)

    f = open(file, "rb")                                            #Open file
    st = os.stat(file)                                              #Get file size

    if debug: print('File Size: ', st.st_size)

    block = f.read(st.st_size)                                      #Read in blocks of data

    str = ""
    count = PACKET_SIZE
    packet = ''
    #TODO: Fix formtting if data is not align correctly
    for ch in block:
        packet += hex(ch)[2:].zfill(2).upper()
        count -= 1
        if count == 0:
            str += packet
            packetList.append(packet)
            str += '\n'
            packet = ''
            count = PACKET_SIZE

    if debug:
        print('Number of packets read in: ', packetList.__len__())
        print('Data read in done')
        print('--------------------------------------')

def count_packages():
    if debug:
        print('Start counting packets')

    nrADC = 0
    nrACC = 0
    nrGyro = 0
    nrTime = 0

    for packet in packetList:
        if packet[:4] == '01AD':
            nrADC += 1
        elif packet[:4] == '02AD':
            nrADC += 1
        elif packet[:4] == '03AD':
            nrADC += 1
        elif packet[:3] == '2AC':
            nrACC += 1
        elif packet[:3] == '3AC':
            nrACC += 1
        elif packet[:4] == '0C0C':
            nrGyro += 1
        elif packet[:4] == '0C0B':
            nrGyro += 1
        elif packet[:4] == '4006':
            nrTime+= 1
        else:
            print('ERROR! Mismatched packet!:', packet)

    if debug:
        print('Number of matched ADC packets:  ', nrADC)
        print('Number of matched ACC packets:  ', nrACC)
        print('Number of matched Gyro packets: ', nrGyro)
        print('Number of matched Time packets: ', nrTime)
        tot = nrADC + nrACC + nrGyro + nrTime
        print('Total number of matched packets: ', tot)
        print('--------------------------------------')




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
