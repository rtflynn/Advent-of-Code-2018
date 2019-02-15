

recipes = [3, 7]
first_elf, second_elf = 0, 1

def create_new_recipes(recipes, first_elf, second_elf):
    current_recipes_sum = recipes[first_elf] + recipes[second_elf]
    if current_recipes_sum < 10:
        recipes.append(current_recipes_sum)
    else:
        recipes.append(1)
        recipes.append(current_recipes_sum % 10)


def move_elf(recipes, elf):
    move_amount = recipes[elf] + 1
    new_location = (elf + move_amount) % len(recipes)
    return new_location


num_recipes = 2018

for i in range(num_recipes + 8):
    create_new_recipes(recipes, first_elf, second_elf)
    first_elf = move_elf(recipes, first_elf)
    second_elf = move_elf(recipes, second_elf)
    #print(recipes)

ans_string = "".join(str(num) for num in recipes[num_recipes:num_recipes + 10])
print("Project 1 answer: " + ans_string)



recipes = [3, 7]
first_elf, second_elf = 0, 1

#given_score_sequence = [5,1,5,8,9]
#given_score_sequence = [5, 9, 4, 1, 4]
#given_score_sequence = [0, 1, 2, 4, 5]
given_score_sequence = [9, 4, 5, 1, 0]
given_score_sequence = [8, 9, 4, 5, 0, 1]

score_seq_length = len(given_score_sequence)


counter = 0
while recipes[-score_seq_length:] != given_score_sequence and\
        recipes[-score_seq_length - 1: -1] != given_score_sequence:
    create_new_recipes(recipes, first_elf, second_elf)
    first_elf = move_elf(recipes, first_elf)
    second_elf = move_elf(recipes, second_elf)
    counter += 1


if recipes[-score_seq_length:] == given_score_sequence:
    ans2 = len(recipes) - score_seq_length
else:
    ans2 = len(recipes) - score_seq_length - 1

print("Project 2 answer: " + str(ans2))