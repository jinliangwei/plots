#!/usr/bin/env python

import numpy
import os, sys
import re
import matplotlib.pyplot as pplt
from pylab import *

# absolute path
project_root="/usr0/home/jinlianw/Work/research/code/petuum.git/"

# result directory
result_dir="results/vd_7_17/"

llh_files = [
#"aggr_exp.SSPAggr.staleness-2.iter_per_unit-1.update_sort_policy-Random.bg_idle_milli-10.thread_oplog_batch_size-80000.bw-12.ubound_kb-40.server_push_row_threshold-200.server_batch-1000000.work_units-80.1GE/nytimes.llh",
"aggr_exp.SSPAggr.staleness-2.iter_per_unit-1.update_sort_policy-Random.bg_idle_milli-10.thread_oplog_batch_size-80000.bw-25.ubound_kb-80.server_push_row_threshold-200.server_batch-1000000.work_units-80.1GE/nytimes.llh",
"aggr_exp.SSPAggr.staleness-2.iter_per_unit-1.update_sort_policy-Random.bg_idle_milli-10.thread_oplog_batch_size-80000.bw-50.ubound_kb-160.server_push_row_threshold-200.server_batch-1000000.1GE/nytimes.llh",
#"aggr_exp.SSPAggr.staleness-2.iter_per_unit-1.update_sort_policy-RelativeMagnitude.bg_idle_milli-10.thread_oplog_batch_size-80000.bw-12.ubound_kb-40.server_push_row_threshold-200.server_batch-1000000.work_units-80.1GE/nytimes.llh",
"aggr_exp.SSPAggr.staleness-2.iter_per_unit-1.update_sort_policy-RelativeMagnitude.bg_idle_milli-10.thread_oplog_batch_size-80000.bw-25.ubound_kb-80.server_push_row_threshold-200.server_batch-1000000.work_units-80.1GE/nytimes.llh",
"aggr_exp.SSPAggr.staleness-2.iter_per_unit-1.update_sort_policy-RelativeMagnitude.bg_idle_milli-10.thread_oplog_batch_size-80000.bw-50.ubound_kb-160.server_push_row_threshold-200.server_batch-1000000.1GE/nytimes.llh",
"aggr_exp.SSPPush.staleness-2.iter_per_unit-1.update_sort_policy-Random.bg_idle_milli-10.thread_oplog_batch_size-80000.bw-50.ubound_kb-160.server_push_row_threshold-200.server_batch-1000000.1GE/nytimes.llh.80",
#"bsp_exp.SSPPush.staleness-0.iter_per_unit-1.update_sort_policy-Random.bg_idle_milli-10.thread_oplog_batch_size-80000.bw-50.ubound_kb-160.server_push_row_threshold-200.server_batch-1000000.work_units-220.1GE/nytimes.llh"
]

marker = [
    '1',
    '+',
    '1',
    '+',
    '.'
]

line_style = [
    '-.',
    '-.',
    '-',
    '-',
    ':'
]

label_list = [
    "MBSSP-Random, 400Mbps",
    "MBSSP-Random, 800Mbps",
    "MBSSP-Largeness, 400Mbps",
    "MBSSP-Largeness, 800Mbps",
    "SSP, slack = 2",
    "BSP"
]

def read_llh(file_name):
    iter_num = []
    llh = []
    sec = []
    llh_file = open(file_name, 'r')
    line_num = 0
    for line in llh_file:
        #if line_num == 0:
        #    line_num += 1
        #    continue
        line_array = line.split(' ')
        iter_num.append(int(line_array[0]))
        llh.append(float(line_array[1]))
        sec.append(float(line_array[2]))

    return iter_num, llh, sec

def plot_llh(sec_or_iter, llh, line_marker, style):
    pplt.plot(sec_or_iter, llh, marker=line_marker, ls=style, ms=12, lw=2)

def read_plot_gl(file_name, line_marker):
    llh = []
    sec = []
    llh_file = open(file_name, 'r')
    for line in llh_file:
        line_array = line.split(' ')
        llh.append(float(line_array[1]))
        sec.append(float(line_array[0]))
    pplt.plot(sec, llh)

if __name__ == '__main__':
    index = 0

    for llh_file in llh_files:
        iter_num, llh, sec = read_llh(project_root + result_dir + llh_file)
        plot_llh(sec, llh, marker[index], line_style[index])
#        plot_llh(iter_num, llh, marker[index])
        index += 1

    x1,x2,y1,y2 = plt.axis()
    plt.axis((x1,x2,-1.5e9,y2))
    plt.tick_params(axis='both', which='major', labelsize=16)

   # font = {'size'   : 18}
   # matplotlib.rc('font', **font)

    grid(True)
    xgridlines = getp(gca(), 'xgridlines')
    ygridlines = getp(gca(), 'ygridlines')
    pplt.setp(xgridlines, 'linestyle', '-')
    pplt.setp(ygridlines, 'linestyle', '-')

    pplt.suptitle("Convergence per sec", fontsize=20)
    pplt.xlabel("seconds", fontsize=20)
    pplt.ylabel("Log-Likelihood", fontsize=20)
    pplt.legend(label_list, loc=4, prop={'size':18})

    pplt.savefig('lda_llh_sec_bw.pdf')

#    pplt.suptitle("Convergence per iteration")
#    pplt.xlabel("iterations")

#    pplt.savefig('lda_llh_iter_bw.pdf')
