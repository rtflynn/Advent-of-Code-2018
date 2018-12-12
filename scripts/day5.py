import re
my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day5_input.txt")
my_string = my_file.readlines()[0].strip('\n')


def collapse_polymer(my_string):

    string_length = len(my_string)
    my_cursor = 0
    while my_cursor < string_length - 1:
        if my_string[my_cursor].lower() == my_string[my_cursor + 1].lower():
            if my_string[my_cursor] != my_string[my_cursor + 1]:
                my_string = my_string[:my_cursor] + my_string[my_cursor+2:]
                string_length -= 2
                if my_cursor > 0:
                    my_cursor -= 1 # We need to backtrack after cancelling adjacent letters because we may have just caused a new adjacency
            else:
                my_cursor += 1
        else:
            my_cursor += 1
    return my_string

shortened_string = collapse_polymer(my_string)
print("Project 1 answer:  " + str(len(shortened_string)))


def remove_letter_and_collapse_polymer(letter, some_string):
    lowercase_letter = letter.lower()
    cap_letter = letter.upper()
    letter_pair_to_remove = lowercase_letter + cap_letter
    some_string = re.sub(str([letter_pair_to_remove]), '', some_string)
    some_string = collapse_polymer(some_string)
    return some_string

min_size_polymer = len(my_string)
best_letter = ""
letters = 'abcdefghijklmnopqrstuvwxyz'
for letter in letters:
    collapsed_polymer = remove_letter_and_collapse_polymer(letter, my_string)
    collapsed_length = len(collapsed_polymer)
    if collapsed_length < min_size_polymer:
        min_size_polymer = collapsed_length
        best_letter = letter

print("The letter " + best_letter + " made for the shortest collapsed polymer, with a length of " + str(min_size_polymer) + ".")
print("Project 2 answer:  " + str(min_size_polymer))



