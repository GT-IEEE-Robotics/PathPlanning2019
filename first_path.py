#given current position and a list of coordinates
#picks a random coordinate pair and gives path to get there

#note that I did NOT use a grid, I just ran calculations

import random as rdm
import math

def go_to_2(coords, my_coords):
    path = [tuple(my_coords[:])]
    goal = coords[0]
    while my_coords != goal:
        direction = est_angle(my_coords, goal)
        if math.pi*(-7/8)<=direction<=math.pi*(-5/8):
            my_coords[0] += -1
            my_coords[1] += -1
        elif math.pi*(-5/8)<direction<=math.pi*(-3/8):
            my_coords[1] += -1
        elif math.pi*(-3/8)<direction<=math.pi*(-1/8):
            my_coords[0] += 1
            my_coords[1] += -1
        elif math.pi*(-1/8)<direction<=math.pi/8:
            my_coords[0] += 1
        elif math.pi/8<direction<=math.pi*(3/8):
            my_coords[0] += 1
            my_coords[1] += 1
        elif math.pi*(3/8)<direction<=math.pi*(5/8):
            my_coords[1] += 1
        elif math.pi*(5/8)<direction<=math.pi*(7/8):
            my_coords[0] += -1
            my_coords[1] += 1
        else:
            my_coords[0] += -1
        path.append(tuple(my_coords[:]))
    return path

def go_to(coords, my_coords):
    path = [tuple(my_coords[:])]
    goal = coords[0]
    while my_coords != goal:
        direction = est_angle(my_coords, goal)
        if math.pi*(-3/4)<=direction<=math.pi/(-4):
            my_coords[1] += -1
        elif math.pi/(-4)<direction<=math.pi/4:
            my_coords[0] += 1
        elif math.pi/4<direction<=math.pi*(3/4):
            my_coords[1] += 1
        else:
            my_coords[0] += -1
        path.append(tuple(my_coords[:]))
    return path

def coords_diff(my_coords, goal_coords):
    return (goal_coords[0]-my_coords[0], goal_coords[1]-my_coords[1])

def est_angle(my_coords, goal_coords):
    xy_dist = coords_diff(my_coords, goal_coords)
    return math.atan2(xy_dist[1], xy_dist[0])

class __main__:
    coords = [[rdm.randint(0, 50), rdm.randint(0, 50)] for n in range(4)]
    my_coords = coords.pop()
    print(go_to(coords, my_coords[:]))
    print()
    print(go_to_2(coords, my_coords))
