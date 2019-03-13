import color_obj
import math

#defines the state of the robot
class robot:
    
    #data describing the current state of the robot
    def __init__(self, my_coords, objects, my_quad):
        self.coords = my_coords
        self.objs = objects
        self.quadrant = my_quad

    #returns the angle with respect to the center
    def angle(self):
        return math.atan2(self.coords[1]-50, self.coords[0]-50)

    #returns distance from center
    def radius(self):
        return math.hypot(self.coords[0]-50, self.coords[1]-50)

    #changes the color quadrant to the next one
    def next_quad(self):
        if self.quadrant == 3: self.quadrant = 0
        else: self.quadrant += 1

    #returns blocks the robot is carrying
    def objs_held(self):
        held = []
        for b in self.objs:
            if b.retrieved: held.append(b)
        return held

    #returns blocks the robot could potentially target
    #must be target color, spotted, not retrieved, and not sorted
    def target_objs(self):
        targets = []
        for b in self.objs:
            if (b.color==self.quadrant) and b.spotted and (not b.retrieved) and (not b.sort):
                targets.append(b)
        return targets

    #sorts objects based on given attribute, low to high
    #only returns a list of targets if targets_only = True
    #attributes are distance and angle as of now
    def attr_sort(self, attribute, targets_only=True):
        if targets_only: objects = self.target_objs()
        else: objects = self.objs
        if attribute == 'distance':
            return sorted(objects, key=lambda x: x.dist(self.coords))
        elif attribute == 'angle':
            return sorted(objects, key=lambda x: x.angle_WRT_robot(self.coords))
        elif attribute == 'spotted':
            attr = []
            for o in objects:
                if o.spotted == True: attr.append(o)
            return attr

    #decides which object to go to next
    def next_obj(self):
        corners = [(5, 5), (95, 5), (95, 95), (5, 95)]
        if len(self.objs_held())==3: return corners[self.quadrant]
        elif len(self.attr_sort('spotted')) == 0:
            next_angle = self.angle() + math.pi/8
            if self.radius() < 15: rad = self.radius() + 5
            elif self.radius() > 50: rad = self.radius() - 30
            else: rad = self.radius()
            return (rad*math.cos(next_angle)+50, rad*math.sin(next_angle)+50)
        elif self.attr_sort('distance')[0].dist(self.coords)<10: return self.attr_sort('distance')[0]
        else: return self.attr_sort('angle')[0]

    #run-through that gets objects
    #mostly for testing, since actual parameters shifts are triggered by inputs
    def four_loops(self):
        goals = []
        for n in range(0, 4):
            while type(self.next_obj()) is not tuple:
                target = self.next_obj()
                self.next_obj().retrieved = True
                self.coords = target.coords
                goals.append(target.coords)
            goals.append(self.next_obj())
            self.coords = self.next_obj()
            for o in self.objs_held():
                o.sort = True
                o.retrieved = False
            self.next_quad()
        goals.append((5, 5))
        return goals

    #the idea here is that the robot outputs the immediate next location
    def next_step(self):
        target = next_obj()

#testing the robot class
"""
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy
import math

stuff = [color_obj.color_obj((8, 10), 0, True, False, False)]
stuff.append(color_obj.color_obj((18, 10), 0, True, False, False))
stuff.append(color_obj.color_obj((16, 37), 0, True, True, False))
stuff.append(color_obj.color_obj((5, 94), 1, True, False, False))
stuff.append(color_obj.color_obj((65, 37), 1, True, False, False))
stuff.append(color_obj.color_obj((5, 17), 1, True, False, False))
stuff.append(color_obj.color_obj((4, 38), 2, True, False, False))
stuff.append(color_obj.color_obj((5, 31), 2, True, False, False))
stuff.append(color_obj.color_obj((46, 37), 2, True, False, False))
stuff.append(color_obj.color_obj((19, 91), 3, True, False, False))
stuff.append(color_obj.color_obj((76, 37), 3, True, False, False))
stuff.append(color_obj.color_obj((6, 37), 3, True, False, False))
JJ = robot((3, 3), stuff, 0)

plt.plot([JJ.coords[0]], [JJ.coords[1]], 'k+')
point_colors = ['bo', 'go', 'ro', 'yo']
for n in range(0, 4):
    xx = [o.coords[0] for o in JJ.objs[3*n:3*n+3]]
    yy = [o.coords[1] for o in JJ.objs[3*n:3*n+3]]
    plt.plot(xx, yy, point_colors[n])
plt.plot([8*math.cos(x)+50 for x in numpy.arange(0, 6.35, math.pi/2)], [8*math.sin(y)+50 for y in numpy.arange(0, 6.35, math.pi/2)])
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.show()
"""
