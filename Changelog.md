# Changelog
*Please not*: this log has only been updated since version 0.7.0, as this was effectively the first 'working' release.
This log is **only** for major features in each update.  I will not be listing every single character I change here, considering GitHub can do that for me.

### 0.7.1
 - Added castling ability to GUI
 - Added (*very* experimental) options screen
 - Functional `subvalidcache` cache mechanism - each piece gets a list of coords approved by its `apply_ruleset()` method to speed up operations like `valid()`
 - New bug: caches don't load properly on game creation (don't let the lack of green squares on the GUI fool you - you can still move)

### 0.7.0
 - Added functional GUI to Pythonista
 - Pawn promotion
 - Much improved file IO
 - Package-wide base class
 - integer_args() decorator - convert all float arguments such as 1.0, 2.0 to 1, 2 but **NOT** 1.5 or 2.5
 - Fix issue in Phantom.core.coord.point.Coord.as_chess() method where chess coordinates were given starting at 0 rather than 1
 - Fix issue where pawns would just...kind of...disappear randomly
 - New bug: pawns that can capture en passant can go just about anywhere
 - New bug: after a piece is killed, it does not become the other player's turn