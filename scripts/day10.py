import re
import numpy as np
import matplotlib.pyplot as plt


my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day10_input.txt")
points_of_light = []
velocities = []
temp = []
for point_of_light in my_file.readlines():
    parsed_info = re.split(r'position|=|<|>|velocity|\n|,', point_of_light)
    (x_pos, y_pos, x_vel, y_vel) = parsed_info[3], parsed_info[4], parsed_info[8], parsed_info[9]
    points_of_light.append([int(x_pos), -int(y_pos)])
    velocities.append([int(x_vel), -int(y_vel)])
    temp.append(parsed_info)


points = np.array(points_of_light)
vels = np.array(velocities)


### I had two complementary ideas here.  One:  Once the message has been written, all the points will fit
### into a small bounding box.  Find that box and use this to intelligently search for the currect image
### Two: Most points will have no neighbors at most times.  So, count the total number of points with
### neighbors.  This should be maximum around the same time as the message appears.
### I went with idea Two, which runs slower than One but has the advantage of working even when we add extra
### 'noise' points into the mix which aren't part of the message.

def taxicab(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def are_neighbors(a,b, threshold = 1):
    return 0 < taxicab(a,b) <= threshold

def has_neighbor(a, points):
    for x in points:
        if are_neighbors(a, x):
            return True
    return False

def count_nonisolated_points(point_list):
    total = 0
    for a in point_list:
        if has_neighbor(a, point_list):
            total += 1
    return total


def tick(points, vels):
    points += vels


offset = 10612       # YOUR OFFSET WILL BE DIFFERENT!!!
### I found this offset by looking at how many nonisolated points there were after each tick, and then
### looking at the graphs myself to figure out the exact offset necessary.
for i in range(offset):
    tick(points, vels)


for i in range(30):             # Just so I don't have to run this over and over, I'd go through a bunch of images.
    x, y = points[:,0], points[:,1]
    plt.scatter(x, y)
    plt.show()
    tick(points, vels)

