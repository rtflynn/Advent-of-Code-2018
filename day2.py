my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day2_input.txt")
my_string_list = []
for box_id in my_file.readlines():
    box_id = box_id.strip('\n')
    my_string_list.append(box_id)
if my_string_list:
    box_id_length = len(my_string_list[0])


def get_multiplicity_list(my_string):
    characters_seen_dict = {}
    for i in range(len(my_string)):
        if my_string[i] in characters_seen_dict:
            characters_seen_dict[my_string[i]] += 1
        else:
            characters_seen_dict[my_string[i]] = 1
    return [characters_seen_dict[key] for key in characters_seen_dict]


num_ids_which_contain_a_double = 0
num_ids_which_contain_a_triple = 0

for box_id in my_string_list:
    chars_seen_multiplicities = get_multiplicity_list(box_id)
    if 2 in chars_seen_multiplicities:
        num_ids_which_contain_a_double += 1
    if 3 in chars_seen_multiplicities:
        num_ids_which_contain_a_triple += 1

check_sum = num_ids_which_contain_a_double*num_ids_which_contain_a_triple
print("Project 1 answer:  " + str(check_sum))


def delete_nth_letter_from_all_strings(n, list_of_strings):
    new_list = []
    for my_string in list_of_strings:
        new_string = my_string[:n] + my_string[n+1:]
        new_list.append(new_string)
    return new_list


for i in range(box_id_length):
    new_list = delete_nth_letter_from_all_strings(i, my_string_list)
    ids_seen_dict = {}
    for some_string in new_list:
        if some_string in ids_seen_dict:
            print("Project 2 answer:  " + some_string)
            break
        else:
            ids_seen_dict[some_string] = 0













