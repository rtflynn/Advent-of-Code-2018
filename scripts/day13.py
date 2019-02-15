import re
my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day13_input.txt")

current_state = []
for line in my_file.readlines():
    current_state.append(re.split('\n', line)[0])


carts = {}
intersections = {}
downright_corners = {}
upright_corners = {}
for row in range(len(current_state)):
    for column in range(len(current_state[row])):
        temp = current_state[row][column]
        location = (row, column)
        if temp == 'v' or temp == '^' or temp == '<' or temp == '>':
            carts[location] = temp, 0
        elif temp == '+':
            intersections[location] = 0
        elif temp == '\\':
            downright_corners[location] = 0
        elif temp == '/':
            upright_corners[location] = 0


left_turn_dict = {'<': 'v', 'v': '>', '>': '^', '^': '<'}
right_turn_dict = {'<': '^', '^': '>', '>': 'v', 'v': '<'}


def turn(direction, num_turns_made):
    if num_turns_made == 0:
        new_direction = left_turn_dict[direction]
    elif num_turns_made == 1:
        new_direction = direction
    elif num_turns_made == 2:
        new_direction = right_turn_dict[direction]
    num_turns_made += 1
    if num_turns_made > 2:
        num_turns_made = 0
    return new_direction, num_turns_made


def move(cart, carts, intersections, downright_corners, upright_corners):
    if cart not in carts:
        return (-1, -1), carts

    row, column = cart
    dir, num_turns_made = carts[cart]
    del carts[cart]

    if dir == '>':
        column += 1
    elif dir == '<':
        column -= 1
    elif dir == '^':
        row -= 1
    elif dir == 'v':
        row += 1

    cart = (row, column)

    if (row, column) in intersections:
        dir, num_turns_made = turn(dir, num_turns_made)

    elif (row, column) in downright_corners:
        if dir == '>':
            dir = 'v'
        elif dir == '<':
            dir = '^'
        elif dir == '^':
            dir = '<'
        elif dir == 'v':
            dir = '>'

    elif (row, column) in upright_corners:
        if dir == '>':
            dir = '^'
        elif dir == '<':
            dir = 'v'
        elif dir == '^':
            dir = '>'
        elif dir == 'v':
            dir = '<'

    if cart in carts:
        print("Collision!  At location " + str(column) + ", " + str(row) + ".")
        del carts[cart]
    else:
        carts[cart] = dir, num_turns_made
    return (row, column), carts

def tick(carts, intersections, downright_corners, upright_corners):
    temp_carts_list = list(carts)
    temp_carts_list.sort()
    for cart in temp_carts_list:
        _, carts = move(cart, carts, intersections, downright_corners, upright_corners)
    return carts


while(len(list(carts)) > 1):
    carts = tick(carts, intersections, downright_corners, upright_corners)

for cart_loc in carts.keys():
    last_cart_row, last_cart_column = cart_loc

print("The last remaining cart is at: " + str(last_cart_column) + ", " + str(last_cart_row))