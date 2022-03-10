#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Morgan Contrino
# email: mcontri@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Andrew Liu
# partner's email: aliu26@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    def __init__(self, depth_limit):
        """constructs a new Searcher object by initializing the attributes 
        states, num_tested, and depth_limit"""
        
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def add_state(self, new_state):
        """takes a single State object called new_state and adds it to the 
        Searcher‘s list of untested states"""
        
        self.states += [new_state]
        
    def should_add(self, state):
        """takes a State object called state and returns True if the called 
        Searcher should add state to its list of untested states, and False 
        otherwise"""
        
        if self.depth_limit != -1 and self.depth_limit < state.num_moves:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True
            

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def add_states(self, new_states):
        """takes a list State objects called new_states, and that processes 
        the elements of new_states one at a time"""
        
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s


    def find_solution(self, init_state):
        """performs a full state-space search that begins at the specified 
        initial state init_state and ends when the goal state is found or when
        the Searcher runs out of untested states"""
        
        self.add_state(init_state)
        while len(self.states) > 0:
            self.num_tested += 1
            s = self.next_state()
            successors = s.generate_successors()
            if s.is_goal() == True:
                return s
            else:
                self.add_states(successors)
            
        return None
        

### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """a class for searcher objects that perform breadth-first search (BFS) 
    instead of random search. inherits from searcher class"""
    
    def next_state(self):
        """overrides the next_state method that is inherited from Searcher.
        Rather than choosing at random from the list of untested states, 
        this version of next_state follows FIFO ordering"""
        
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    """a class for searcher objects that perform depth-first search
    instead of random search"""
    
    def next_state(self):
        """overrides the next_state method that is inherited from Searcher.
        Rather than choosing at random from the list of untested states, 
        this version of next_state follows LIFO ordering"""
        
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def __init__(self, heuristic):
        """constructs a new GreedySearcher object"""
        
        super().__init__(-1)
        self.heuristic = heuristic
        
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher"""
        
        return -1 * self.heuristic(state)
    
    
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def add_state(self, state):
        """adds a sublist that is a [priority, state] pair, where priority is 
        the priority of state that is determined by calling the priority
        method"""
        
        self.states += [[self.priority(state), state]]
        
    
    def next_state(self):
        """overrides next_state from Searcher and choose one of the states 
        with the highest priority"""
        
        priority = max(self.states)
        self.states.remove(priority)
        return priority[1]
        
    
def h1(state):
    """ a heuristic function that computes and returns an estimate of how 
    many additional moves are needed to get from state to the goal state"""
    
    boards = state.board
    num = Board.num_misplaced(boards)
    return num


def h2(state):
    """a heuristic function that computes and returns an estimate of how many 
    moves are needed to get to the goal state more accurately than h1"""
    
    
    num_wrong = 0
    num_c = 0
    num_r = 0
    boards = state.board
    boardtiles = Board.give_tiles(boards)
    GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]
    
    
    for a in range(3):
        for b in range(3):
            if boardtiles[a][b] not in GOAL_TILES[a] and a < 2 and \
                boardtiles[a+1][b] != GOAL_TILES[a+1][b] and \
                boardtiles[a][b] != '0': 
                num_wrong += 1

            elif boardtiles[a][b] not in GOAL_TILES[a] and \
                  boardtiles[a][b] != '0' and GOAL_TILES[a][b] != '0':
                  num_c += 2
                 
            elif a < 2 and \
                boardtiles[a+1][b] != GOAL_TILES[a+1][b] and \
                boardtiles[a+1][b] != '0' and GOAL_TILES[a+1][b] != '0':
                    num_r += 1
                    
                
          
    return  num_c + num_r + num_wrong
                
    
   
   
### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    """an informed search algorithm that assigns a priority to each state
    based on a heuristic function, and that selects the next state based on 
    those priorities. considers the cost that has already been expended to
    get to that state"""
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher"""
        
        return -1 * (self.heuristic(state) + state.num_moves)

