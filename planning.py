"""
What we know:
    - We're given obstacles and locations
    - List of possible goals (High level)
    - We're rotating counterclockwise

What to do:
    - Provide Greedy Algorithm that determines the priority of goals
    - Return location of goal along with goal
    - Pass that to RTO (Space Planning)

Design:
   - Goal Class: Represents a goal, point value, and location
   - State Class: Define state. Next goal to achieve along with location of goal
       - Do we track the current location of the robot?
   - TSP problem: Initialize Graph with original state. Negate edge weights (points) and use TSp to solve
       - This is quite slow however, and we will want something that is more adaptable.
   - GreedySearch: Order all goals in a priority queue and pop the one with the least amount of points or the one that's closest
   - DecisionTree: Create some hypothesis. But what attributes to select?

TODO:
   - Account for counterclockwise logic (Not sure if RRT handles this or not)
   - Define goals. we can break complicated goals into simple pieces to make searching state space easier
"""


"""
TODO:
what we know for a fact:
8 cubes , 4 spheres
for cubes: 2 of each color
for spheres: 1 of each

NO OTHER ROBOTS ON THE SAME FIELD

-localize
-assign values to blocks based on proximity and "how long to organize"
push through PriorityQueue
- provide 4 blocks to go to in Order
-
"""

import queue

""" Goal class containing location of goal and reward for completion

Comparison operators are implemented to allow
Goal objects to be placed in a PQ
"""

class Goal:

    def __init__(self, color, location=(), order):
        self.color = color
        self.location = location
        self.order = order # Number representing the priority of goals

    def __gt__(self, other):
        if not isInstance(other, Goal):
            raise ValueError("Attempted to compare incorrect types")

        return self.order > other.order

    def __lt__(self, other):
        if not isInstance(other, Goal):
            raise ValueError("Attempted to compare incorrect types")

        return self.order < other.order

    """
    Returns the amount of time it would take to complete a goal based on a list
    of average times that is precalculated.
    The higher the timer the closer the section (ie. higher priority/less time)
    """
    def calc_Time(self, currState):
        timer = 3;
        for location in currState.locations:
            if self.color == location:
                self.value = timer
            timer--


    @property
    def points(self):
        return self.points

class State:

    sorted = False
    isHome = True # Robot always starts at home

    def __init__(self, goal):
        self.next_goal = goal
        checkSensors()


    @property
    def next_goal(self):
        return self.next_goal

    @staticmethod
    def initial_state():
        return State(None) #

    """
    Check the sensors to see what section you are currently in and update the list
    of locations to go through.
    Helps to organize goals based on what comes up next
    """
    def checkSensors(self):
        if sensors is "red":
            self.locations = {"yellow", "blue", "green", "red"}
        elif sensors is "yellow":
            self.locations = {"blue", "green", "red", "yellow"}
        elif sensors is "blue":
            self.locations = {"green", "red", "yellow", "blue"}
        elif sensors is "green":
            self.locations = {"red", "yellow", "blue", "green"}

""" Method to populate a priority queue of goals

Outputs priority queue with all desired goal states

TODO: Right now the *args treats inputs as Goals. Modify for coordinate tuples
"""
def populate_goals(*args):
    priority = PriorityQueue()
    for goal in args:
        if not isInstance(goal, tuple):
            print("Next goal not Goal object. Skipping...")
        else:
            priority.put(goal) # TODO
    return priority

"""
This is a TSP algorithm found online
"""
def optimized_travelling_salesman(points, start=None):
    """
    As solving the problem in the brute force way is too slow,
    this function implements a simple heuristic: always
    go to the nearest city.

    Even if this algoritmh is extremely simple, it works pretty well
    giving a solution only about 25% longer than the optimal one (cit. Wikipedia),
    and runs very fast in O(N^2) time complexity.

    >>> optimized_travelling_salesman([[i,j] for i in range(5) for j in range(5)])
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 4], [1, 3], [1, 2], [1, 1], [1, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 4], [3, 3], [3, 2], [3, 1], [3, 0], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
    >>> optimized_travelling_salesman([[0,0],[10,0],[6,0]])
    [[0, 0], [6, 0], [10, 0]]
    """
    if start is None:
        start = points[0]
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path

""" Things to consider

Right now the approach is to target the goal
that is worth the most points. Later on we
might want to integrate some average with the
amount of time taken to achieve a task
for the purposes of this task, we can
approximate that value as the euclidean distance
between the goal location and the current location
of the bot

Right now, we consider the most basic scenario, which
is leaving home and entering Z1, collecting all objects,
sorting each one, and raising the flag at the end. Every
goals' order attribute represents this

Input: Tuple of coordinates
"""
def main(*args):
    #print("Hello World")
    grid = ()
    #
    for goal in args:
        goal.order = self.order * calc_Time(goal, currState)
    goal_order = populate_goals(args) # TODO! See method
    distance = []
    for goal in goal_order:
        distance[1] = goal.location - State.curr_loc
    if State.isHome and not State.sorted:
        # Go to Zone 1
        # State.isHome = False

    while not State.sorted:
        # Go counterclockwise through each zone and sort debris

    # Go to Z1, and go home from there.
    # Raise flag to indicate success


if __name__="__main__":
    main()
