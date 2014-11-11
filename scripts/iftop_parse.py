#!/usr/bin/env python

import numpy
import os, sys
import re
import matplotlib.pyplot as pplt
from pylab import *

# absolute path
project_root="/Users/jinlianw/Work/plots.git/"

# result directory
result_dir="data/"

iftop_files = [
    "netio.log"
]

runtime = [
469
]

label_list = [
    "bandwidth 400Mbps",
    "bandwidth 800Mbps",
    "SSP, slack = 2"
]

def read_bw_list(netio_file):
    bw_list = []
    netio_obj = open(netio_file, 'r')
#    netio_str = '^Total send rate:\s+(?P<bw>([0-9]|\.)*[0-9]+)(?P<unit>K|M|'')b'
    netio_str = '^Total send rate:\s+([0-9]|\.)*[0-9]+(K|M|'')b\s+(?P<bw>([0-9]|\.)*[0-9]+)(?P<unit>K|M|'')b'
    netio_pattern = re.compile(netio_str)
    line = netio_obj.readline()
    while line != "":
        match_obj = netio_pattern.match(line)
        if match_obj:
            bw = float(match_obj.group('bw'))
            if match_obj.group('unit') == '':
                bw /= 1024*1024
            elif match_obj.group('unit') == 'K':
                bw /= 1024
            if bw > 1024:
                bw = 1024
            bw_list.append(bw)
        line = netio_obj.readline()
    netio_obj.close()
    return bw_list

def read_bw_list_batch(netio_file, batch_size):
    bw_list = []
    netio_obj = open(netio_file, 'r')
    netio_str = '^Total send rate:\s+([0-9]|\.)*[0-9]+(K|M|'')b\s+(?P<bw>([0-9]|\.)*[0-9]+)(?P<unit>K|M|'')b'
    netio_pattern = re.compile(netio_str)
    line = netio_obj.readline()
    curr_batch_size = 0
    bw_batch = 0
    while line != "":
        match_obj = netio_pattern.match(line)
        if match_obj:
            bw = float(match_obj.group('bw'))
            if match_obj.group('unit') == '':
                bw /= 1024*1024
            elif match_obj.group('unit') == 'K':
                bw /= 1024
            if bw > 1024:
                bw = 1024
            curr_batch_size += 1
            bw_batch += bw
            if (curr_batch_size == batch_size):
                bw_list.append(bw_batch/batch_size)
                curr_batch_size = 0
                bw_batch = 0
        line = netio_obj.readline()
    bw_list.append(bw_batch/curr_batch_size)
    netio_obj.close()
    return bw_list

def plot_bw_list(time_len, bw_list, mk):
    sec_list = []
    accum_sec = 0
    num_data_points = len(bw_list)
    time_step = double(time_len) / num_data_points
    #print time_len
    for x in range (0, num_data_points):
        sec_list.append(accum_sec)
        accum_sec += time_step
    pplt.plot(sec_list, bw_list, marker=mk)
    print accum_sec

marker = [
    '1',
    '+',
    '.'
]

line_style = [
    '-.',
    '-',
    ':'
]

if __name__ == '__main__':
    index = 0
    for netio_file in iftop_files:
#        bw_list = read_bw_list_batch(project_root + result_dir + netio_file, 3)
        bw_list = read_bw_list(project_root + result_dir + netio_file)
        plot_bw_list(runtime[index], bw_list, marker[index])
        index += 1

    plt.tick_params(axis='both', which='major', labelsize=16)

    pplt.suptitle("Bandwidth usage", fontsize=20)
    pplt.xlabel("seconds", fontsize=20)
    pplt.ylabel("Mbps", fontsize=20)
    pplt.legend(label_list, loc=3, prop={'size':18})

    pplt.savefig('bw.pdf')

