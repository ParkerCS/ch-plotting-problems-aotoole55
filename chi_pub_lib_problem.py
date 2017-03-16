
# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
# calculate (and make a list of) the total visitors to Chicago libraries each month.  Do not plot every library individually.  Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend
# label axes, title the graph

import csv
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
import matplotlib.patches as mpatches

lib_data = []
headers = []
file = open('chilib_visitors_2016', 'r')

reader = csv.reader(file, delimiter = '\t')

for line in reader:
    lib_data.append(line)

x_label = lib_data[0][1:13]

month_totals = []

for month in range(12):
    total = 0
    for i in range(1,len(lib_data)):
        total += int(lib_data[i][month+1])
    month_totals.append(int(total))
print(month_totals)

print(lib_data)

lib_data = lib_data[1:]

for i in range(len(lib_data)):
    lib_data[i][-1] = int(lib_data[i][-1])

lib_data.sort(key=itemgetter(-1))
print(lib_data[-3:])

bar_graph = []
most_popular = lib_data[-3:]
bar_graph.append(most_popular)
bar_graph.append(month_totals)

x_bars = x_label
y_total = month_totals




print(bar_graph)

plt.figure(figsize = [10, 5], tight_layout=True)


plt.xticks(np.arange(len(y_total)), x_label, rotation = 45)


total, = plt.plot(np.arange(len(y_total)), bar_graph[1])
first, = plt.plot(np.arange(len(y_total)), bar_graph[0][2][1:13])
second, = plt.plot(np.arange(len(y_total)), bar_graph[0][1][1:13])
third, = plt.plot(np.arange(len(y_total)), bar_graph[0][0][1:13])

first.set_color('purple')
second.set_color('orange')
third.set_color('green')
total.set_color('blue')

total_patch = mpatches.Patch(color = 'blue', label = 'Total Visistors By Month')
first_patch = mpatches.Patch(color = 'purple', label = 'Library with Most Total Visistors')
second_patch = mpatches.Patch(color = 'orange', label = 'Library with Second Most Total Visistors')
third_patch = mpatches.Patch(color = 'green', label = 'Library with Third Most Total Visistors')

plt.legend(handles = [total_patch, first_patch, second_patch, third_patch], shadow = True)
plt.xlabel('Months')

plt.ylabel('Number of Visitors')

plt.title('Library Visitors by Month')


plt.show()


