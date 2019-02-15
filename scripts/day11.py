import numpy as np


# NOTE(!) :  My part 1 solution is fine.  My part 2 solution is one of the most wasteful/inefficient
# things I've ever written!  I reckon part 2 can be done much more efficiently by (say) pre-building
# a collection of np.arrays whose component-wise sum gives the grid_total.  And to get these arrays,
# either pad our power_levels array on the top and on the left with i+1 rows, j+1 columns of zeros,
# i, j ranging from 0 to ell.  At least then the sum can be done much more efficiently than we've done
# in grid_total.  Off the top of my head, I can't see a significantly better way of solving this,
# but I wouldn't be surprised if there's one which blows this out of the water.




grid_serial_number = 7989
grid = np.zeros([300,300])
rack_ids = np.zeros([300, 1])
for i in range(300):
    rack_ids[i] = i + 11

rack_ids = rack_ids.T


y_coords = np.zeros([300,1])
for i in range(300):
    y_coords[i] = i+1


power_levels = np.dot(y_coords, rack_ids).T
power_levels += grid_serial_number
power_levels = np.multiply(power_levels, rack_ids.T)
power_levels = np.floor(power_levels/100)
power_levels = power_levels % 10
power_levels = power_levels - 5

#power_levels[121,78]   returns the power level for the fuel cell at (122,79).  Note the offset-by-one!



def get_padded_plvls(plvls, padding_size):
    new_power_levels = np.pad(plvls, ((0, padding_size), (0, padding_size)), mode='constant')
    return new_power_levels


def grid_total(plvls, i, j, square_size):
    total = 0
    for a in range(square_size):
        for b in range(square_size):
            total += plvls[i+a, j+b]
    return total



max = -1
max_i = -1
max_j = -1
for i in range(300):
    for j in range(300):
        new_power_levels = get_padded_plvls(power_levels, 3)
        if grid_total(new_power_levels, i, j, 3) > max:
            max = grid_total(new_power_levels, i, j, 3)
            max_i = i
            max_j = j

print("Project 1 answer:  " + str(max_i) + "," + str(max_j))

max = 0
max_i = -1
max_j = -1
for ell in range(300):
    for i in range(300):
        for j in range(300):
            new_power_levels = get_padded_plvls(power_levels, ell + 1)
            if grid_total(new_power_levels, i, j, ell+1) > max:
                max = grid_total(new_power_levels, i, j, ell+1)
                max_i = i + 1
                max_j = j + 1
                #print("Current record:  max, i, j, ell = " + str(max) + ", " + str(max_i) + ", " + str(max_j) + ", " + str(ell+1) + ".")


print("Project 2 answer:  " + str(max_i) + "," + str(max_j) + "," + str(ell+1))