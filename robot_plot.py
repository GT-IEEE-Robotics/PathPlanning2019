import robot_2019
import matplotlib.pyplot as plt
import numpy
import random
import math

#creates objects and robot (pre-determined, for controlled testing)
"""
stuff = [robot_2019.color_obj.color_obj((28, 27), 0, True, False, False)]
stuff.append(robot_2019.color_obj.color_obj((66, 32), 0, True, False, False))
stuff.append(robot_2019.color_obj.color_obj((29, 60), 0, True, False, False))
stuff.append(robot_2019.color_obj.color_obj((18, 48), 1, True, False, False))
stuff.append(robot_2019.color_obj.color_obj((65, 37), 1, True, False, False))
stuff.append(robot_2019.color_obj.color_obj((35, 59), 1, True, False, False))
stuff.append(robot_2019.color_obj.color_obj((77, 62), 2, True, False, False))
stuff.append(robot_2019.color_obj.color_obj((40, 84), 2, True, False, False))
stuff.append(robot_2019.color_obj.color_obj((46, 37), 2, True, False, False))
stuff.append(robot_2019.color_obj.color_obj((31, 40), 3, True, False, False))
stuff.append(robot_2019.color_obj.color_obj((76, 37), 3, True, False, False))
stuff.append(robot_2019.color_obj.color_obj((60, 73), 3, True, False, False))
JJ = robot_2019.robot((5, 5), stuff, 0)
"""

#draws straight-line path
def draw_path(obj):
    plt.plot([JJ.coords[0], obj.coords[0]], [JJ.coords[1], obj.coords[1]])

#draws field
def show_field():
    plt.plot([8*math.cos(x)+50 for x in numpy.arange(0, 6.35, math.pi/2)], [8*math.sin(y)+50 for y in numpy.arange(0, 6.35, math.pi/2)], 'k')
    plt.plot([40*math.cos(x)+50 for x in numpy.arange(0, 6.35, .1)], [40*math.sin(y)+50 for y in numpy.arange(0, 6.35, .1)], 'k')
    color_list = ['b', 'g', 'r', 'y']
    plt.plot([10, 42], [50, 50], color_list[0])
    plt.plot([50, 50], [42, 10], color_list[1])
    plt.plot([58, 90], [50, 50], color_list[2])
    plt.plot([50, 50], [58, 90], color_list[3])
    plt.plot([0, 10, 10], [10, 10, 0], color_list[0])
    plt.plot([90, 90, 100], [0, 10, 10], color_list[1])
    plt.plot([90, 90, 100], [100, 90, 90], color_list[2])
    plt.plot([0, 10, 10], [90, 90, 100], color_list[3])
    plt.plot([JJ.coords[0]], [JJ.coords[1]], 'k+')
    for n in range(0, 4):
        xx = [o.coords[0] for o in JJ.objs[3*n:3*n+3]]
        yy = [o.coords[1] for o in JJ.objs[3*n:3*n+3]]
        plt.plot(xx, yy, color_list[n]+'o')
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.show()
    
#identical to four_loops(), but with GUI
def loops_gui():
    goals = []
    for n in range(0, 4):
        while type(JJ.next_obj()) is not tuple:
            target = JJ.next_obj()
            draw_path(target)
            JJ.next_obj().retrieved = True
            JJ.coords = target.coords
            goals.append(target.coords)
        goals.append(JJ.next_obj())
        plt.plot([JJ.coords[0], JJ.next_obj()[0]], [JJ.coords[1], JJ.next_obj()[1]])
        JJ.coords = JJ.next_obj()
        for o in JJ.objs_held():
            o.sort = True
            o.retrieved = False
        JJ.next_quad()
    plt.plot([JJ.coords[0], 5], [JJ.coords[1], 5])
    JJ.coords = (5, 5)
    goals.append((5, 5))
    return goals

#resets parameters for live testing
def reset_field():
    JJ.coords = (5, 5)
    JJ.quadrant = 0
    for o in JJ.objs:
        o.spotted = True
        o.retrieved = False
        o.sort = False

if __name__=="__main__":
    #creates objects and robot (random)
    stuff = [robot_2019.color_obj.color_obj((random.randint(20, 80), random.randint(20, 80)), n, True, False, False) for n in [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]]
    JJ = robot_2019.Robot((5, 5), stuff, 0)
    loops_gui()
    show_field()