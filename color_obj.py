import math

#defines the state of each color object
class color_obj:

    #data describing the current state of each object
    #color is the color index (0:3), spotted is if the object has been seen
    #retrieved is if the robot currently is holding the object
    #has_sorted is if the object has been sorted or not
    def __init__(self, coords, color, spotted, retrieved, has_sorted):
        self.coords = coords
        self.color = color
        self.spotted = spotted
        self.retrieved = retrieved
        self.sort = has_sorted
        self.angle = math.atan2(self.coords[1]-50, self.coords[0]-50)

    def __str__(self):
        return 'object (color: '+str(self.color)+') @ '+str(self.coords)

    #returns the tuple (x, y) describing the differnece in distance WRT robot
    def _xy_dist(self, my_coords):
        return (self.coords[0]- my_coords[0], self.coords[1]- my_coords[1])

    #calculates dist from the robot to the block, given robot's coordinates
    def dist(self, my_coords):
        return math.hypot(self._xy_dist(my_coords)[1], self._xy_dist(my_coords)[0])

    #returns the angle from the robot to the object
    def angle_WRT_robot(self, my_coords):
        robot_angle = math.atan2(my_coords[1]-50, my_coords[0]-50)
        if self.angle < (robot_angle - .3): return self.angle + 2*math.pi
        else: return self.angle
        #return math.atan2(self._xy_dist(my_coords)[1], self._xy_dist(my_coords)[0])

#testing the color object class
"""
block = color_obj((8, 10), 0, True, False, False)
"""
