# Phantom
Phantom is a (in development) game of Chess written in Python.  It's not very graphical but what it does have at the moment is the ability to pretty-print the board to the screen, ex:
```
  a b c d e f g h
8 r n b q k b n r 8
7 p p p p p p p p 7
6                 6
5                 5
4                 4
3                 3
2 P P P P P P P P 2
1 R N B Q K B N R 1 <
  a b c d e f g h
```
and will use Unicode characters as well.  A proper GUI is underway for the iOS app [Pythonista][0].  

Please note: this project is a huge learning experience for me.  This is the 3rd revision (I've restarted from scratch twice) of my ongoing chess project, each one getting better.  Hopefully there is no 4th revision.  If you find a bug, *please* don't hesitate to let me know so I can fix it.

## Features

- [x] Human vs. human play
- [ ] Checkmate detection  (work-in-progress)
- [x] Static board analysis (always improving)
- [ ] Move search engine (work-in-progress)
- [ ] Descriptive game notation
- [x] Move validation
- [x] En passant
- [x] Pawn promotion
- [x] Pretty printing
- [x] Save/load boards
- [x] Read/write FEN strings
- [x] Read EPD strings
- [ ] Write EPD strings
- [x] Algebraic chess notation
- [ ] Pythonista GUI *see below
- [ ] Windows GUI
- [x] Self-test suite
- [ ] Timers

*The basics of a GUI exist and work, however, at this time there is no support for promotion in the GUI, so it is considered incomplete for now.

## Installation
To download & extract PhantomChess, the first thing to do is download the `Phantom_installer.py` file in the master branch.  Place it in the directory to extract to and run.

### Easy method
Although it is more error-prone and not quite as user friendly as I'd like, a single executable is available (`Simple.exe`).  All you have to do is download this.  You don't even have to have Python installed to run it! (built with [PyInstaller][1])

## Static board analysis
How exactly does Phantom analyze a board and give it a score?  It uses a set of heuristics coded into the Phantom.ai.pos_eval.heuristics file.  This is a list of the currently active heuristics that are used to analyze a board:

- developed pieces
- advanced pawns
- separate scoring method for kings based on opening, midgame, endgame
- does player have the bishop pair
- has the player castled
- analyze pawn structure (work-in-progress)
- assess pawns, knights, bishops, rooks, queens & kings according to the Phantom.ai.pos_eval.piece_tables file (which came from [here][3])
- assess bad bishops

as well as the much simpler material analysis.

### Why no mobility heuristic?
Briefly considering how chess works, one would assume a piece that could make more moves would be more valuable.  And that would be correct, although it wouldn't make the piece as valuable as you might think because most legal moves in any given chess game *are pointless*.  Also, the main reason the function isn't put to use (it does exist in the file) is that it simply takes too long to generate the list of valid moves.

### Score system
Scores are given in "centipawns", such that 100 cp = 1 pawn.  The values used are too many to list here, and can be found in the Phantom.ai.settings file.

# Usage
To create and play a new game, simply do this:

```python
>>> import Phantom
>>> game = Phantom.ChessGame()
>>> game
  a b c d e f g h
8 r n b q k b n r 8
7 p p p p p p p p 7
6                 6
5                 5
4                 4
3                 3
2 P P P P P P P P 2
1 R N B Q K B N R 1 <
  a b c d e f g h
>>> game.move('e2e4')  # move the piece at e2 to e4
>>> game
  a b c d e f g h
8 r n b q k b n r 8 <
7 p p p p p p p p 7
6                 6
5                 5
4         P       4
3                 3
2 P P P P   P P P 2
1 R N B Q K B N R 1
  a b c d e f g h
```
In the Pythonista app, it is possible to activate a GUI for that game by `game.gui()`.  This feature is planned for Windows as well, but will most likely require the [Pygame][2] package.

# Contributing
Are you a programmer?  Know Python?  Interested in Phantom?  Feel free to help! I've never actually been taught Python, just learned it from trial & error, so I'm sure there's plenty of things that could be done much better.
Not a programmer but still interested in chess? Good, I need help there too! (I stink at chess).  Mainly the evaluation function - I don't have a good idea of what makes a board good or bad.
If you have any ideas, ***please*** open an issue or make a pull request so I can make things better.

[0]: http://omz-software.com/pythonista
[1]: https://github.com/pyinstaller/pyinstaller/wiki
[2]: http://pygame.org/news.html
[3]: https://chessprogramming.wikispaces.com/Simplified+evaluation+function
