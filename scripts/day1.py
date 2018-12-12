my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day1_input.txt")
current_sum = 0
for num in my_file.readlines():
    num = num.strip('\n')
    num = int(num)
    current_sum += num
print("project 1 answer:  " + str(current_sum))


seen_frequencies_dict = {}
current_sum = 0
found_repeat = False
while not found_repeat:
    my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day1_input.txt")
    for num in my_file.readlines():
        num = num.strip('\n')
        num = int(num)
        current_sum += num
        if current_sum in seen_frequencies_dict:
            found_repeat = True
            break
        else:
            seen_frequencies_dict[current_sum] = 1
print("Project 2 answer:  " + str(current_sum))







