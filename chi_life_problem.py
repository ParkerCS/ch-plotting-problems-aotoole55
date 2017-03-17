#1 Import csv, numpy, and matplotlib.plot
#2 Open the chi_life_expectancy.txt file
#3 Use csv.reader(file, delimeter='\t') to read in the file to a list.  Make appropriate lists for plotting. Community name will be the x and 2010 life expectancy on the y.
#4 Plot the life_expectancy_2010_list vs a numpy arange() as a bar graph
#5 Use ax = plt.gca() to grab the axes object as ax. Use ax.set_xticklabels(community_list) to place the labels on the x axis, use the kwarg rotation=60 to tilt the lettering since there are a lot of communities
#6  Set an appropriate plt.ylim([min,max])
#7  Label your axes
#8  Add a title
#9  Add text to indicate the minimum and maximum values
#10 Customize your graph in at least two other ways using documentation from matplotlib.org
#11  Comment your code as always.

# Note:  If you would like to present something different than the above for your graph using this dataset, just let me know your intentions before you start and I will do my best to support you.

import csv
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
import matplotlib.patches as mpatches

file = open('chi_life_expectancy.txt', 'r')

life_data = []

reader = csv.reader(file, delimiter = '\t')


for line in reader:
    life_data.append(line)
print(life_data)

#Create Lists
x_list = []
y_list = []
y2_list = []

for i in range(1,len(life_data)):
    x_list.append(life_data[i][1])
    y_list.append(float(life_data[i][8]))
    y2_list.append(float(life_data[i][2]))
print(x_list)
print(y_list)
print(y2_list)

print(life_data)
life_data = life_data[1:]
life_data2 = life_data[1:]

#Find min and max
life_data.sort(key=itemgetter(8))
print(life_data)

life_data2.sort(key=itemgetter(2))
print(life_data2)

#Variables
y_total = y_list
x_labels = x_list
y2_total = y2_list

#Format
plt.figure(figsize = [15, 7], tight_layout=True)
plt.ylim(0, len(y_total)+28)

#min and max lines
start = -1
end = len(x_labels)
val2010 = len(life_data)-1
val1990 = len(life_data2)-1

min2010, = plt.plot((start,end), (life_data[0][8],life_data[0][8]), color = 'blue')
max2010, = plt.plot((start,end), (life_data[val2010][8],life_data[val2010][8]), color = 'blue')
min1990, = plt.plot((start,end), (life_data2[0][2],life_data2[0][2]), color = 'green')
min1990, = plt.plot((start,end), (life_data2[val1990][2],life_data2[val1990][2]), color = 'green')

#Graph
plt.bar(np.arange(len(y_total)), y_total, 0.75, color = 'orange') #0.75 is thickness of the line

plt.bar(np.arange(len(y2_total)), y2_total, 0.75, color = 'red')

#Legend
first_patch = mpatches.Patch(color = 'orange', label = '2010 Life Expectancy')
second_patch = mpatches.Patch(color = 'red', label = '1990 Life Expectancy')
third_patch = mpatches.Patch(color = 'blue', label = '2010 Min. and Max. Life Expectancy')
fourth_patch = mpatches.Patch(color = 'green', label = '1990 Min. and Max. Life Expectancy')

plt.legend(handles = [first_patch, second_patch, third_patch, fourth_patch], shadow = True)


#Text for min and max values
plt.text(len(x_labels)/2-5, 101, str("2010 Maximum is: " + life_data[val2010][8]))
plt.text(len(x_labels)/2-5, 97,str("2010 Minimum is: " + life_data[0][8]))
plt.text(len(x_labels)/2-5, 93, str("1990 Maximum is: " + life_data[val1990][2]))
plt.text(len(x_labels)/2-5, 89, str("1990 Minimum is: " + life_data[0][2]))

#Labels
plt.xticks(np.arange(len(y_total)), x_labels, rotation = 90)

plt.xlabel('Neighborhood')

plt.ylabel('Life Expectancy')

plt.title('Life Expectancy by Neighborhood')

plt.show()