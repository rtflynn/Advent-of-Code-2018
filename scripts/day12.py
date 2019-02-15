# Note: This solution requires that the pattern '.....' produces result '.' in the next time step.
# In the context of the problem this makes sense:  A plant isn't going to spontaneously pop out of nowhere.
# Also, if this pattern didn't produce this result, then after one time step the entire negative portion
# of the number line would be covered with '#'.  Anyhow, I've checked that this condition holds for my puzzle input.

import re
my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day12_input.txt")
temp = my_file.readlines()
current_state_non_neg = re.split('initial state: |\n', temp[0])[1] + '.....'
current_state_neg = "....."
current_state = current_state_neg + current_state_non_neg

patterns = {}
for i in range(len(temp) - 2):
    pattern, result, _ = re.split(' => |\n', temp[i+2])
    patterns[pattern] = result


def tempsum(non_neg_string, neg_string):
    total = 0
    temp_neg = neg_string[::-1]
    for i in range(len(non_neg_string)):
        if non_neg_string[i] == '#':
            total += i
    for i in range(len(temp_neg)):
        if temp_neg[i] == '#':
            total -= i + 1
    return total


def time_step(current_state_non_neg, current_state_neg, patterns):
    current_state = current_state_neg + current_state_non_neg
    index_offset = len(current_state_neg)

    new_state = ".."
    for i in range(len(current_state) - 4):
        substring = current_state[i:i+5]
        new_state += patterns[substring]

    new_state_neg = new_state[:index_offset]
    new_state_non_neg = new_state[index_offset:]

    if new_state_neg[0:5] != '.....':
        new_state_neg = '.....' + new_state_neg

    non_neg_length = len(current_state_non_neg)
    if new_state_non_neg[non_neg_length:] != '.....':
        new_state_non_neg = new_state_non_neg + '.....'

    return new_state_non_neg, new_state_neg, new_state


def time_steps(current_state_non_neg, current_state_neg, patterns, n):
    for i in range(n):
        current_state_non_neg, current_state_neg, new_state = time_step(current_state_non_neg, current_state_neg, patterns)
        #print(current_state_neg + current_state_non_neg)
        temp_int = tempsum(current_state_non_neg,current_state_neg)

    return current_state_non_neg, current_state_neg



after20steps_pos, after20steps_neg = time_steps(current_state_non_neg, current_state_neg, patterns, 20)
ans1 = tempsum(after20steps_pos, after20steps_neg)
print("Project 1 answer:  " + str(ans1))



# Eventually the state's shape stabilizes and the whole thing moves over a fixed amount each time step.
# It's easy to see that this is true, by induction, once it's true for a single time step.
# Once this is known, we know that the total sum is also shifted by a constant factor each time step.
# Using this it was easy to determine the following formula.
def sum_after_n_generations(n):
    return 1246 + 51*n


print("Project 2 answer:  " + str(sum_after_n_generations(50000000000 - 1)))
