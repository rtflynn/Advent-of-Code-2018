import re

my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day3_input.txt")
parsed_strings = []
for claim in my_file.readlines():
    parsed_claim = re.split(r'#| @ |,|:|x| |\n', claim)
    parsed_claim = list(filter(None, parsed_claim))
    print(parsed_claim)
    parsed_strings.append(parsed_claim)

overlap_squares_count = 0
squares_hit_dict = {}
for parsed_string in parsed_strings:
    claim_number, x, y, width, height = parsed_string
    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    for i in range(width):
        for j in range(height):
            if (x + i, y + j) in squares_hit_dict:
                squares_hit_dict[(x + i, y + j)] += 1
            else:
                squares_hit_dict[(x + i, y + j)] = 1


for square in squares_hit_dict:
    if squares_hit_dict[square] > 1:
        overlap_squares_count += 1

print("Project 1 answer:  " + str(overlap_squares_count))


for parsed_string in parsed_strings:
    claim_number, x, y, width, height = parsed_string
    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    is_correct_claim = True
    for (i, j) in ((a,b) for a in range(width) for b in range(height)):
        if squares_hit_dict[(x+i,y+j)] > 1:
            is_correct_claim = False
            break
    if is_correct_claim:
        print("Project 2 answer:  " + claim_number)