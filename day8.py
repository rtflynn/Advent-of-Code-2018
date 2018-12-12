### Note:  Part 1 wasn't bad.  Part 2 didn't look too bad but oh boy, was my code a mess!
### After trying this and that for about 3 hours, I decided to check out the subreddit.
### I read /u/sciyoshi's answer at https://www.reddit.com/r/adventofcode/comments/a47ubw/2018_day_8_solutions/ ,
### thought about it, closed the window and took a walk.  Came back and did something similar from scratch.


my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day8_input.txt")
for line in my_file:
    num_list = [int(x) for x in line.split()]


def build_tree(num_list, cursor_loc=0):
    child_node_quantity = num_list[cursor_loc]
    metadata_quantity = num_list[cursor_loc + 1]
    cursor_loc += 2
    metadata_total = 0

    for i in range(child_node_quantity):
        metadata_contrib, cursor_loc = build_tree(num_list, cursor_loc)
        metadata_total += metadata_contrib

    for j in range(metadata_quantity):
        metadata_total += num_list[cursor_loc]
        cursor_loc += 1
    return metadata_total, cursor_loc


metadata_tot, _ = build_tree(num_list=num_list)
print("Project 1 answer:  " + str(metadata_tot))


def new_get_value(num_list):
    num_children = num_list[0]
    num_meta = num_list[1]
    num_list = num_list[2:]
    child_values = []

    for i in range(num_children):
        value, num_list = new_get_value(num_list)
        child_values.append(value)

    if num_children == 0:
        value = sum(num_list[i] for i in range(num_meta))
        num_list = num_list[num_meta:]
        return value, num_list

    else:
        meta_list = [num_list[i] for i in range(num_meta)]
        value = sum(child_values[k-1] for k in meta_list if 0 < k <= len(child_values))
        num_list = num_list[num_meta:]
        return value, num_list


ans, _ = new_get_value(num_list)
print("Project 2 answer:  " + str(ans))






















