import re
my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day4_input.txt")
parsed_strings = []
for my_string in my_file.readlines():
    parsed_string = re.split('\[|-| |:|]|\n|1518|\#', my_string)
    parsed_string = list(filter(None, parsed_string))
    parsed_strings.append(parsed_string)

parsed_strings.sort()

# Leaving this in for future reference:  Uncomment and run to see the general layout of our list of parsed strings.
# This wil make the following code and all the indices make a lot more sense.
#for parsed_string in parsed_strings:
#    print(parsed_string)

current_guard = -1
awake = True
last_minute_asleep = 0
intervals_slept_dict = {}

for parsed_string in parsed_strings:
    if parsed_string[4] == 'Guard':
        current_guard = parsed_string[5]
        last_minute_asleep = 0
    if parsed_string[4] == 'falls':
        last_minute_asleep = int(parsed_string[3])
    if parsed_string[4] == 'wakes':
        wakeup_minute = int(parsed_string[3])
        time_slept = wakeup_minute - last_minute_asleep
        if current_guard in intervals_slept_dict:
            intervals_slept_dict[current_guard].append([last_minute_asleep, wakeup_minute - 1])
        else:
            intervals_slept_dict[current_guard] = [[last_minute_asleep, wakeup_minute - 1]]

# Remove comments here to see what the intervals_slept_dict looks like.
#for guard in intervals_slept_dict:
#    print(guard)
#    print(intervals_slept_dict[guard])

max_time_slept = 0
sleepiest_guard = -1
for guard in intervals_slept_dict:
    total_time_sleeping = 0
    for interval in intervals_slept_dict[guard]:
        total_time_sleeping += interval[1] - interval[0]
    if total_time_sleeping > max_time_slept:
        max_time_slept = total_time_sleeping
        sleepiest_guard = guard

interval_list = intervals_slept_dict[sleepiest_guard]
sleepiest_minute = -1
max_days_slept_during_given_minute = -1
for i in range(60):
    num_days_slept_this_minute = 0
    for interval in interval_list:
        if interval[0] <= i <= interval[1]:
            num_days_slept_this_minute += 1
    if num_days_slept_this_minute > max_days_slept_during_given_minute:
        max_days_slept_during_given_minute = num_days_slept_this_minute
        sleepiest_minute = i

print("The sleepiest guard is " + sleepiest_guard + " and the most likely minute he/she will be sleeping is the " + str(sleepiest_minute) + " minute.")
ans = int(sleepiest_guard) * sleepiest_minute
print("Project 1 answer:  " + str(ans))



part2_sleepiest_minute = -1
part2_sleepiest_guard = -1
part2_max_dats_slept_during_given_minute = -1
for guard in intervals_slept_dict:
    interval_list = intervals_slept_dict[guard]
    for i in range(60):
        num_days_slept_this_minute = 0
        for interval in interval_list:
            if interval[0] <= i <= interval[1]:
                num_days_slept_this_minute += 1
        if num_days_slept_this_minute > part2_max_dats_slept_during_given_minute:
            part2_max_dats_slept_during_given_minute = num_days_slept_this_minute
            part2_sleepiest_minute = i
            part2_sleepiest_guard = guard
print("For part 2, guard " + guard + " had the most consistent 'sleep-minute', which occurred at " + str(part2_sleepiest_minute) + ".")
part2_ans = int(part2_sleepiest_guard) * part2_sleepiest_minute
print("Project 2 answer:  " + str(part2_ans))
