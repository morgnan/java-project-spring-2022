#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Morgan Contrino
# email: mcontri@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Andrew Liu
# partner's email: aliu26@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        c = 0
        for a in range(3):
            #self.blank_r = 0 + a
            for b in range(3):
                if digitstr[c] == '0':
                    self.blank_c = 0 + b
                self.tiles[a][b] = str(digitstr[c])
                c+=1            
            if '0' in digitstr[0:3]:
                self.blank_r = 0
            elif '0' in digitstr[3:6]:
                  self.blank_r = 1
            elif '0' in digitstr[6:9]:
                self.blank_r = 2
           
    
    ### Add your other method definitions below. ###
    
    
    def give_tiles(self):
        """helper funtion for h2"""
        return self.tiles
        
    
    def __repr__(self):
        """returns a string representation of a Board object"""
        
        s = ''
        
        for num in self.tiles[0]:
            if num == '0':
                s += '_'+ ' '
            else:
                s += str(num) + ' '
        s += '\n'
        
        for num in self.tiles[1]:
            if num == '0':
                s += '_'+ ' '
            else:
             s += str(num) + ' '
        s += '\n'
        
        for num in self.tiles[2]:
            if num == '0':
                s += '_' + ' '
            else:
             s += str(num) + ' '
        s += '\n'
             
        return s
    
    
    def  move_blank(self, direction):
        """ takes as input a string direction that specifies the direction in
        which the blank should move, and that attempts to modify the contents 
        of the called Board object accordingly"""
        
        if direction == 'up':
            newr = self.blank_r - 1
            newc = self.blank_c
            if newr < 0:
                return False
            else:
                self.tiles[newr+1][newc] = self.tiles[newr][newc]
                self.tiles[newr][newc] = '0'
                self.blank_r -= 1
                return True
        elif direction == 'down':
            newr = self.blank_r + 1
            newc = self.blank_c
            if newr > 2:
                return False
            else:
                self.tiles[newr-1][newc] = self.tiles[newr][newc]
                self.tiles[newr][newc] = '0'
                self.blank_r += 1
                return True
        elif direction == 'left':
            newc = self.blank_c - 1
            newr = self.blank_r 
            if newc < 0:
                return False
            else:
                self.tiles[newr][newc+1] = self.tiles[newr][newc]
                self.tiles[newr][newc] = '0'
                self.blank_c -= 1
                return True
        elif direction == 'right':
            newc = self.blank_c + 1
            newr = self.blank_r 
            if newc > 2:
                return False
            else:
                self.tiles[newr][newc-1] = self.tiles[newr][newc]
                self.tiles[newr][newc] = '0'
                self.blank_c += 1
                return True
        else:
            return False
        
        
        
    def digit_string(self):
            """ creates and returns a string of digits that corresponds to 
            the current contents of the called Board object’s tiles attribute
            """
            
            digit = ''
            for c in self.tiles[0]:
                digit += c
            for d in self.tiles[1]:
                digit += d
            for e in self.tiles[2]:
                digit += e
            return digit
            
    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of 
        the called object"""
        
        newboard = Board(self.digit_string()) 
        
        return newboard
    
    
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object 
        that are not where they should be in the goal state"""
        
        misplaced = 0
        
        for tile in range(3):
            for num in range(3):
                if self.tiles[tile][num] != GOAL_TILES[tile][num] and \
                self.tiles[tile][num] != '0':
                     misplaced += 1    
        
        return misplaced
    
    
    def __eq__(self, other):
        """can be called when the == operator is used to compare two Board 
        objects. The method should return True if the called object (self) 
        and the argument (other) have the same values for the tiles attribute,
        and False otherwise"""
        
        if self.tiles == other.tiles:
            return True
        
        return False
    
    
