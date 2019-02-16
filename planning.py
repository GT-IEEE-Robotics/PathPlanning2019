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

import queue

""" Goal class containing location of goal and reward for completion

Comparison operators are implemented to allow
Goal objects to be placed in a PQ
"""
class Goal:
    
    def __init__(self, loc=(), order):
        self.loc = loc
        self.order = order # Number representing the priority of goals
    
    def __gt__(self, other):
        if not isInstance(other, Goal):
            raise ValueError("Attempted to compare incorrect types")
        
        return self.order > other.order
    
    def __lt__(self, other):
        if not isInstance(other, Goal):
            raise ValueError("Attempted to compare incorrect types")
        
        return self.order < other.order
    
    @property
    def points(self):
        return self.points

class State:
    
    sorted = False
    isHome = True # Robot always starts at home

    def __init__(self, goal):
        self.next_goal = goal
        #self.curr_loc will represent current location of robot
    
    @property
    def next_goal(self):
        return self.next_goal
    
    @staticmethod
    def initial_state():
        return State(None) # 

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
        
""" TODO
"""
# def TSP():

""" Things to consider

Right now the approach is to targe the goal 
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
    print("Hello World")
    grid = ()
    goal_order = populate_goals(args) # TODO! See method
    if State.isHome and not State.sorted:
        # Go to Zone 1
        # State.isHome = False
    
    while not State.sorted:
        # Go counterclockwise through each zone and sort debris
    
    # Go to Z1, and go home from there.
    # Raise flag to indicate success
    

if __name__="__main__":
    main()
    
