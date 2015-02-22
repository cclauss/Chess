# -*- coding: utf-8 -*-
# R0 20150215T2048
def top(): pass
#                                                   CHESS
###################################################################################################################

# In this documentation, I'll be using functions that return strings.  These allow the documentation to be import-
# able from anywhere and read from anywhere.  I find it quite useful personally.

def move_logic(): return """
            HOW THE PROGRAM DETERMINES MOVE VALIDITY
––––––––––––––––––––––––––––––––––––––––––––––––––––
 The program determines whether or not a move is valid by applying the following
 steps, in order.  They are grouped into several levels in a logical order.

 +-Level 0
 | +- 0.0: select piece to move from board
 | +- 0.1: alert board for scheduled move
 | |       freeze board layout & other player
 +-Level 1
 | +- 1.0: determine if piece's color is correct
 | |       for the current turn
 | +- 1.1: test the move in the piece's ruleset
 | +- 1.2: test if the target is valid
 | +- 1.3: test if there are pieces "in the way"
 | |       of the move
 | +- 1.4: checkmate test
 +-Level 2
 | +- 2.0: freeze piece
 | +- 2.1: kill piece at target
 | +- 2.2: move piece
 | +- 2.3: unfreeze piece
 | |       alert board move is complete
 | |       unfreeze board & other player
"""

def class_interface(): return """
        HOW LOW-LEVEL CLASSES ACCESS DATA IN HIGHER LEVELS
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 A problem arises in level 1.2 of the move validation.  This problem is because
 level 1.2 checks the color of the piece at a target.  However, since the pieces are
 held in sets in an instance of the Chess.core.board.Board class, the individual
 pieces do not have access to the list they are contained in.  This means the piece
 cannot get the piece at it's target and therefore cannot check it's color.

 The solution to this is to store the board instance as an attribute of the piece.
 
 An example:
 ```
 class low_level (object):
     def __init__(self, y):
         self.y = y

 class mid_level (object):
     def __init__(self, a):
         self.a = low_level(a)
     
 class top_level (object):
     def __init__(self, x):
         self.x = mid_level(x)
 ```
 Now say the low_level class needs to access the top_level's x attr.  This can be done by:
 ```
 class low_level (object):
     def __init__(self, y):
         self.y = y
     def set_owner(self, o):
         self.owner = o

 class mid_level (object):
     def __init__(self, a):
         self.a = low_level(a)
         self.a.set_owner(self)
     def set_owner(self, o):
         self.owner = o
     
 class top_level (object):
     def __init__(self, x):
         self.x = mid_level(x)
         self.x.set_owner(self)
         self.z = 5
 ```
 Now, the class low_level can access the top_level by:
 self.owner.owner.z

 However, using this method, one must be careful not to cause indirect recursion errors by doing the following:
 `self.owner.a.owner.a.owner.`···
 as a is the low_level itself.  
"""

def use_of_eval(): return """
                 WHEN/WHERE/WHY IS EVAL() USED
––––––––––––––––––––––––––––––––––––––––––––––
 As a more experienced programmer will know, using the eval() function or the exec statement
 makes things slow.  If they're used often enough in a program, they make it REALLY slow.
 As such I have attempted to avoid using these.  There are 2 occasions of use so far:

 eval(): Chess.core.pieces.ChessPiece.__init__
         eval() is used to determine display character name from the Chess.constants file
  exact use: `self.disp_char = eval('d_{}_{}'.format(self.color.color, self.ptype))`

 eval(): Chess.core.pieces.ChessPiece.__init__
         eval() is used to determine FEN notation character name from the Chess.constants file
  exact use: `self.fen_char = eval('c_{}_{}'.format(self.color.color, self.ptype))`

 Both of these are only called once at piece instantiation time when the board is generated.  Because of
 this they will be used no more than 32 times per game generation.
"""

def import_cleanness(): return """
            WHAT IS A CLEAN IMPORT AND WHY IS IT IMPORTANT
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
 A clean import is a module within a package that doesn't import anything from the package.
 It may import standard library modules, such as `os` or `sys`, but with Chess as an example
 it cannot import anything that would begin with `Chess.` (such as `Chess.core.board`).
 
 Sometimes you may see a file saying it is a 1-level clean import -- what I meant by saying this
 is that the file only imports clean-import files.
 
 Why is it important?
 While writing this package, I constantly got ImportErrors that looked similar to this:
     
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "game_class.py", line 5, in <module>
        from Chess.core.board import Board, Tile, load
      File "/var/.../Chess/core/board.py", line 12, in <module>
        from Chess.boardio.load import loadgame, listgames
      File "/var/.../Chess/boardio/load.py", line 6, in <module>
        from Chess.core.board import Board
    ImportError: cannot import name Board

 As you can see from this traceback, in the Chess.core.game_class file I import Board from Chess.core.board.
 In Chess.core.board, I import Chess.boardio.load.
 In Chess.boardio.load, I import Chess.core.board.
 In Chess.core.board, I import Chess.boardio.load.
 And the loop of imports never ends.
 
 This is why clean imports are important -- importing something that isn't clean can often lead to errors.
 """

def links(): return """
                    USEFUL ONLINE READING
–––––––––––––––––––––––––––––––––––––––––

 A good list of links for reading that I'm not going to bother typing out again:
 http://stackoverflow.com/questons/494721/what-are-some-good-resources-for-writing-a-chess-engine/502029#502029
 
 An article that includes a bit of the history of computer chess as well:
 http://arstechnia.com/gaming/2011/08/force-fersus-heuristics-the-contentious-rise-of-computer-chess/
 
 The oblicatory Wikipedia link:
 http://en.wikipedia.org/wiki/Computer_chess
 
 How to read/write FEN strings
 http://en.wikipedia.org/wiki/Forsyth-Edwards_Notation
 
 A good article on algebraic chess notation
 http://chesshouse.com/how_to_read_and_write_chess_notation_a/166.htm
"""

def why_freeze(): return '''
            WHY FREEZE THE BOARD?
–––––––––––––––––––––––––––––––––
 The Chess.core.board.Board.freeze method is exactly as follows:
     
        ```
        def freeze(self):
            """Lock the board in place."""
            self.isFrozen = True
            self.pieces = list(self.pieces)
        ```
 
 The most inportant thing that happens is the `self.pieces = list(self.pieces)`.
 The reason:
     For the Chess.ai.basic.mover.make_random_move function to work, it needs to select a random
     element from the board's pieces.  From the `random` module sourcecode, the choice method does this:
         
         `return seq[int(self.random() * len(seq))]`
        
    Since the `set` type does not support indexing, `choice` cannot be used.  Therefore we must convert 
    the set of pieces to a list before the AI can make a choice.
'''
     

def bottom(): pass

