#!/usr/bin/env python
# a bar plot with errorbars
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as pplt

# fig = plt.figure(figsize=(8, 2))
# fig.subplots_adjust(bottom=0.15)

fig, ax = pplt.subplots()

# Set log scale must be before plotting
# ax.set_yscale('log')

# (In MB)

sec_to_llh_ssp = [
747.621,
]

sec_to_llh = [
547.782,
#406.138,
]

sec_to_llh_f = [
450.18,
#395.848,
]

N = len(sec_to_llh)
ind1 = [1]
#ind = [2, 3]  # the x locations for the groups
ind = [2]  # the x locations for the groups
#ind2 = [2.25, 3.25]
ind2 = [2.25]
width = 0.25       # the width of the bars

indall = [1.125, 2.125, 3.125]

# fig, ax = plt.subplots()
sec_to_llh_bars1 = ax.bar(ind1, sec_to_llh_ssp, width, color='r', edgecolor='black', \
                      hatch='+', label="Unlimited Bandwidth of 1000Mbps")
sec_to_llh_bars = ax.bar(ind, sec_to_llh, width, color='g', edgecolor='black', \
                      hatch='/', label="Bandwidth Limit 400Mbps")
sec_to_llh_bars2 = ax.bar(ind2, sec_to_llh_f, width, color='b', edgecolor='black', \
                      hatch='x', label="Bandwidth Limit 800Mbps")
ax.set_ylim(ymin=100)

# add some
ax.set_ylabel('Time (seconds)', fontsize=16)
ax.set_yticklabels(ax.get_yticks(), fontsize=16)

ax.set_title('Number of seconds to convergence', fontsize=20)
ax.set_xticks(ind1)
ax.set_xticklabels(('SSP'))

ax.set_xticks(indall)
ax.set_xticklabels(('SSP',
        'MBSSP-Random',
#        'MBSSP-Largeness'
                    ), fontsize=16)

ax.set_xlabel('Update Prioritization Policy & Bandwidth', fontsize=20)

#ax.legend((sec_to_llh_bars[0],
#          sec_to_llh_bars2[0]),
#          ('Bandwidth limit 400Mbps',
#           'Bandwidth limit 800Mbps'), loc=1)

ax.legend()

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., height + 0.3, '%0.2f'% height,
                ha='center', va='bottom', fontsize=12)


autolabel(sec_to_llh_bars)
autolabel(sec_to_llh_bars2)
autolabel(sec_to_llh_bars1)

#autolabel(bg_apply_server_row_bars)

#pplt.tight_layout()

#pplt.show()
pplt.savefig('time_to_reach_llh_random.pdf')
