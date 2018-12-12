import re
my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day6_input.txt")

# Note to reader:  I'm actively un-proud of this particular solution.  When project 2 opened up, I already had most
# of the functions available to answer it right away.  The tradeoff was that I had to make my functions more complicated,
# so that now several of the functions you see here have multiple responsibilities.
# I'd definitely refactor this, but since it's just a challenge question I'll leave it as is.
# If you want a nice exercise in tidying up, take a stab at refactoring this so that 'total_dist_to_all_coords'
# and 'num_points_within_10k_of_all_coords' are separate from the functions they currently appear in.


coordinate_list = []
for coord in my_file.readlines():
    coord = re.split(' |,|\n', coord)
    x_coord = int(coord[0])
    y_coord = int(coord[2])
    coordinate_list.append((x_coord,y_coord))

min_x = min(coordinate_list[i][0] for i in range(len(coordinate_list)))
min_y = min(coordinate_list[i][1] for i in range(len(coordinate_list)))
max_x = max(coordinate_list[i][0] for i in range(len(coordinate_list)))
max_y = max(coordinate_list[i][1] for i in range(len(coordinate_list)))
dist_upper_bound = abs(min_x) + abs(min_y) + abs(max_x) + abs(max_y)

left_edge = [[min_x, y] for y in range(min_y, max_y + 1)]
right_edge = [[max_x, y] for y in range(min_y, max_y + 1)]
bottom_edge = [[x, min_y] for x in range(min_x, max_x + 1)]
top_edge = [[x, max_y] for x in range(min_x, max_x + 1)]
bounding_rectangle = left_edge + right_edge + bottom_edge + top_edge



def find_closest_coord(our_point, coordinate_list):
    min_dist = dist_upper_bound
    closest_coord = []
    total_dist_to_all_coords = 0
    for coordinate in coordinate_list:
        dist = abs(our_point[0] - coordinate[0]) + abs(our_point[1] - coordinate[1])
        total_dist_to_all_coords += dist
        if dist < min_dist:
            min_dist = dist
            closest_coord = coordinate
    return total_dist_to_all_coords, min_dist, closest_coord


def find_coords_with_infinite_area(bounding_rect, coordinate_list):
    coords_with_infinite_area = {}
    for my_point in bounding_rect:
        _, _, coord = find_closest_coord(my_point, coordinate_list)
        if coord not in coords_with_infinite_area:
            coords_with_infinite_area[coord] = 1
    return coords_with_infinite_area


def populate_areas_dict(min_x, min_y, max_x, max_y, coordinate_list):
    areas_dict = {}
    num_points_within_10k_of_all_coords = 0
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            total_dist, min_dist, closest_coord = find_closest_coord((i,j), coordinate_list)
            if closest_coord in areas_dict:
                areas_dict[closest_coord] += 1
            else:
                areas_dict[closest_coord] = 1
            if total_dist < 10000:
                num_points_within_10k_of_all_coords += 1
    return areas_dict, num_points_within_10k_of_all_coords


areas_dict, num_points_within_10k_of_all_coords = populate_areas_dict(min_x, min_y, max_x, max_y, coordinate_list)
infinite_areas_dict = find_coords_with_infinite_area(bounding_rectangle, coordinate_list)
for key in infinite_areas_dict:
    del areas_dict[key]

max_area = 0
max_area_point = ()
for key in areas_dict:
    if areas_dict[key] > max_area:
        max_area = areas_dict[key]
        max_area_point = key

print("The coordinate with the maximum area is " + str(max_area_point) + ", with a whopping area of " + str(max_area) + "!")
print("Project 1 answer:  " + str(max_area))

print("There are " + str(num_points_within_10k_of_all_coords) + " points whose total distance to all our coordinates is < 10000.")
print("Project 2 answer:  " + str(num_points_within_10k_of_all_coords))
